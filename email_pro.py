
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
发送带有附件的电子邮件；
"""
def eMail():
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
    zipFile = r'E:\newexcel2.zip'
    zipApart = MIMEApplication(open(zipFile, 'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment', filename = zipFile)
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
    eMail()
