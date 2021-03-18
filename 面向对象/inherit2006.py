# 创建类；
class Person(object):
    """人"""
    # 类的初始化；
    def __init__(self, name, age):
        self._name = name
        self._age = age
    # 属性，可读；
    @property
    def name(self):
        return self._name
    # 属性，可读；
    @property
    def age(self):
        self._age = age
    # 属性，可写；
    @age.setter
    def age(self, age):
        self._age = age
    # 类的普通方法；
    def play(self):
        print("%s 正在愉快的玩耍。" % self._name)
    # 类的普通方法；
    def watch_av(self):
        if self._age >= 18:
            print("%s 正在观看爱情动作片。" % self._name)
        else:
            print("%s 只能观看《熊出没》。" % self._name)
# 创建类；
class Student(Person):
    """"学生"""
    # 类的初始化；
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    #定义属性，可读；
    @property
    def grade(self):
        return self._grade
    # 定义属性，可写；
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    # 类的普通方法；
    def study(self, course):
        print("%s 的 %s 正在学习 %s。" % (self._grade, self._name, course))
# 创建类；
class Teacher(Person):
    """老师"""
    # 类的初始化；
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title
    # 定义属性，可读；
    @property
    def title(self):
        return self._title
    # 定义属性，可写；
    @title.setter
    def title(self, title):
        self._title = title
    # 类的普通方法；
    def teach(self, course):
        print("%s%s 正在讲 %s." % (self._name, self._title, course))
# 定义函数（执行程序的入口）；
def main():
    # 根据类创建对象；
    stu = Student('曾卫军', 33, '大学')
    # 调用类的方法；
    stu.study('数学')
    # 调用父类的方法；
    stu.watch_av()

    # 根据类创建对象；
    t = Teacher('小王', 31, '专家')
    # 调用类的普通方法；
    t.teach('python程序设计')
    # 调用父类的方法；
    t.watch_av()

if __name__ == "__main__":
    main()
