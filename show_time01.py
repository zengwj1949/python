
# 此脚本用于计算函数执行的时间；

# 导入时间模块；
import time

# 计算执行时间的函数1；
def foo():
    print('foo......')
    time.sleep(2)

# 计算执行时间的函数2；
def bar():
    print('bar......')
    time.sleep(2)

# 调用函数：
'''foo()'''

# 在不改变原来函数的基础上，新增加一个功能函数用于计算原函数的执行时间；
def show_time(f):
    start = time.time()
    f()
    end = time.time()
    print('spend %s' %(end - start))

# 调用功能函数，把需要计算执行时间的函数传递为功能函数的实参；
show_time(foo)
show_time(bar)
