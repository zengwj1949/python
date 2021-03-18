import logging
import logging.config

"""
1、Logging 模块中的几个概念；
1）Logger：日志记录器，是应用程序中能直接调用的接口；在使用接口debug，info，warn，error，critical之前必须创建Logger实例，即创建一个记录器；
2）Handler：日志处理器，表示将日志保存到什么地方以及保存多久；
3）Formatter：格式化，配置日志的输出格式；
在典型的使用场景中， 一个日志记录器使用一个日志处理器，一个日志处理器使用一个日志格式化；
对于比较简单的脚本，可以直接使用 basicConfig 在代码中配置日志；
对于比较复杂的项目，可以将日志的配置保存到一个配置文件中，然后在代码中使用 fileConfig 函数中读取配置文件；

# format 格式，如 %(levelno)s 表示打印日志级别的数值，%(asctime)s 表示打印日志的时间；
"""

logging.config.fileConfig("log2006.cnf")
logger = logging.getLogger('ProxyIP')
logger.info("Hello 智障！")
