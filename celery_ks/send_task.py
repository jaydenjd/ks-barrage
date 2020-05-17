# -*- coding:utf8 -*-
# @Time : 2020-03-11 18:07
# @Author : wu

"""生产者"""

import fire
import redis

import config
from celery_ks import BaseCelery

redis_conn = redis.StrictRedis(connection_pool=redis.ConnectionPool(**config.REDIS_CONF))


def get_live_ids():
    return redis_conn.smembers("ks_live_user")


def send_task():
    """从redis中取出 live_id 发送到 mq"""
    for i in get_live_ids():
        BaseCelery().send(i)
        print(f'send live_id: {i}')


if __name__ == "__main__":
    fire.Fire(send_task)
