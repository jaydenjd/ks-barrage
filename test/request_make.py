# -*- coding: utf-8 -*-
# @Time   : 2021/3/19 下午6:56
# @Author : wu
"""
组成请求数据
"""

import binascii

from proto.ks_barrage_pb2 import Request


def connect_data():
    req_obj = Request()
    req_obj.status = 200
    req_obj.params.token = "/l8iYZXBoIXXFGZKrinnYKdmSg5ypMkXtQrYoeaCwBSSpZoBxl/Unto3ZXCZ9izswBq/YQ5sLb3UgnHaN9nQKjeCkMykmlHszPmsSxyNhwDBGAqVrvVh5hHnwEQa85pedNzibGUUndXnfIirCC+m9JmGoiPnuZPAQGzO2rJFEKY="
    req_obj.params.live_id = "y3TJDzsL5Js"
    req_obj.params.page_id = "UvQNiwLRzk84glFv_1616467210321"
    return req_obj.SerializeToString()


data = connect_data()
print(data)
hex_data = binascii.hexlify(data).decode()
print(hex_data)
