import threading

balance = 0

lock = threading.Lock()

def run_thead(n):
    for i in range(5):
        # 先要获取锁；
        lock.acquire()
        try:
            # 可以放心修改数据了；
            change_it(n)
        finally:
            # 修改完之后需要释放锁；
            lock.release()

if __name__ == "__main__":
    run_thead('a')
