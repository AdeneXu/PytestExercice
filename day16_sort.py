"""
排序算法

时间复杂度递增顺序 O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n)
"""
def select_sort(origin_items,comp=lambda x,y:x<y):
    """
     简单选择排序（复杂度：）--不稳定排序
     基本思想：从要排序的一组数中，选出最小（或最大）的一个数与第一个位置交换。
     时间复杂度：平方时间复杂度 O(n ** 2)
     """
    items = origin_items[:]
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index = j
        items[i],items[min_index] = items[min_index],items[i]
    return items

def bubble_sort(origin_items,comp=lambda x,y:x>y):
    """
    高质量冒泡排序
    时间复杂度：平方时间复杂度 O(n ** 2)
    基本原理：依次比较队列中两个相邻的元素，比较到最后一个元素，将最大值放在最右边。一趟确定一个值。
    :param origin_items:
    :param comp:
    :return:
    """
    items = origin_items[:]
    for i in range(len(items) -1):
        swapped = False
        for j in range(i,len(items) - 1 - i):
            if comp(items[j],items[j+1]):
                items[j],items[j+1] = items[j+1],items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) -2 -i,i,-1):
                if comp(items[j-1],items[j]):
                    items[j],items[j-1] = items[j-1],items[j]
                    swapped = True
        if not swapped:
            break
    return items


def merge(items1, items2, comp):
    """合并（将两个有序的列表合成一个有序的列表）"""
    items = []
    index1,index2 = 0,0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1],items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

def merge_sort(items,comp=lambda x,y:x <= y):
    """
    归并排序（分治法）  时间复杂度：O(n*log_2 n) 对数线性时间复杂度
    思想：分组
    :param items:
    :param comp:
    :return:
    """
    if len(items) < 2:
        return items[:]
    mid = len(items) //2
    left = merge_sort(items[:mid],comp)
    right = merge_sort(items[mid:],comp)
    return merge(left,right,comp)

def seq_search(items,key):
    """顺序查找
    时间复杂度：O(n) 线性时间复杂度
    """
    for index,item in enumerate(items):
        if item == key:
            return index
    return -1

def bin_search(items,key):
    """
    折半查找(二分查找)
    时间复杂度:对数时间复杂度  O(log_2 n)
    前提要求：折半查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列
    """
    start,end = 0, len(items) - 1
    while start <= end:
        mid = (start + end ) //2
        if key > items[mid]:
            start = mid +1
        elif key < items[mid]:
            end = mid -1
        else:
            return mid
    return -1

if __name__ == '__main__':
    num_list_int = [25,88,96,56,34,21,15,8]
    num_list_int_search = [12,25,36,52,69,79,85,95]
    # number_list = str(input('请输入需要排序的数字（以空格分隔）：')).split(' ')
    # for i in range(len(number_list)):
    #     num_list_int.append(int(number_list[i]))
    print('简单算法排序：',select_sort(num_list_int))
    print('冒泡算法排序：',bubble_sort(num_list_int))
    print('归并算法排序：',merge_sort(num_list_int))
    print('顺序查找：',seq_search(num_list_int_search,69))
    print('折半查找：',bin_search(num_list_int_search,69))