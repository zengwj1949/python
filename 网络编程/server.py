

'''
"""
网络编程的简单示例；
"""
# 导入网络通信模块；
import socket

# 创建 socket 对象；
server = socket.socket()
# 绑定IP和端口；
server.bind(("172.16.1.245", 80))
# 等待的队列；
server.listen(5)
# 被动等待客户端来连接（阻塞）；返回值是一个（conn, addresss）的值对，这里的conn是一个socket对象，可以用来改送或接收数据.而address是连接另一端绑定的地址；
conn, address = server.accept()
# 从 conn 接收数据，注意是byte类型，批一次最多接收数据的大小；
data = conn.recv(1024)
print(data)
# 服务端通过对象 conn 给客户端回复了一个消息；
conn.send(b'stop')
# 关闭连接；与客户端断开连接；
conn.close()
# 关闭服务端的服务；
server.close()
'''


"""
编写一个简单的服务器程序来接受客户端的请求；
"""
import socket
# 创建一个 socket;
s = socket.socket()
# 给 socket 绑定IP和端口；
s.bind(('172.16.1.245', 8000))
# 等待连接的最大数量；
s.listen(5)
print("Waiting for connection......")

while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if data == b'exit':
            print("关闭连接")
            break
            #conn.close()
        response = data + b'SB'
        conn.send(response)

    conn.close()
