import pymysql
import xlwt, sys, time, zipfile, os
# 发送邮件模块；
import smtplib
# 构建发送字符串的邮件；
from email.mime.text import MIMEText
# 处理多种形态的邮件主体，如附件，是需要 MIMEMultipart 类；
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
# 构建图片相关的邮件，需要 MIMEImage 类；
from email.mime.image import MIMEImage


"""
数据库连接及基本操作；
"""
'''
def export_Excel(table_name):
    # 连接数据库；
    try:
        conn = pymysql.Connect(
        host = '61.144.244.107',
        port = 3366,
        user = 'erp',
        passwd = 'EmtErp123!#@',
        db = 'qianhai',
        charset = 'utf8'
        )
        print("连接数据库成功。")
    except:
        print("连接数据库失败。")
        sys.exit(9)

    # 创建游标，用于执行SQL语句；
    cur = conn.cursor()
    # 执行SQL语句；
    sql = 'SELECT ID_,REV_,NAME_,BYTES_ FROM %s' % table_name
    cur.execute(sql)

    # 获取返回的信息；
    data = cur.fetchone()
    print(data)

    # 断开连接；
    cur.close()
    conn.close()
'''

"""
此脚本用于从MySQL数据库读取数据然后保存到 Excel 文档，然后经过压缩并发送到指定邮箱；
步骤如下：
1、安装 pymysql 模块、xlwt 模块；
2、编写脚本；
3、压缩文件；
4、发送包含附件的 Email;
"""
# 2、编写脚本；
# 需要进行压缩的Excel文件；
c_time = time.strftime('%y%m%d_%H%M%S')
file = r'E:\erp%s.xls' % c_time
# 经过压缩后的Excel文件；
file_zip = r'E:\erp%s.zip' % c_time

def export_Excel(table_name):
    # 连接数据库；
    try:
        conn = pymysql.Connect(
        host = '61.144.244.107',
        port = 3366,
        user = 'erp',
        passwd = 'EmtErp123!#@',
        db = 'qianhai',
        charset = 'utf8'
        )
        print("连接数据库成功。")
    except:
        print("连接数据库失败。")
        sys.exit(9)

    # 创建游标，用于执行SQL语句；
    cur = conn.cursor()
    # 执行SQL语句；
    sql = 'SELECT ID_, REV_, NAME_, BYTES_ FROM %s' % table_name
    cur.execute(sql)

    # 获取所有字段名称；
    fields = [field[0] for field in cur.description]
    print(fields)

    # 获取返回的数据；
    all_data = cur.fetchall()
    #print(all_data)

    # 写入Excel；
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet1')
    # 写上字段信息；
    #for field in range(0, len(fields)):
    #    sheet.write(0, field, fields[field][0])
    for col,field in enumerate(fields):
        sheet.write(0,col,field)

    # 获取并写入数据段信息
    row = 1
    col = 0
    for row in range(1,len(all_data) + 1):
        for cl in range(0, len(fields)):
            sheet.write(row, cl, u'%s' % all_data[row-1][cl])

    book.save(file)
    print("SQL out_to Excel is succfully.")
    # 断开连接；
    cur.close()
    conn.close()

# 3、压缩文件；
def zip_file(filename):
    filezip = zipfile.ZipFile(file_zip, mode = 'w')

    os.chdir('E:\\')
    print(os.getcwd())
    filezip.write(filename, compress_type = zipfile.ZIP_DEFLATED)
    print("Zipfile is succfully.")

# 4、发送邮件到指定邮箱；
"""
发送带有附件的电子邮件；
"""
def eMail(zipName):
    # 第三方SMTP发送邮件设置；
    smtpServer = "smtp.sina.com"
    smtpUser = "zengwj1949@sina.com"
    smtpPasswd = "1949101Xl"

    # 邮件接收方地址；
    toaddrs = ['2962372861@qq.com', 'zengwj1949@sina.com']

    # 创建一个带附件的对象；
    m = MIMEMultipart()
    # 发送方信息，如发件人;通常使用三个引号来设置邮件信息，标准邮件需要三个头部信息： From(发件人), To(接收人), 和 Subject(邮件主题);
    sender = smtpUser
    m["From"] = sender
    # 设置邮件主题；
    m["Subject"] = "市场部数据"

    # 设置邮件信息；
    # =============== 文字部分 ===============
    # 设置发送邮件内容；
    msg = MIMEText('''刘总：
    附件请接收。
    ''')
    m.attach(msg)

    # =============== 附件部分 ===============
    zipApart = MIMEApplication(open(file_zip, 'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment', filename = file_zip)
    m.attach(zipApart)

    try:
        # 登陆邮件服务器，默认端口为25；
        mailServer = smtplib.SMTP(smtpServer, 25)
        mailServer.login(smtpUser, smtpPasswd)
        # 发送邮件;
        mailServer.sendmail(sender, toaddrs, m.as_string())
        mailServer.quit()
        print("Mail is Success.")
    except Exception as e:
        print("Error: ", e)

if __name__ == '__main__':
    export_Excel('act_ge_bytearray')
    zip_file(file)
    eMail(file_zip)
