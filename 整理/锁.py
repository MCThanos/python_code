import threading
import time

# 信号量（semaphore）
'''
同进程的一样，semaphore管理一个内置的计数器，每当调用acquire()时内置内容-1，每当调用release()时内置函数+1。计数器不能为0，
当计数器为0时acquire()将阻塞线程，直到其他线程调用release()。
'''
mysf = threading.Semaphore(5)  # 创建信号量对象,(5表示这个锁同时支持的个数)

def func():
    if mysf.acquire():  # 因为使用了信号量，下面的输出就会5个5个的同时输出
        print(threading.currentThread().getName() + ' get semaphore')
        time.sleep(1)
        mysf.release()

for i in range(20):
    t = threading.Thread(target=func)
    t.start()

# # 互斥锁
# '''
# 互斥就是互相排斥的意思,在多个进程或线程对同一个资源请求的时候,如果每个进程或线程请求的时候都加锁,别的进程或线程就没法访问这里的资源,
# 就会一直等待.直到占用该资源的那个进程或线程释放了该锁.所以互斥锁又叫排他锁,又叫同步锁.
# '''
# R = threading.Lock()
#
# def sub():
#     global num
#     R.acquire()  # 加锁，保证同一时刻只有一个线程可以修改数据
#     num -= 1
#     R.release()  # 修改完成就可以解锁
#     time.sleep(1)
#
# num = 100  # 定义一个全局变量
# l = []
# for i in range(100):
#     t = threading.Thread(target=sub)  # 每次循环开启一个线程
#     t.start()  # 开启线程
#     l.append(t)  # 将线程加入列表l
# for i in l:
#     i.join()  # 这里加上join保证所有的线程结束后才运行下面的代码
# print(num)
# # 重入锁(RLock)
# '''
# 可重入锁是用来解决死锁的.其实就是一个锁对象可以被一个线程重复多次使用,而一般的锁的时候,我们在同一个进程或者线程如果要锁不同的地方,
# 需要使用多个锁对象.可重入锁的原理就是,它在内部维护一个计数器,初始值是0.当遇到这个锁对象acquire()的时候计数就加1,当遇到release()的时候,
# 计数就减一.它解决死锁的原理就是,当有另外线程要操作相同的资源的时候,会先去检查这个计数,只有当这个计数为0的时候,
# 才会让其获取这段资源的使用权.否则就会等待.
# '''
#
# A = threading.RLock()  # 这里设置锁为递归锁
#
# class obj(threading.Thread):
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         self.a()
#         self.b()
#
#     def a(self):  # 递归锁，就是将多个锁的钥匙放到一起，要拿就全拿，要么一个都拿不到
#         # 以实现锁
#         A.acquire()
#         print('123')
#         print(456)
#         time.sleep(1)
#         print('qweqwe')
#         A.release()
#
#     def b(self):
#         A.acquire()
#         print('asdfaaa')
#         print('(⊙o⊙)哦(⊙v⊙)嗯')
#         A.release()
#
# for i in range(2):
#     t = obj()
#     t.start()


