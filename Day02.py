import math
"""
将华氏温度转换为摄氏温度
转换公式为：$C=(F - 32) \div 1.8$。
"""

def temperatureConvertion():
    f =float(input('请输入华氏温度:'))
    c = (f - 32)/1.8
    print('%.1f华氏度 = %.1f摄氏度' % (f,c))

def calCircle():
    r = float(input('请插入圆的半径：'))
    perimeter = math.pi * r * 2
    area = math.pi * r * r
    print('周长 = %.2f' % perimeter)
    print('面积 = %.2f' % area)

def isLeapyear():
    year = int(input('请输入年份：'))
    is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    print(is_leap)

if __name__ == '__main__':
    # temperatureConvertion()
    # calCircle()
    isLeapyear()

