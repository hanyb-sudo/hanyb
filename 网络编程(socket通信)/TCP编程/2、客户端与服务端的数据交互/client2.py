import socket

# 创建socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立一个连接
sk.connect(("192.168.31.144", 8080))

while True:
    # 发送数据
    data = input("client>>")
    sk.send(data.encode("utf-8"))
    if data == "EOF":
        break

    if data == "quit":
        sk.close()
        print("程序结束\n")
        exit()

    # 接收数据
    msg = sk.recv(1024)
    print("server:%s" % (msg.decode("utf-8")))
    if msg == b"EOF":
        break

    if msg == b"quit":
        sk.close()
        print("程序结束\n")
        exit()


