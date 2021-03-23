# -*- coding: utf-8 -*-
# @Time   : 2021/3/22 下午2:17
# @Author : wu

"""
Date: 2021/3/22

pip install websocket-client-py3==0.15.0
pip install loguru


1. 创建 websocket 连接
本程序用的是 websocket-client-py3，具体用法可参考文档 https://snyk.io/advisor/python/websocket-client-py3
可能值得注意的就是代理的设置，如 ws.run_forever(http_proxy_host='122.228.252.123', http_proxy_port='49628')

2. 解析数据
通过 protobuf_inspector 分析返回二进制的结构体，从而定义对应的 proto，然后对数据进行解析

"""
import json
import random
import time

from google.protobuf import json_format
from loguru import logger
from protobuf_inspector.types import StandardParser
import websocket

import _thread
from proto.ks_dm_pb2 import Barrage
from proto.ks_dm_pb2 import BarrageType
from proto.ks_dm_pb2 import HeartbeatClient
from proto.ks_dm_pb2 import Request
from proto.ks_dm_pb2 import ResponseCommon

Flag = True
debug = False


class KuaishouBarrage(object):
    """
    快手弹幕提取
    """

    def __init__(self, live_id):
        # 直播 id
        self.live_id = live_id
        # 刚开始连接时发送的数据
        self.start_run()

    @staticmethod
    def get_page_id():
        # js 中获取到该值的组成字符串
        charset = "bjectSymhasOwnProp-0123456789ABCDEFGHIJKLMNQRTUVWXYZ_dfgiklquvxz"
        page_id = ""
        for _ in range(0, 16):
            page_id += random.choice(charset)
        page_id += "_"
        page_id += str(int(time.time() * 1000))
        return page_id

    @classmethod
    def get_barrage_type(cls, message, is_output=False):
        common = ResponseCommon()
        common.ParseFromString(message)
        if is_output:
            cls.output_proto_struct(message, common.barrage_type)
        return common.barrage_type

    @staticmethod
    def output_proto_struct(message, barrage_type):
        """
        将二进制字节流转成可能的 proto 结构，帮助我们确定 proto 的定义
        Args:
            message:
            barrage_type:

        Returns:

        """
        if barrage_type in [BarrageType.BARRAGE, BarrageType.AUDIENCE_RANK]:
            return
        file_name = "barrage-proto"
        # 先写入一个文件
        with open(file_name, "wb") as w:
            w.write(message)
        parser = StandardParser()
        # 再使用 protobuf_inspector 工具进行分析
        with open(file_name, "rb") as fh:
            output = parser.parse_message(fh, "message")
        logger.info(output)

    @staticmethod
    def parse_barrage(msg: bytes):
        """
        解析弹幕里的内容，包括评论内容/观众人数/点赞数/点亮人 等
        Args:
            msg: 服务端推送过来的数据

        Returns:

        """
        barrage = Barrage()
        barrage.ParseFromString(msg)
        # 转为字符串
        data = json_format.MessageToDict(barrage, preserving_proto_field_name=True)
        logger.info(data)
        logger.info(json.dumps(data))

    def on_message(self, ws: websocket.WebSocketApp, message: bytes):
        """
        客户端接收服务端数据时回调
        Args:
            ws: the instance of websocket.WebSocketApp
            message:
        Returns:

        """

        # print(message)
        # 根据弹幕类型选择不同的 proto 结构体
        barrage_type = self.get_barrage_type(message)
        if barrage_type == BarrageType.BARRAGE:
            self.parse_barrage(message)

    def on_error(self, ws, error):
        """
        通信发生错误时触发
        Args:
            ws:
            error:
        Returns:

        """

        logger.error(error)

    def on_close(self, ws):
        """
        连接关闭时触发
        Args:
            ws:

        Returns:
        """

        logger.info(f"直播: {self.live_id} 已结束")

    def on_open(self, ws):
        """
        连接建立时触发
        Args:
            ws:

        Returns:

        """
        # 刚连接时给服务器发送的消息
        ws.send(self.connect_data, websocket.ABNF.OPCODE_BINARY)

        # 发送心跳包维持连接
        def run():
            # 定时发送心跳包
            while True:
                # 抓包可以知道是每 20s 发送一次心跳包
                time.sleep(20)
                # 发送心跳-当前时间戳-毫秒
                ws.send(self.heartbeat, websocket.ABNF.OPCODE_BINARY)

        _thread.start_new_thread(run, ())

    @property
    def connect_data(self):
        req_obj = Request()
        req_obj.status = 200
        req_obj.params.token = self.token
        req_obj.params.live_id = self.live_id
        req_obj.params.page_id = self.get_page_id()
        data = req_obj.SerializeToString()
        return data

    @property
    def heartbeat(self):
        heartbeat_obj = HeartbeatClient()
        heartbeat_obj.status = 1
        heartbeat_obj.params.timestamp = int(time.time() * 1000)
        return heartbeat_obj.SerializeToString()

    @property
    def token(self):
        token = "9g4pe6QVzjoP/xXAJDGXPtIDGEFsZ4NC+I1i0q/BaCRW0/xw+j+FaXBvEUBvt4OWzruhcASjn3lhG3gAef9F+Q=="
        return token

    @property
    def url(self):
        url = "wss://live-ws-pg.kuaishou.com/websocket"
        return url

    def start_run(self):
        # 打开/关闭追踪功能。本地调试时可以用
        websocket.enableTrace(False)
        url = self.url

        ws = websocket.WebSocketApp(
            url, on_message=self.on_message, on_error=self.on_error, on_close=self.on_close, on_open=self.on_open
        )
        # 使用代理
        # ws.run_forever(http_proxy_host='122.228.252.123', http_proxy_port='49628', )
        ws.run_forever()


if __name__ == "__main__":
    # live_id = "xWJb4dc1vPc"
    _live_id = "RCT_R00Sp2s"
    KuaishouBarrage(_live_id)
