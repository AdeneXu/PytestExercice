"""
正则表达式
Python通过标准库中的re模块支持正则表达式操作
"""
import re

def re_1():
    """
    验证输入用户名和QQ号是否有效并给出对应的提示西悉尼

    要求：用户名必须由字母、数字或下划线构成，且长度在6~20个字符之间
          QQ号是5~12的数字且首位不能为0
    :return:
    """
    username = input('请输入用户名：')
    qq = input('请输入QQ号:')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    if not m1:
        print('请输入有效的用户名!')
    m2 = re.match(r'^[1-9]\d{4,11}$',qq)
    if not m2:
        print('请输入有效的QQ号!')
    if m1 and m2:
        print('您输入的信息是有效的')

def re_2():
    """
    从一段文字中提取出国内手机号码
    :return:
    """
    #创建正则表达式对象，使用前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence = '''
     重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    #查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern,sentence)
    print(mylist)
    print('-----------------------')
    #通过迭代器取出匹配对象并获得匹配内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('---------------')
    #通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence,m.end())

def re_3():
    """
    替换字符串中不良内容
    :return:
    """
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔','*',sentence,flags=re.IGNORECASE)
    print(purified)

def re_4():
    """
    拆分长字符串
    :return:
    """
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。,.]',poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

if __name__ == '__main__':
    # re_1()
    # re_2()
    # re_3()
    re_4()