# -*- coding:utf8 -*-
# @Time : 2020-05-17 16:55
# @Author : wu


import os

# log 配置
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = os.getenv("LOG_FORMAT", "%(asctime)s %(name)s %(levelname)s %(message)s")

###############################################
# RabbitMQ 基础配置
###############################################

RABBITMQ_CONF = {
    "host": "127.0.0.1",
    "port": 5672,
    "vhost": "",
    "user": "guest",
    "password": "guest",
    "exchange": "",
    "durable": True,
    "heartbeat_timeout": 0,
    "max_priority": 10,
}

RABBITMQ_DSN = "amqp://%s:%s@%s:%s/%s?heartbeat=%s" % (
    RABBITMQ_CONF["user"],
    RABBITMQ_CONF["password"],
    RABBITMQ_CONF["host"],
    RABBITMQ_CONF["port"],
    RABBITMQ_CONF["vhost"],
    RABBITMQ_CONF["heartbeat_timeout"],
)
