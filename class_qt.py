
'''
创建3个学校，并且3个学校的设施内容都是一样的。
'''

# 父类：学校名称和地址；
class School(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def speech(self):
        pass

obj1 = School("老男孩北京校区", "沙可")
obj2 = School("老男孩上海校区", "浦东新区")
obj3 = School("老男孩深圳校区", "南山区")

# 子类：老师的相关信息；
class Teacher(object):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary
        self.school = None

t1 = Teacher('zwj', 33, 3333)
t2 = Teacher('zangs', 44, 4444)
t3 = Teacher('lisi', 55, 5555)

# 老师和学校相关联；
t1.school = obj1
t2.school = obj2
t3.school = obj3

# 查看t1老师所有校区和地址；
print(t1.school.name)
print(t1.school.address)
print(t1.name)
print(t1.age)
