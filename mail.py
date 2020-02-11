# 发送邮件模块；
import smtplib
# 构建发送字符串的邮件；
from email.mime.text import MIMEText
# 处理多种形态的邮件主体，如附件，是需要 MIMEMultipart 类；
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
# 构建图片相关的邮件，需要 MIMEImage 类；
from email.mime.image import MIMEImage

def eMail():
    # 第三方SMTP发送邮件设置；
    smtpServer = "smtp.sina.com"
    sender = "zengwj1949@sina.com"
    passwd = "1949101Xl"

    # 邮件接收方地址；
    toaddrs = ['2962372861@qq.com', 'zengwj1949@sina.com']

    # 设置邮件信息；
    # =============== 发送字符串邮件 ===============
    # 设置发送邮件内容；
    msg = MIMEText("CPU is Hight.")
    # 设置邮件主题；
    msg["Subject"] = "来自远方"
    # 发送方信息，如发件人;
    msg["From"] = sender

    try:
        # 登陆邮件服务器，默认端口为25；
        mailServer = smtplib.SMTP(smtpServer, 25)
        mailServer.login(sender, passwd)
        # 发送邮件;
        mailServer.sendmail(sender, toaddrs, msg.as_string())
        mailServer.quit()
        print("Mail is Success.")
    except Exception as e:
        print("Error: ", e)

if __name__ == '__main__':
    eMail()
