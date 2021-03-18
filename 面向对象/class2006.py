"""
#定义类；
class Test:
    #构造函数，初始化类；
    def __init__(self, foo):
        #定义私有实例变量；
        self.__foo = foo
    #定义私有方法；
    def __bar(self):
        #打印私有实例变量；
        print(self.__foo)
        #打印字符串；
        print('__bar')

def main():
    #创建对象，类的实例化；
    test = Test('Hello')
    #类中所有双下划线开头的名称如__bar都会自动变形成：_类名__bar 的形式：
    #调用类的私有方法；
    test._Test__bar()
    #打印私有实例变量；
    print(test._Test__foo)

if __name__ == "__main__":
    main()
"""

"""
练习 1
修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)

Version: 0.1
Author: zwj
Date: 2018-03-08
"""
116.24.64.138
#导入模块；
import math
#创建类；
class Circle(object):
    #初始化类；
    def __init__(self, radius):
        self._radius = radius

    """
    @property 定义属性，是关键字（装饰器）；
    下面开始定义属性，3个函数的名字要一样！
    1》只有@property表示只读。
    2》同时有@property和@x.setter表示可读可写。
    3》同时有@property和@x.setter和@x.deleter表示可读可写可删除。
    """
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius

if __name__ == '__main__':
    radius = float(input('请输入游泳池的半径: '))
    #类的实例化（创建对象）
    small = Circle(radius)
    big = Circle(radius + 3)

    print('围墙的造价为: ￥%.1f元' % (big.perimeter * 115))
    print('过道的造价为: ￥%.1f元' % ((big.area - small.area) * 65))
    print("==================")
    #调用属性；
    print(small.area)
    print(big.radius)
    print("==================")
