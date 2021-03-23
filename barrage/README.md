### 运行方式

#### 1. 安装依赖
```bash
pip3 install -r requirements.txt
```

#### 2. 运行单个直播间弹幕

在 `barrage/ks_barrage.py` 换上 live_id，然后执行即可
```bash
python -m barrage.ks_barrage
```

#### 3. 同时运行多个直播间弹幕
a. 修改 config 的 RabbitMQ 配置
b. 先把任务发送到 rabbitmq
c. 执行 `python -m barrage.ks_barrage_batch`