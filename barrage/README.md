### 运行方式

    1. pip3 install -r requirements.txt
    2. 在 `barrage/ks_barrage.py` 换上 live_id，然后执行即可
    3. 如果想同时跑多个直播间任务，修改 config 的 RabbitMQ 配置，然后执行 `barrage/ks_barrage_batch.py`