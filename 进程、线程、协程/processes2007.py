from multiprocessing import Process
from multiprocessing import Pool
import time
import os

def run(name):
    print("子进程%d启动: %s" % (name, os.getpid()))
    time.sleep(10)
    print("子进程%d结束: %s" % (name, os.getpid()))

if __name__ == "__main__":
    """
    # 通过进程池 Pool 创建多个进程，Pool 默认创建的进程数为CPU的核心数；
    """
    print("父进程启动")
    pp = Pool(2)
    # 创建的进程数需要大于 Pool 进程池中的进程数；
    for i in range(4):
        # 创建进程，放入进程池统一管理；
        pp.apply_async(run, args=(i,))

    # 在调用join之前必须先调用close，调用close之后就不能再往进程池中添加新的进程了；
    pp.close()
    # 进程池对象调用 join ，会等待进程池中所有子进程结束完毕再去执行父进程；
    pp.join()
    print("父进程结束")
