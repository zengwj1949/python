
class Rect(object):
    def __init__(self, width=0, height=0):
        """初始化方法"""
        self.__width = width
        self.__height = height

    # 普通方法：计算周长；
    def perimeter(self):
        """计算周长"""
        return (self.__width + self.__height) * 2

    # 普通方法：计算面积；
    def area(self):
        """计算面积"""
        return self.__width * self.__height

    # 类的特殊成员；
    def __str__(self):
        """矩形对象的字符串表达式"""
        return '矩形[%f, %f]' % (self.__width, self.__height)

    # 类的特殊成员；
    def __del__(self):
        """析构器"""
        print("销毁矩形对象。")

if __name__ == "__main__":
    # 创建对象 1；
    rect1 = Rect()
    print(rect1)
    # 计算周长；
    print(rect1.perimeter())
    # 计算面积；
    print(rect1.area())
    # 创建对象 2；
    rect2 = Rect(3, 4)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())
