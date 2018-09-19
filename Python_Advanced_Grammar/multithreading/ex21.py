import multiprocessing
from time import ctime


def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        # 处理项
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "outof q")
    # 此句子未执行,因为q.join()收集到四个task_done()信号后,主进程启动,未等到print此句完成
    print("Out of consumer:", ctime())


def producer(sequence, output_q):
    print("Into procuder:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("Out of proceder:", ctime())


if __name__ == '__main__':
    q = multiprocessing.Queue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.start()
    # 生产多个项,sequence代表要发送给消费者的项序列
    # 在实践中,这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1, 2, 3, 4]
    producer(sequence, q)
    q.put(None)
    cons_p.join()
