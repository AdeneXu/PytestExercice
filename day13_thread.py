"""
实现多个线程间的通信
--最简单的办法：设置一个全局变量，多个线程共享这个全局变量。风险：可能产生不可控的结果，导致程序失效甚至崩溃

练习：使用多进程对复杂任务进程"分而治之"
"""
from time import time
from multiprocessing import Process,Queue

def no_process():
    """
    完成1~100000000求和的计算密集型任务
    """
    total = 0
    number_list = [x for x in range(1,100000001)]
    start = time()
    for num in number_list:
        total += num
    print(total)
    end = time()
    print('Execution time: %.3fs' %(end -start))

def task_handler(curr_list,request_queue):
    total = 0
    for num in curr_list:
        total += num
    request_queue.put(total)

def use_process():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    #启动8个进程将数据切片后进行计算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000],result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    #开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    #合并结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time：',(end - start),'s',sep='')

if __name__ == '__main__':
    # no_process()
    use_process()