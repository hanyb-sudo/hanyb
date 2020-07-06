import socket


# ip = socket.gethostbyname(socket.gethostname())
# print(ip)

#创建一个udp
udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#元组中第一个参数为ip，第二个为端口号
udpClient.connect(("192.168.31.144",8001))

while True:
    #发送数据
    data = input("%s:"%"192.168.31.144")
    udpClient.send(data.encode("utf-8"))

    msg = udpClient.recv(1024)
    print("server:",msg.decode("utf-8"))
