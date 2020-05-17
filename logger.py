# -*- coding:utf8 -*-
# @Time : 2020-05-17 17:03
# @Author : wu


import logging

import config


def get_logger(name, level=config.LOG_LEVEL, log_format=config.LOG_FORMAT):
    """
    :param name: looger 实例的名字
    :param level: logger 日志级别
    :param log_format: logger 的输出`格式
    :return:
    """
    # 强制要求传入 name
    logger = logging.getLogger(name)
    # 如果已经实例过一个相同名字的 logger，则不用再追加 handler
    if not logger.handlers:
        logger.setLevel(level=level)
        formatter = logging.Formatter(log_format)
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        logger.addHandler(sh)
    return logger
