import time,functools
#高阶函数的用法(filter、map以及他们的替代品)
items1 = list(map(lambda x : x ** 2,filter(lambda x:x % 2,range(1,10))))
items2 = [x **2 for x in range(1,10) if x % 2]
print(items1)
print(items2)

"""

函数可以作为函数的参数
函数可以作为函数的返回值
"""
def hi(name='python'):

    def greet_1():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome function"

    if name == "python":
        return greet_1
    else:
        return welcome

    # return "hi " + name

print(hi())

#函数可以赋值给变量
#当把一堆小括号放在后面，这个函数就会执行。如果不带括号，它就可以被到处传递，并且可以赋值给别人而不去执行它
greet = hi
print("函数可以赋值给变量")
print(greet())

#从函数中返回函数
a = hi()
print("从函数中返回函数")
print(a)
print(a())
print(hi()())

"""
装饰器使用场景：授权、日志、性能测试、事务处理、缓存
"""

"""
深复制/深拷贝/深度克隆  copy.deepcopy
浅复制/浅拷贝/影子克隆  copy.copy/list.copy/L[:]
区别：浅拷贝是拷贝父对象，共用子对象
      深拷贝：父对象和子对象都拷贝

python默认的拷贝方式是浅拷贝
时间角度：浅拷贝花费时间更少
空间角度：浅拷贝花费内存更少
效率角度：浅拷贝只拷贝顶层数据，一般情况比深拷贝效率高
"""
import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

"""
垃圾回收：引用计数、标记-清除、分代收集
"""

"""
魔法属性：
1、__dict__  分为类和实例的__dict__属性   __init__方法就是对__dict__属性的初始化赋值
2、__doc__ 记录了类的说明文档
3、__class__ 指向该实例的类
4、__slots__  限制动态绑定属性和方法的作用；默认不存在。

魔法方法：
1、__new__ 类创建实例调用的第一个方法，返回一个实例（在单例模式中常用）
2、__init__  
3、__del__ 在实例对象引用计数变为0或del关键字调用时触发
4、__repr__ 在print()调用或repr()调用时执行，用于定义对类的信息描述
"""

""" 
mixin 混入  只包含一组特定的函数集合，我们将会将其与其他类进行混合，生成一个适用于实际需要的新类
"""
class Displayer():
    def display(self, message):
        print(message)


class LoggerMixin():
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        super().display(message)
        self.log(message)


class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename='subclasslog.txt')

subclass = MySubClass()
subclass.display("This string will be shown and logged in subclasslog.txt")

class SetOnceMappingMixin:
    """自定义混入类"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """自定义字典"""
    pass


my_dict= SetOnceDict()
try:
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'
except KeyError:
    pass
print(my_dict)

"""
元编程：一种构建函数和类的行为，可以通过修改、包装现有代码或生成代码来操作代码
可以通过修改器或元类实现

元类是类的特殊类型。在普通类定义其自身实例的行为时，元类定义了普通类及其实例的行为
元类可以向普通类添加或删去方法或字段。
python有一个特殊的类，叫类型类，默认情况他是一个元类，所有自定义类型类都必须从类型类继承

self表示一个类的实例对象本身，如果用了staticmethod就可以无视self，将这个方法当成普通函数使用了。
类先调用__new__方法，返回该类的实例对象，这个实例对象就是__init__方法的第一个参数self。即self是__new__的返回值
cls表示这个类本身
"""

def debug_fuction(func):

    def wrapper(*args,**kwargs):
        print("{0} is called with parameter {1}".format(func.__qualname__,args[1:]))
        return func(*args,**kwargs)
    return wrapper

def debug_all_methods(cls):
    """
    vars()函数 返回对象object的属性和属性值的字典对象
    callabe()函数 用于检查一个对象是否可调用  语法：callable(object)
    :param cls:
    :return:
    """
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug_fuction(val))
    return cls

"""
type 可以动态创建类  语法 type(clasname,bases,dict)
class MetaClassDebug(object):
    bar = True
等价于====> MetaClassDebug = type(MetaClassDebug,(),{'bar':True})

metaclass=XXX 设置元类

一个类没有声明自己的元类，默认元类就是type,除了使用元类type,用户也可以通过继承type来自定义元类

自定义元类的主要目的：
1、拦截类的创建
2、读取类的信息，可以做修改
3、返回新的类
"""
#自定义一个元类
class MetaClassDebug(type):

    def __new__(cls, clsname, bases,clsdict):
        obj = super().__new__(cls,clsname,bases,clsdict)
        print("==================",super())
        obj = debug_all_methods(obj)
        return obj


class Calc(metaclass=MetaClassDebug):
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y

#pytho中类的实例化过程，会首先寻找metaclass,通过metaclass创建user类
calc = Calc()
print(calc.add(2,3))
print(calc.sub(2,3))
print(calc.mul(2,3))


