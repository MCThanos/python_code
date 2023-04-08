'''
语法：
from  multiprocessing import Pipe
#创建管道
fd1,fd2 = Pipe(duplex = True)
参数：默认表示双向管道,如果为False表示单向管道(一个进程只负责写，一个进程只负责读，否则一个进程既有读又有写，可能出现堵塞)
返回值（其实是文件描述符）：表示管道两端的读写对象，如果是双向管道均可读写，如果是单向管道fd1只读  fd2只写

#从管道获取内容,返回值：获取到的数据（读）
fd.recv()


#向管道写入内容,参数： 要写入的数据（写）
fd.send(data)
'''

from multiprocessing import Process, Pipe


def app1(fd1):
    print('启动app1,app1显示可以使用app2登录')
    print('使用app2登录，向app2发请求')
    # 管道通信写操作：send()
    fd1.send('app1需要：用户名，头像')

    # 读fd2send过来的数据
    data = fd1.recv()
    print('oh yeah', data)


def app2(fd2):
    ##管道通信读操作：recv(),接受fd1的sende()
    data = fd2.recv()
    print(data)

    # 写操作
    fd2.send({'name': 'Han', 'img': '有'})


if __name__ == '__main__':
    # 创建管道,默认双向
    fd1, fd2 = Pipe()
    p1 = Process(target=app1, args=(fd1,))
    p2 = Process(target=app2, args=(fd2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
