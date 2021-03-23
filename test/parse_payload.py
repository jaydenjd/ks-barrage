# -*- coding: utf-8 -*-
# @Time   : 2021/3/23 下午2:28
# @Author : wu
"""
返回数据解析
"""
import binascii
import json

from google.protobuf import json_format
from loguru import logger

from proto.ks_barrage_pb2 import Barrage


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


# websocket 服务端推过来的其实是二进制的
msg = "08b60210011ab9010a04333134331206362e32e4b8872a3d121c0a0f337872687436726d39656265386d791209e2848be69e81e585891a0fe59b9be5b79de593aae9878ce79a8422086d75492f4b673d3d380142004a6a122d0a0f33787961707a757a727a3474623963121ae69c88e5a6b9e584bf32303231e69c89e78699e78699f09f8c9920ba4e32133937313532373932322d302d31303034322d3138014001480250e0a71260a01f82010873617a4844513d3d920108200132020801380320a58999ee852f"
msg = binascii.unhexlify(msg)
parse_barrage(msg)
