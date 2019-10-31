
# 导入邮件相关模块；
import smtplib
from email.mime.text import MIMEText

# 第三方SMTP发送邮件设置；
smtpServer = "smtp.sina.com"
sender = "zengwj1949@sina.com"
passwd = "1949101Xl"

"""
发送相关信息
"""
# 设置发送内容，并把发送内容转换成邮件文本；
message = "zwj is a chinese."
msg = MIMEText(message)
# 设置发送标题；
msg["Subject"] = "来自帅哥的问候。"
# 发送方相关信息，如发件人、SMTP服务器、端口、发件人登陆的用户及密码；
msg["From"] = sender

try:
    mailServer = smtplib.SMTP(smtpServer, 25)
    mailServer.login(sender, passwd)

    # 接收人邮件设置；
    receivers = ["2962372861@qq.com", "zengwj1949@sina.com"]

    # 发送邮件，包含邮件发送方、邮件接收方、将MIMEText发送邮件的内容变成字符串等参数；
    mailServer.sendmail(sender, receivers, msg.as_string())
    mailServer.quit()
    print("Email is Success.")
except Exception as e:
    print("Error: ", e)
