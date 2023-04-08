import threading
import time


def fun1():
    for i in range(10):
        print('1')
        time.sleep(1)


def fun2():
    for i in range(10):
        print('2')
        time.sleep(3)


if __name__ == '__main__':
#函数名不能加括号，否则就不能进行多线程
    sing_thread = threading.Thread(target=fun1)
    song_thread = threading.Thread(target=fun2)

    sing_thread.start()
    song_thread.start()
