
import socket

s = socket.socket()
s.connect(('192.168.1.4', 80))

while True:
    send_str = input("请输入消息：")
    s.send(send_str.encode())
    receive = s.recv(1024)
    if not receive :
        break
    print(f"服务器回复：{receive.decode('utf-8')}")



