"""
常用算法
"""

def exhaustion():
    """
    穷举法（暴力破解法）：对所有的可能性进行验证，直到找到正确答案
    五人分鱼
    # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
    # 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
    # B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
    # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
    :return:
    """
    fish = 6
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 5

class Thing(object):
    """物品"""

    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """ 价格重量比"""
        return self.price/self.weight

def input_thing():
    """输入物品信息"""
    name_str, price_str,weight_str = input().split()
    return name_str,int(price_str),int(weight_str)

def voracity():
    """主函数"""
    max_weight,num_of_things = map(int,input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x:x.value,reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + total_price <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += total_weight
            total_price += total_price
    print(f'总价值:{total_price}美元')

if __name__ == '__main__':
    # exhaustion()
    voracity()