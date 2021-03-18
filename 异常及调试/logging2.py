import logging,traceback

'''
把日志写到不同文件中；
'''
# 1 定义 web 日志文件及输出格式；
weblog = r'./web.txt'
file_handler = logging.FileHandler(weblog, 'a', encoding = 'utf-8')
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s"))

# 2 创建一个logger；
web_log = logging.Logger('web', level=logging.INFO)
web_log.addHandler(file_handler)

#web_log.error('11111')

# 3 应用到代码；
def main():
    try:
        a = a + 1
        print(a)
    except Exception as e:
        msg = traceback.format_exc()
        web_log.error(msg)

main()
print("End web.")


# 1 定义 app 日志文件及输出格式；
applog = r'./app.txt'
file_handler2 = logging.FileHandler(applog, 'a', encoding = 'utf-8')
file_handler2.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s"))

# 2 创建一个logger；
app_log = logging.Logger('app', level=logging.INFO)
app_log.addHandler(file_handler2)

#web_log.error('11111')

# 3 应用到代码；
def app():
    try:
        a = a + 1
        print(a)
    except Exception as e:
        msg = traceback.format_exc()
        app_log.error(msg)

app()
print("End app.")
