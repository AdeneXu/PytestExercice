import heapq

def nest_list():
    """
    嵌套的列表
    :return:
    """
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    # scores_1 = [[None] * len(courses)] * len(names)  # error 所有的位于同一地址
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row,name in enumerate(names):
        for col,course in enumerate(courses):
            #以f开头表示在字符串内支持大括号内的python表达式
            scores[row][col] = float(input(f'请输入{name}的{course}的成绩：'))
    print(scores)

def other_gram():
    """
    heapq
    从列表中找出最大的或最小的N个元素
    堆结构(大根堆/小根堆)
    :return:
    """
    list1 = [34,25,12,99,87,63,58,78,88,92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

    print(heapq.nlargest(3,list1))
    print(heapq.nsmallest(3,list1))
    print(heapq.nlargest(2,list2,key=lambda x:x['price']))
    print(heapq.nlargest(2,list2,key=lambda x:x['shares']))

if __name__ == '__main__':
    # nest_list()
    other_gram()