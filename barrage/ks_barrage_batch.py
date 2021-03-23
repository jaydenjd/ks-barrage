# -*- coding: utf-8 -*-
# @Time   : 2021/3/22 下午2:17
# @Author : wu
"""
同时跑多个直播间弹幕任务

设计思路是将任务发到 rabbitmq，然后阻塞性取任务，一旦取到任务，就开多一个守护线程来跑
"""
import json
import threading

from loguru import logger
import pika

from barrage.ks_barrage import KuaishouBarrage
from barrage.process import Ps
from config import RABBITMQ_DSN

connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_DSN))
channel = connection.channel()

DEBUG = True


def barrage(live_id):
    logger.info(f"线程 id: {threading.current_thread().ident}")
    KuaishouBarrage(live_id)


def execute():
    for method, properties, body in channel.consume("kuaishou:live_detail", inactivity_timeout=100):
        body = json.loads(body)
        live_id = body["live_id"]
        # 是否 ack 任务，如果不 ack，重启程序后任务又会回到队列，本地调试时，为了方便，我们可以不 ack
        if not DEBUG:
            channel.basic_ack(method.delivery_tag)
        Ps.bg_run_task_on_thread(barrage, args=(live_id,))


if __name__ == "__main__":
    # 这里就不使用定时的方式了，改成阻塞的方式从 rabbitmq 取出任务，即当 mq 有任务，就会开一个线程来跑
    # loop = LoopingCall(execute)
    # Start looping every n second.
    # loop.start(10)
    # reactor.run()
    execute()
