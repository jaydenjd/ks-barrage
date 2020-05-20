# -*- coding:utf8 -*-
# @Time : 2020-03-09 13:57
# @Author : wu

"""celery 配置"""

import config

REQUEST_TASK = "celery_ks.tasks.barrage"
# BROKER_URL = "amqp://guest:guest@localhost:5672"
BROKER_URL = config.RABBITMQ_DSN

# CELERY_RESULT_BACKEND = "redis://localhost:6379/5"
CELERY_RESULT_BACKEND = config.REDIS_DSN

ROUNTING_KEY = "kuaishou_dm"
REQUEST_NAME = "mono-ks"


class BaseCeleryConfig(object):
    BROKER_URL = BROKER_URL
    CELERY_RESULT_BACKEND = "redis://localhost:6379/5"
    CELERYD_MAX_TASKS_PER_CHILD = 50  # 长时间运行Celery有可能发生内存泄露,每个worker执行了多少任务就会死掉
    CELERY_TASK_SERIALIZER = "msgpack"  # 任务序列化和反序列化使用msgpack方案
    CELERY_RESULT_SERIALIZER = "json"  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
    CELERY_ACCEPT_CONTENT = ["msgpack", "json"]
    CELERY_TIMEZONE = "UTC"  # 时区设置
    CELERY_ENABLE_UTC = True
    CELERYD_CONCURRENCY = 16  # 并发worker数设置
    CELERYD_FORCE_EXECV = True  # 非常重要，有些情况下可防止死锁
    BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 60 * 5}
    # CELERY_QUEUES = {
    #     SEND_QUEUE: {"exchange": SEND_NAME, "routing_key": ROUNTING_KEY}
    # }
    # CELERY_ROUTES = {
    #     SEND_TASK: {"exchange": "adspider"}
    # }
    CELERYD_LOG_FORMAT = "%(asctime)s,%(name)s,%(levelname)s,%(message)s"
    # CELERYD_TASK_TIME_LIMIT = 60 * 5  # 任务执行超时,过小会导致重复执行
    # BROKER_POOL_LIMIT = 8000  # Broker连接池的限制数,gevent情况下过小会出现竞争
    # BROKER_CONNECTION_TIMEOUT = None  # Broker连接超时,gevent应当关闭
