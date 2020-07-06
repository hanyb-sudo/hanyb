'''

客户端：创建TCP连接时，主动发起连接的叫做客户端
服务端：接收客户端的连接
'''

import socket,ssl

# 1、创建socket
#参数1：指定协议 AF_INET(ipv4) 或 AF_INET6(ipv6)
#参数2：SOCK_STREAM 指定使用面向流的TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ssl加密
sk = ssl.wrap_socket(socket.socket())

# 2、建立连接
#参数：是一个元组，第一个参数为要连接的服务器的IP地址，第二个参数为端口
sk.connect(("www.sina.com.cn", 443))


sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')


#等待接收数据
data = []

while True:
    #每次接收1KB的数据
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break

dataStr = (b''.join(data)).decode("utf-8")
#断开连接
sk.close()
# print(dataStr)
headers,html = dataStr.split("\r\n\r\n", 1)
print(headers)