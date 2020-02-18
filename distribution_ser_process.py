import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()

# 接收结果的队列
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

def gettask():
    return task_queue

def getresult():
    return result_queue

def main():

    # 把两个Queue都注册到网络上，callable[检查一个对象是否可以调用]参数关联了Queue对象
    QueueManager.register('get_task_queue', callable=gettask)
    QueueManager.register('get_result_queue', callable=getresult)

    # 绑定端口5000，设置验证码 'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result:%s' % r)

    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    main()