'''

TCP 是建立可靠的连接，并且双方都可以以流的形式发送数据。相对于TCP，UDP则是面对无连接的协议

使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发送数据包。但是能不能到就不知道了

虽然传输数据不可靠，但他的优点是和TCP相比，速度快，对于要求不高的数据可以使用UDP
'''
import socket

#创建一个udp
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#元组中第一个参数为ip，第二个为端口号
udp.connect(("", ))

udp.send("message....".encode("utf-8"))

udp.sendto()
udp.close()