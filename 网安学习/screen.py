# -*- coding=utf-8 -*-
import ipaddress
from scapy.all import *
from scapy.layers.inet import IP, TCP,UDP,ICMP
import warnings


def host_scan(net):
    net = ipaddress.ip_network(net)
    ip_list = []
    for ip in net.hosts():  # 迭代可用的主机地址
        id_no = random.randint(1, 65535)
        pkt = IP(dst=str(ip))/ ICMP(id=id_no)
        result_raw = sr1(pkt, timeout=0.2, verbose=False)
        if result_raw == None:
            print(str(ip) + "不在线")
        elif result_raw != None:
            ip_list.append(str(ip))  # ip默认类型未IPv4adress，需转换为str类型
            print(str(ip) + "在线")
    print("在线主机如下：\n%s" % ip_list)


def syn_scan_final(dstip, lport, hport):
    # 发送SYN包，并且等待回应##############目的端口可以为元组(lport,hport)##flag为SYN（S）#########
    port_list = []
    for p in range(int(lport), int(hport) + 1):
        source_port = random.randint(1024, 65535)
        pkt = IP(dst=dstip) / TCP(sport=source_port, dport=p, flags="S")
        print(pkt.summary())
        result_raw = sr1(pkt, verbose=False, timeout=2)  # 发送三层包，等待接收一个回应
        if result_raw != None:
            if result_raw.getlayer(TCP).fields["flags"] == 18:
                port_list.append(str(p))
                print("TCP " + str(p) + "端口可达,open")
        elif result_raw == None:
            print("TCP " + str(p) + "端口无响应")
    print("%s 开放的TCP端口为:%s\n" % (dstip, port_list))


def udp_port_scan(dstip, lport, hport):
    port_list = []
    for p in range(int(lport), int(hport) + 1):
        source_port = random.randint(1024, 65535)
        pkt = IP(dst=dstip) / UDP(sport=source_port,dport=p)
        print(pkt.summary())
        result_raw = sr1(pkt, verbose=False, timeout=3)  # 发送三层包，等待接收一个回应
        if result_raw != None:
            print("UDP " + str(p) + "端口无响应")
        elif result_raw == None:
            port_list.append(str(p))
            print("UDP " + str(p) + "open")
    print("%s 开放的UDP端口为:%s\n" % (dstip, port_list))


if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    while True:
        print('''
        -----选择功能-----
        1.主机扫描
        2.TCP端口扫描
        3.UDP端口扫描
        q.退出
        ''')
        choice = input("选择功能>>>")
        try:
            if choice == '1':
                net = input("Net/mask>>>")
                host_scan(net)
            elif choice == '2':
                host = input('请你输入扫描主机的IP地址: ')
                port_low = input('请你输入扫描端口的最低端口号: ')
                port_high = input('请你输入扫描端口的最高端口号: ')
                syn_scan_final(host, port_low, port_high)
            elif choice == '3':
                host = input('请你输入扫描主机的IP地址: ')
                port_low = input('请你输入扫描端口的最低端口号: ')
                port_high = input('请你输入扫描端口的最高端口号: ')
                udp_port_scan(host, port_low, port_high)
            elif choice == 'q':
                break
            else:
                print("输入错误！！")
        except Exception:
            pass
