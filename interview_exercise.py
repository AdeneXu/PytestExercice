import functools,time
"""
0214
实现删除一个list里面重复元素
"""
num_list = [1,1,2,3,5,5,6,8,9,9]
print(list(set(num_list)))

"""
实现一个任意函数能调用，且能打印函数执行的装饰器函数
"""
def decorator(func):
    @functools.wraps(func)
    def time_log(*args,**kwargs):
        time0 = time.time()
        ret = func(*args,**kwargs)
        time1 = time.time()
        print("{0] executed in {1}s".format(func.__name__,time1-time0))
    return time_log