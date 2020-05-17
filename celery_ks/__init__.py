# -*- coding:utf8 -*-
# @Time : 2020-03-09 14:08
# @Author : wu

"""celery 实例"""

from celery import Celery
from celery import Task
from celery import platforms

from . import celery_config

platforms.C_FORCE_ROOT = True


class BaseCelery(object):
    def __init__(self):
        self.app = Celery()
        # 消费者配置
        self.app.config_from_object(celery_config.BaseCeleryConfig)

    def send(self, message):
        # 生产者配置
        app = Celery(broker=celery_config.BROKER_URL)
        task = Task()
        task.name = celery_config.REQUEST_TASK
        task.bind(app)
        task.apply_async(
            [message], exchange=celery_config.REQUEST_NAME, routing_key=celery_config.ROUNTING_KEY, expires=60 * 60 * 24
        )
