

import logging
import traceback

"""
'''
把 INFO 级别日志打印到命令行
'''
#日志的基本设置；
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        a = a + 1
        b = 100
        print(a, b)
    except Exception as e:
        logging.error(str(e))

main()
print("My English is ok.")
"""


'''
把相关级别日志打印到文件;
logging有 5 个不同层次的日志级别，可以将给定的 logger 配置为这些级别：
DEBUG：详细信息，用于诊断问题。Value=10。
INFO：确认代码运行正常。Value=20。
WARNING：意想不到的事情发生了，或预示着某个问题。但软件仍按预期运行。Value=30。
ERROR：出现更严重的问题，软件无法执行某些功能。Value=40。
CRITICAL：严重错误，程序本身可能无法继续运行。Value=50
'''
logger1 = logging.basicConfig(filename = 'log1.log',
                            format = '%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
                            datefmt = '%Y-%m-%d %H:%M:%S',
                            level = 10)

def main():
    try:
        a = a + 1
        b = 100
        print(b)
        print(b)
    except Exception as e:
        #把错误定位到具体位置；
        msg = traceback.format_exc()
        logging.error(msg)

main()
print("My English is ok.")
