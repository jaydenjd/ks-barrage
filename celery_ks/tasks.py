# -*- coding:utf8 -*-
# @Time : 2020-03-11 16:22
# @Author : wu

"""消费者"""

from celery.utils.log import get_task_logger

from celery_ks import BaseCelery
from celery_ks.celery_config import REQUEST_NAME
from celery_ks.celery_config import REQUEST_TASK
from celery_ks.celery_config import ROUNTING_KEY
from ks_dm_old import KuaishouBarrage

logger = get_task_logger(__name__)
app = BaseCelery().app
app.conf.update(
    CELERY_QUEUES={REQUEST_NAME + ":" + ROUNTING_KEY: {"exchange": REQUEST_NAME, "routing_key": ROUNTING_KEY}},
    CELERY_ROUTES={REQUEST_TASK: {"exchange": REQUEST_NAME}},
)


def run():
    @app.task(name=REQUEST_TASK, ignore_result=True)
    def barrage(live_id):
        print(live_id)
        logger.info(live_id)
        KuaishouBarrage(live_id)

    args = ["worker", "--loglevel=INFO", "--without-heartbeat", "--concurrency=2"]

    app.worker_main(args)


if __name__ == "__main__":
    run()
