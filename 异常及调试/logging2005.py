import logging
import traceback

"""
1、Logging 模块中的几个概念；
1）Logger：日志记录器，是应用程序中能直接调用的接口；
2）Handler：日志处理器，表示将日志保存到什么地方以及保存多久；
3）Formatter：格式化，配置日志的输出格式；
在典型的使用场景中， 一个日志记录器使用一个日志处理器，一个日志处理器使用一个日志格式化；
对于比较简单的脚本，可以直接使用 basicConfig 在代码中配置日志；
对于比较复杂的项目，可以将日志的配置保存到一个配置文件中，然后在代码中使用 fileConfig 函数中读取配置文件；

# format 格式，如 %(levelno)s 表示打印日志级别的数值，%(asctime)s 表示打印日志的时间；
"""

'''
1、把INFO日志打印到命令行；
'''
'''
# 初始化日志对象；
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        a = a + 1
        b = 100
        print(a, b)
    except Exception as e:
        logging.error(str(e))
'''

'''
2、打印日志到单个文件；
'''
'''
# 初始化日志对象；
logger = logging.basicConfig(filename = r'd:\log1.log',
                            format = '%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
                            datefmt = '%Y-%m-%d %H:%M:%S',
                            level = 10)

def main():
    try:
        a = a + 1
        b = 100
        print(b)
    except Exception as e:
        # 把错误定位到具体的位置；
        msg = traceback.format_exc()
        logging.error(msg)
'''

'''
3、不同日志写入到不再日志文件；
'''
# 3.1 定义 WEB 日志文件；
# 3.1.1 定义 web 日志文件及初始化日志对象；
weblog = r'd:\web.txt'
file_handler = logging.FileHandler(weblog, 'a', encoding = 'utf-8')
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s"))

# 3.1.2 创建一个logger 对象；
web_log = logging.Logger('web', level=logging.INFO)
web_log.addHandler(file_handler)

# 3.1.3 应用到代码；
def main():
    try:
        a = a + 1
        print(a)
    except Exception as e:
        msg = traceback.format_exc()
        web_log.error(msg)

# 3.2 定义 APP 日志文件；
# 3.2.1 定义APP日志文件和初始化日志对象；
applog = r'D:\app.txt'
file_handler2 = logging.FileHandler(applog, 'a', encoding = 'utf-8')
file_handler2.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s"))

# 3.2.2 创建一个logger 对象；
app_log = logging.Logger('app', level=logging.INFO)
app_log.addHandler(file_handler2)

# 3.3.3 应用到代码；
def app():
    try:
        a = a + 1
        print(a)
    except Exception as e:
        msg = traceback.format_exc()
        app_log.error(msg)

if __name__ == "__main__":
    main()
    app()
    
