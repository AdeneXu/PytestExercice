"""
面向对象设计原则
1、单一职责原则（SRP）--一个类只做该做的事情（类的设计要高内聚）
2、开闭原则（OCP）--软件实体应该对扩展开放，对修改关闭。增加新功能，不改变原有代码
3、依赖倒转原则（DIP） 面向抽象编程（在弱类型语言中已经被弱化）
4、里氏替换原则（LSP） 任何时候可以用子类对象替换父类对象
5、接口隔离原则（ISP） 接口要小而专，不要大而全（python 中没有接口的概念）
6、合成聚合复用原则（CARP） 优先使用强关联关系而不是继承关系复用代码
7、最少知识原则（迪米特法则，LoD） 不要给没有必然联系的对象发消息
"""

"""
GoF设计模式（待深入）
-创建型：单例、工厂、建造者、原型
-结构性：适配器、门面（外观）、代理
-行为型：迭代器、观察者、状态、策略
"""

"""
迭代器和生成器

迭代器：访问集合元素的一种方式，可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。（只会往前不会后退）
两个基本方法：iter() next()
把一个类作为一个迭代器使用需要在类中实现两个方法：__iter__()和__next__()

生成器：使用了yield的函数
生成器是一个返回迭代器的函数，只能用于迭代操作。（生成器就是一个迭代器）
在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时从当前位置继续运行
"""
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor
#迭代器
# list=[1,2,3,4,5,6,7,8,9]
# it = iter(list)
# # for x in it:
# #     print(x,end=' ')
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

#生成器
# def fibonacci(n):
#     a,b,counter = 0,1,0
#     while True:
#         if(counter > n):
#             return
#         yield a
#         a,b = b,a+b
#         counter += 1
#
# f = fibonacci(10)
# while True:
#     try:
#         print(next(f),end=' ')
#     except StopIteration:
#         sys.exit()

"""
并发编程（
优点：提高程序的执行效率、改善用户体验
缺点：并发的程序不易开发和调试，对其他程序来说并不友好）

python实现并发编程三种方案：多线程、多进程、异步I/O

"""
class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self,money):
        #通过锁保护临界资源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance

class AddMoneyThread(threading.Thread):
    """自定义线程类"""

    def __init__(self,account,money):
        self.account = account
        self.money = money
        #自定义线程的初始化方式中必须调用父类的初始化方式
        super().__init__()

    def run(self):
        #线程启动后要执行的操作
        self.account.deposit(self.money)

def main():
    """主函数"""
    account = Account()
    #创建线程池
    pool = ThreadPoolExecutor(max_workers=10)
    features = []
    for _ in range(100):
        # 创建线程的第一种方式
        # threading.Thread(target=account.deposit,args=(1,)).start()
        # 创建线程的第二种方式
        # AddMoneyThread(account,1).start()
        # 创建线程的第三种方式：调用线程池中的线程来执行特定的任务
        feature = pool.submit(account.deposit,1)
        features.append(feature)

if __name__ == '__main__':
    main()

