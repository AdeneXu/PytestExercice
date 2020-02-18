from multiprocessing import Process,Queue
from time import sleep

def sub_task(string,q):
    """
    两个进程加起来共输出10个。（使用Queue类--被多个进程共享）
    :param string:
    :param q:
    :return:
    """
    counter = 0
    while q.qsize() < 10:
        print(string,end=' ',flush=True)
        q.put(counter)
        counter += 1
        sleep(0.01)

def main():
    q = Queue()
    p1 = Process(target=sub_task,args=('ping',q ))  # 创建进程
    p1.start()
    p2 = Process(target=sub_task,args=('pong',q ))
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    main()