
'''
multiprocessing 是Python中多进程管理包；
Pool 能创建大量的子进程；
'''

from multiprocessing import Pool
import time
import os

# 子进程要执行的代码；
def run(name):
    print("子进程启动%s-%d" % (name, os.getpid()))
    time.sleep(2)
    print("子进程结束%s-%d" % (name, os.getpid()))

if __name__ == "__main__":
    print("父进程启动")

    #创建多个子进程
    #进程池（Pool），Pool进程池默认进程数为CPU核心数，如 pp = Pool(2)；
    #表示可以同时执行的进程数量
    pp = Pool(2)
    for i in range(4):
        #创建进程，放入进程池统一管理；
        pp.apply_async(run, args=(i,))

    #对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了；
    #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    pp.close()
    pp.join()

    print("父进程结束")
