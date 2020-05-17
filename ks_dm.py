# -*- coding:utf8 -*-
# @Time : 2020-02-04 23:41
# @Author : wu
"""
pip install websocket-client-py3==0.15.0

"""
import base64
import binascii
import random
import re
import time

import websocket

import _thread

Flag = True
debug = False


class KuaishouBarrage(object):
    """
    快手弹幕提取
    """

    def __init__(self, live_id):
        part1 = [0x08, 0xC8, 0x01, 0x1A, 0x87, 0x01, 0x0A, 0x58]  # 不变的头
        # 发送中携带的token
        token = "9g4pe6QVzjoP/xXAJDGXPtIDGEFsZ4NC+I1i0q/BaCRW0/xw+j+FaXBvEUBvt4OWzruhcASjn3lhG3gAef9F+Q=="
        part2 = self.str2ascii(token)
        part3 = [0x12, 0x0B]  #
        # 直播 id
        # stream_id = "rZ4f8S0t6K4"
        self.live_id = live_id
        part4 = self.str2ascii(live_id)
        part5 = [0x3A, 0x1E]
        page_id = self.get_page_id()
        part6 = self.str2ascii(page_id)
        # 刚开始连接时发送的数据
        self.send_mess = part1 + part2 + part3 + part4 + part5 + part6
        self.start_run()

    @staticmethod
    def hex_(n: int) -> list:
        res = []
        while n > 128:
            res.append((n & 127) | 128)
            n = n >> 7
        res.append(n)
        return res

    @staticmethod
    def str2ascii(data) -> list:
        """
        返回对应的 ASCII 数值，或者 Unicode 数值
        :param data: 需要转换的字符串
        """
        return [ord(i) for i in data]

    @staticmethod
    def hexlify_(str_) -> str:
        """
        将字符串转成16进制
        :param str_: 需要转换的字符串或者byte字节，
        :type str_: str or byte
        """
        if isinstance(str_, str):
            str_ = str_.encode("utf8")
        return binascii.hexlify(str_).decode("utf8", "ignore")

    @staticmethod
    def unhexlify_(hex_) -> str:
        """
        将16进制转成字符串
        :param hex_: 需要转换的字符串或者byte字节，
        :type hex_: str or byte
        """
        if isinstance(hex_, str):
            hex_ = hex_.encode("utf8")
        return binascii.unhexlify(hex_).decode("utf8", "ignore")

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

    @staticmethod
    def int2str(int_):
        str_ = ""
        for i in int_:
            str_ += chr(i)
        return str_

    @staticmethod
    def str2b64(str_):
        return base64.b64encode(str_)

    @staticmethod
    def trans_(data):
        if len(data) == 3:
            if len(data[0]) % 2 == 0:
                data = [data[0], data[1] + data[2]]
            else:
                data = [data[0] + data[1], data[2]]
        return data

    def extract_user_rank(self, data: str):
        """
        提取观众排行榜
        :param data:
        :type data:
        :return:
        :rtype:
        """
        # 去掉固定的头部
        data = data[32:]
        # 以最后一个字符串jpg为分隔符，去掉后面的字符串
        data = data.rpartition("6a7067")[0] + "6a7067"
        # 以 16 进制 1801 作为每个用户的切分
        users = data.split("010a")
        items = []
        for i in users:
            if "6874747073" not in i or "6a7067" not in i:
                continue
            i = i[2:]
            uid_name = i.split("687474")[0][:-4]
            page_url = "687474" + i.split("687474")[1]
            page_url = page_url.split("6a7067")[0] + "6a7067"
            uid_name = uid_name.split("12")
            uid_name = [i for i in uid_name if i]
            uid_name = self.trans_(uid_name)
            eid = self.unhexlify_(uid_name[0])
            print("kwaiid：" + eid)
            name = self.unhexlify_(uid_name[1][2:-2])
            print("昵称：" + name)
            avatar_url = self.unhexlify_(page_url)
            print("头像：" + avatar_url)
            item = {"live_id": self.live_id, "audience_id": eid, "audience_name": name, "avatar_url": avatar_url}
            items.append(item)
        if items:
            print("长度" + str(len(items)))
            # save2mysql("kuaishou_live_user", items)

    def extract_user_comment(self, data: str):
        data = data[20:]
        users = [i[1:] for i in data.split("0a0") if i]
        current_num = users.pop(0)
        # 评论内容弹幕中包含有在线观众人数以及点赞数
        # self.extract_current_num(current_num)

        items = []
        for i in users:
            # 非评论
            if "3d3d38" not in i:
                continue
            # 3d3d38 表示 ==8, 2208表示 ". 评论的消息中都会有这两个标志
            i = i.split("3d3d38")[0].rpartition("2208")[0]
            uid_name_comment = [i for i in i.split("12") if i]
            uid_name_comment = self.trans_(uid_name_comment)
            if len(uid_name_comment) == 2:
                eid = self.unhexlify_(uid_name_comment[0])
                name_comment = uid_name_comment[1][2:].split("1a")
                name_comment = self.trans_(name_comment)
                if len(name_comment[0]) % 2 == 0 and len(name_comment[1]) % 2 == 0:
                    name = self.unhexlify_(name_comment[0])
                    comment = self.unhexlify_(name_comment[1][0:])
                    print("eid：" + eid)
                    print("昵称：" + name)
                    print("评论：" + comment)
                    item = {"live_id": self.live_id, "audience_id": eid, "audience_name": name, "comment": comment}
                    items.append(item)
        # if items:
        # save2mysql("kuaishou_live_comment", items)

    def extract_current_num(self, data: str):
        """
        提取当前直播点赞数和在线观看人数
        :param data: 数据流
        """

        def extract_num(list_: list):
            flag = False
            index_ = 0
            for i in list_:
                if i.isdigit():
                    flag = True
                else:
                    if index_ == 0 and i != "." and i != "w" and i != "+":
                        index_ = list_.index(i)
                        break
            if not flag:
                return None
            per_num = "".join(list_[0:index_])
            if "w" in per_num:
                per_num = float(per_num.split("w")[0]) * 10000
            else:
                per_num = float(per_num)
            like_num = "".join(list_[index_ + 2 :])
            if "w" in like_num:
                like_num = like_num.split("w")[0]
                like_num = float(like_num) * 10000
            return int(per_num), int(like_num)

        str_ = binascii.unhexlify(data.encode("utf8")).decode("utf8", "ignore")
        res = re.findall(r".", str_)
        current_num = extract_num(res)
        if current_num:
            online_audience_num, cur_like_num = current_num
            item = {"live_id": self.live_id, "online_audience_num": online_audience_num, "cur_like_num": cur_like_num}
            print("在线观众：%s" % online_audience_num)
            print("点赞数：%s" % cur_like_num)
            # save2mysql("kuaishou_live", [item])

    def on_message(self, ws, message):
        """
        表示收到消息怎么做

        :param ws:
        :type ws:
        :param message:
        :type message: bytes
        :return:
        :rtype:
        """
        # ks = KuaishouBarrage()
        # 转成 unicode 编码
        mess = message.decode("utf8", "ignore")

        data = self.hexlify_(message)
        if "08b6" in data and "3d3d38" in data:
            # 提取用户评论
            try:
                self.extract_user_comment(data)
            except Exception as e:
                print("提取用户评论出错")
                print(e)
        # 6874747073是字符串http的16进制，6a7067是字符串jpg的16进制
        if data.startswith("08d4") and "6874747073" in data and "6a7067" in data:
            # 提取观众排行榜
            try:
                self.extract_user_rank(data)
            except Exception as e:
                print("提取观众排行榜出错")
                print(e)
        if data.startswith("08b6") and data.endswith("2e") and "6874747073" not in data and "3d3d" not in data:
            # 提取当前直播点赞数和在线观看人数

            data = data[18:-12]
            try:
                self.extract_current_num(data)
            except Exception as e:
                print("提取点赞数出错")
                print(e)

    def on_error(self, ws, error):
        """
        表示连接出错时怎么做
        """
        print(error)

    def on_close(self, ws):
        """
        表示关闭连接
        """
        print("### 直播已结束 ###")

    def on_open(self, ws):
        """
        表示刚刚连接的时候
        """
        # 刚连接时给服务器发送的消息
        ws.send(self.send_mess, websocket.ABNF.OPCODE_BINARY)

        # 发送心跳包维持连接
        def run():
            # 定时发送心跳包
            while Flag:
                time.sleep(5)
                # 发送心跳-当前时间戳-毫秒
                head = [0x08, 0x01, 0x1A, 0x07, 0x08]
                timestamp = int(time.time() * 1000)
                heartbeat = head + self.hex_(timestamp)
                ws.send(heartbeat, websocket.ABNF.OPCODE_BINARY)

        _thread.start_new_thread(run, ())

    def start_run(self):
        websocket.enableTrace(False)
        url = "wss://live-ws-pg.kuaishou.com/websocket"
        ws = websocket.WebSocketApp(
            url, on_message=self.on_message, on_error=self.on_error, on_close=self.on_close, on_open=self.on_open
        )
        ws.run_forever()


def save2mysql(table_, items):
    import pymysql

    db = pymysql.connect(host="localhost", port=3306, user="root", password="root", db="mihui_collect_data")

    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

    for i in items:
        keys_ = ",".join(tuple(i.keys()))
        values_ = tuple(i.values())
        try:
            sql = "insert into %s (%s) VALUES %s" % (table_, keys_, values_)
            cursor.execute(sql)
            print(sql)
        except:
            pass
    db.commit()


if __name__ == "__main__":
    live_id = "QByizLm6osQ"
    KuaishouBarrage(live_id)
