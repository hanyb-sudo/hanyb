import socket
import threading

#创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP端口
server.bind(('192.168.31.144', 8080))

#绑定监听
server.listen(5)
print("服务器启动成功！")
'''
print("等待连接....")
clientSocket, clientAddress = server.accept()
print("新连接")
print("IP is %s" % clientAddress[0])
print("port is %d\n" % clientAddress[1])

while True:
    #接收数据
    msg = clientSocket.recv(1024)

    print("服务端接收:", msg.decode("utf-8"))  # 把接收到的数据进行解码
'''

local = threading.local()


def func(clientSocket, clientAddress):
    local.socket = clientSocket
    local.address = clientAddress
    print("新连接")
    print("IP is %s" % local.address[0])
    print("port is %d\n" % local.address[1])
    while True:
        #接收数据
        msg = local.socket.recv(1024)
        print("client %s:%s"%(local.address[0], msg.decode("utf-8")))
        if msg == b"EOF":
            break
        if msg == b"quit":
            local.socket.close()
            server.close()
            print("程序结束\n")
            exit()

        #给客户端发送数据
        sendData = input("server>>")
        local.socket.send(sendData.encode("utf-8"))
        if sendData == "EOF":
            break
        if sendData == "quit":
            local.socket.close()
            server.close()
            print("程序结束\n")
            exit()


#使用线程进行多个连接
print("等待连接....")
while True:
    clientSocket, clientAddress = server.accept()
    threading.Thread(target=func, args=(clientSocket, clientAddress)).start()
