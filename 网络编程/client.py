
'''
import socket

# 创建一个 socket;
client = socket.socket()
# 向服务端发起连接请求；注意服务端的IP及端口；
client.connect(('172.16.1.245', 80))
# 连接上服务端后，向服务端发送数据；
client.send(b"Hello")
# 客户端等待服务端给它回消息；
data = client.recv(1024)
print(data)

# 关闭自己（客户端）：
client.close()
'''


import socket

cli = socket.socket()

cli.connect(('172.16.1.245', 8000))
while True:
    name = input("请输入您的姓名： ")
    cli.send(name.encode('utf-8'))
    if name == 'exit':
        break
    response = cli.recv(1024)
    print(response.decode('utf-8'))
cli.close()
