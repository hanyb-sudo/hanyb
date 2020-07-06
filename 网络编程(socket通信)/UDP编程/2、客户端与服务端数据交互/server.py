import socket
import threading
# ip = socket.gethostbyname(socket.gethostname())

#创建socket对象
#SOCK_DGRAM    udp模式
udpServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udpServer.bind(("192.168.31.144", 8001))  #绑定服务器的ip和端口
print("udp服务器启动成功！")

local = threading.local()


def func(data, addr):
    local.data = data
    local.addr = addr
    #接收数据
    print("\n%s:%s"%(local.addr[0], local.data.decode("utf-8")))

    #发送数据
    msg = input("\n回复 %s:"%local.addr[0])
    udpServer.sendto(msg.encode("utf-8"), local.addr)


while True:
    #只接收数据
    # data = udpServer.recv(1024)
    # print(data.decode("utf-8"))# decode()解码收到的字节
    #接收发送方的数据和地址
    data, addr = udpServer.recvfrom(1024)  #一次接收1024字节
    threading.Thread(target=func, args=(data, addr)).start()
    # print("%s:%s"%(addr[0], data.decode("utf-8")))

