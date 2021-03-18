import sys
# 创建类；
class Person(object):
    # 构造函数，初始化类；
    def __init__(self, name, age):
        self._name = name
        self._age = age
    # 属性包含可读、可写、可删除；
    # 访问器 － getter 方法，可读；
    @property
    def name(self):
        return self._name

    # 访问器－ getter 方法；可读；
    @property
    def age(self):
        return self._age

    # 修改器 － setter 方法：可写；
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print("%s 正玩飞行器。" % self._name)
        else:
            print("%s 正在玩斗地主。" % self._name)
# 程序的执行入口；
def main():
    # 据类创建对象；
    person = Person('王五', 12)
    # 调用类的普通方法；
    person.play()
    """
    # 修改类的属性；
    person.age = 22
    # 再次类的普通方法；
    person.play()
    """
    while True:
        # 输入不同的年龄阶段；再看看执行的结果；
        person.age = int(input("Pleast Input your age: "))
        if person.age > 50:
            print("年龄已经很大，不能再玩了。")
            sys.exit(8)
        else:
            person.play()

if __name__ == '__main__':
    main()
