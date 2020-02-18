"""
多进程和线程池的使用
多线程因为GIL的粗壮乃不能够发挥CPU的多核特性，对于计算密集型任务应该考虑用多进程

多线程和多进程的比较：
-使用多线程的情况：
1、程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程---维护共享的代价相对较小
2、程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多内存

-使用多进程情况：
1、程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）
2、程序的输入可以并行的分块，并且可以将运算结果合并
3、程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字）
"""

import concurrent.futures
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5

def is_prime(n):
    """判断素数"""
    if n %2 ==0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3,sqrt_n+1,2):
        if n% i ==0:
            return False
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number,prime in zip(PRIMES,executor.map(is_prime,PRIMES)):
            print('%d is prime:%s' %(number,prime))


if __name__ == '__main__':
    main()