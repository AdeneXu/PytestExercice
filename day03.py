num1 = 52
num2 = 130
num = 0
# for i in range(25):
#     if num1 != num2:
#         num = num1 + num2 + num
#         num1,num2 = num1+1,num2-1
#         print("i = {0},num1 = {1},num2 = {2},num={3}".format(i,num1,num2,num))
#     else:
#         num = num + num1
#         print("i = {0},num1 = {1},num2 = {2}".format(i, num1, num2))
#         break
#
# print(num)
# print('{0:0.2f}'.format(num/50))

for i in range(1,200):
    num = (abs(num1-200)/200) * 100
    num1 +=1
    # print('i = {0},num1 = {1},num = {2:.2f}%'.format(i, num1, num))
    if num >= 70 and num < 100:
        print('i = {0},num1 = {1},num = {2:.2f}%'.format(i,num1,num))