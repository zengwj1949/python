

from multiprocessing import Process, Queue
import os,time

#子进程代码；
def write(q):
    print("启动了写子进程%d" % (os.getpid()))
    for chr in ['A', 'B', 'C', 'D']:
        q.put(chr)
        time.sleep(2)
    print("结束了写子进程%d" % (os.getpid()))

#子进程代码；
def read(q):
    print("启动了读子进程%d" % (os.getpid()))
    while True:
        value = q.get(True)
        print("value = " + value)
    print("结束了读子进程%d" % (os.getpid()))


if __name__ == "__main__":
    #父进程创建队列，并传递给子进程；
    q = Queue()
    #创建子进程；
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    #启动子进程；
    pw.start()
    pr.start()

    pw.join()
    pr.terminate()
