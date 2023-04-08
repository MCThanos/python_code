import table


def loop(move, li):
    if (move == 1):
        temp = li[0]
        for j in range(0, 27):
            li[j] = li[j + 1]
        li[-1] = temp
        return li
    if (move == 2):
        temp1 = li[0]
        temp2 = li[1]
        for j in range(0, 26):
            li[j] = li[j + 2]
        li[-1] = temp2
        li[-2] = temp1
        return li


def start_ip(mingwen_list):
    ip = [0] * 64
    for i in range(0, 64):
        ip[i] = mingwen_list[table.ip[i] - 1]
    return ip


def start_k(miyao_list):
    start_k = [0] * 56
    for i in range(0, 56):
        start_k[i] = miyao_list[table.pc_1[i] - 1]
    return start_k


def all_k(c0, d0):
    all_k = []
    for i in range(0, 16):
        # 得到k0
        move = table.move[i]
        c0 = loop(move, c0)
        d0 = loop(move, d0)
        k0 = c0 + d0
        k = [0] * 48
        for j in range(0, 48):
            # 得到密钥K
            k[j] = int(k0[table.pc_2[j] - 1])
        all_k.append(k)
    return all_k


def eandk(r0, k):
    s_start = []
    for j in range(0, 48):
        # 得到E表
        e = int(r0[table.e[j] - 1])
        # 得到密钥K
        hh = table.pc_2[j]
        k0 = int(k[j])
        # 得到S表
        s_start.append(e ^ k0)
    return s_start


# S表置换
def gointos(s_start):
    p_start = [0] * 32
    for m in range(0, 8):
        s = s_start[m * 6:(m + 1) * 6]
        p = int(str(s[0]) + str(s[-1]), 2)
        q = int(str(s[1]) + str(s[2]) + str(s[3]) + str(s[4]), 2)
        result = table.s[m][p][q]
        result1 = list(bin(result).replace("0b", ""))
        length = len(result1)
        result2 = [0] * (4 - length)
        result3 = result2 + result1
        for i in range(0, 4):
            p_start[m * 4 + i] = result3[i]
    return p_start


def pandl1(p_start, l0):
    p = [0] * 32
    # P置换
    for i in range(0, 32):
        p[i] = p_start[table.p[i] - 1]
    r1 = []
    for j in range(0, 32):
        l = int(l0[j])
        r = int(p[j])
        r1.append(l ^ r)
    return r1


def ip_1(miwen):
    result = [0] * 64
    for i in range(0, 64):
        result[i] = miwen[table.ip_1[i] - 1]
    return result
