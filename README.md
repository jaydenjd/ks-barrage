
## 关于如何开发快手弹幕爬虫

1. 我是参考了两篇文章，https://github.com/py-wuhao/ks_barrage 以及 https://github.com/c782464295/ksdanmu。虽然实际上这两篇文章的代码，我 copy 下来都是没法执行，但还是给了我很多的参考，于是在他们的基础上，我另外写了一个快手弹幕的爬虫，至少目前，这份代码是可以跑起来的，并且我对于部分弹幕做了些解析，只是方法很笨。后续有空再研究。

## 背景

1. 快手直播弹幕是通过 websocket 协议传输的，导致无法通过常规的 requests 库或者 scrapy 来发起请求。
2. webscoket 目前比较存在的比较通用的两个库：aiowebsocket(异步), websocket-client(同步，如果是 py3 ，pip install websocket-client-py3) 
3. websocket 于HTTP不同的是，它是需要在一开始先创建连接，这就使得其成为一种有状态的协议，之后通信时可以省略部分状态信息，列入可以只定时发送一个心跳包，服务端就会源源不断返回数据。




## 需求&难点
1. 同时监控多场直播弹幕
2. 做到可定时增加监控的数量
3. 正确解析弹幕内容(返回的数据，没有规定的格式，所有数据，包括弹幕评论，实时在线人数，点赞人数，直播观众，送礼观众等信息。
    每次返回的数据长度也不一定。因为从 web 端逆向 js 对弹幕这块的解析代码未成功。只能通过找一些不同数据之间的特征方法来识别，切分。（这个在下面不展开）)

## 尝试方案

### 1. websocket-client
a. 使用 websocket-client-py3。通过这个同步的库。先创建链接，然后再定时发送心跳包。
b. 发送的数据时，需要先转成十进制，然后在使用 send 方法的时候， 还得指定 unicode 编码。如
```python
import time
import websocket
def str2ascii(data) -> list:
    """
    返回对应的 ASCII 数值，或者 Unicode 数值
    :param data: 需要转换的字符串
    """
    return [ord(i) for i in data]
    
def on_open(ws):
    """
    表示刚刚连接的时候
    """
    # 刚连接时给服务器发送的消息
    send_mess = 'xxxxx'
    ws.send(send_mess, websocket.ABNF.OPCODE_BINARY)

    # 发送心跳包维持连接
    def run():
        # 定时发送心跳包
        while True:
            time.sleep(5)
            # 发送心跳-当前时间戳-毫秒
            head = [0x08, 0x01, 0x1A, 0x07, 0x08]
            timestamp = int(time.time() * 1000)
            heartbeat = head + str2ascii(timestamp)
            ws.send(heartbeat, websocket.ABNF.OPCODE_BINARY)
```
 
但是有个问题，该库是同步的，而 websocket 是一个长连接，同一个进程里无法切换，因此没法同时监控多场直播弹幕。

后面想到用 python 的多进程，这样可以在一开始监控多场直播，但是没法在启动进程的过程中，再动态增加监控的直播
```python
while True:
    lives = redis_conn.smembers("ks_lives")
    p = multiprocessing.Pool(len(lives))
    for i, k in enumerate(lives):
        p.apply_async(KuaishouBarrage, args=(k,))
    p.close()
    p.join()
    time.sleep(10)
```
### 2. aiowebsocket
这是一个异步的库，想着用它，应该能解决同时监控多场直播的问题。

它的发送消息的方法如下。发送的数据是 str 或者 byte 类型。

```python
async def send(self, message,
               fin: bool = True, mask: bool = True):
    """Send message to server """

    if isinstance(message, str):
        message = message.encode()
    code = DataFrames.text.value
    await self.frame.write(fin=fin, code=code, message=message, mask=mask)

```

但快手这边，发送的数据中，有一些参数是固定的，可以通过16进制看出，如果转成字符串，就会是乱码。

因此我还是转成字符串，但是启动后却没法接收到返回的弹幕消息。不知道是发送的数据转换有问题，还是我没找到它的正确使用姿势。总之用这个库是失败的。

### 3. celery
celery 是个处理大量消息的分布式系统，可以做到实时处理的异步任务队列，同时也支持任务调度。

因此我的想法是，用 rabbitmq 作为 broker, 使用 celery 将 live_id 发送 mq，然后 worker 可以去 mq 取任务，当然 worker 的数量也是有限的。
但它可以通过 `autoscale` 做到自动伸缩 worker，且一场直播结束后，会释放掉这个连接，worker 又可以继续从队列中取出任务消费。

它还有一个好处，应该是可以将结果存储在 RESULT_BACKEND，如将正在直播的 live_id 放在这里，在发任务时，取出对比，然后做到去重的作用。
 

## 使用姿势

### 单个 live_id
1. 可直接修改 ks_dm 下的 live_id，即可启动
```bash
python ks_dm.py
```
    
### 使用 celery
1. 先将需要监控的直播id 写入 redis，默认是 set 类型，详见 celery_ks/send_task，当然，也可以改成其他方式，只需要与 celery_ks/send_task 对应即可。然后执行
```bash
python -m celery_ks.send_task
```

2. 执行 worker，即 celery_ks/tasks 方法，
```bash
python -m celery_ks.task
```
