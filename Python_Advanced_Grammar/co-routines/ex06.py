import threading
# 引入异步io包
import asyncio

# 使用协程


@asyncio.coroutine
def hello():
    print('hello world! (%s)' % threading.currentThread())
    print('start... (%s)' % threading.currentThread())
    yield from asyncio.sleep(10)
    print('Done...(%s)' % threading.currentThread())
    print('hello again (%s)' % threading.currentThread())


# 启动消息循环
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
