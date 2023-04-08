import function


def des(miyao_list, input_list, tp):
    # 获得初始密钥
    start_k = function.start_k(miyao_list)
    c0 = start_k[0:28]
    d0 = start_k[28:56]
    # 获得初始加密内容
    ip = function.start_ip(input_list)
    l0 = ip[0:32]
    r0 = ip[32:64]
    # 获得全部密钥
    all_k = function.all_k(c0, d0)
    for i in range(0, 16):
        l1 = r0
        k = []
        if (tp == 1):
            k = all_k[i]
        if (tp == 2):
            k = all_k[15 - i]
        # 通过E表和密钥K进行异或
        s_start = function.eandk(r0, k)
        # 通过S表
        p_start = function.gointos(s_start)
        r1 = function.pandl1(p_start, l0)
        r0 = r1
        l0 = l1
    temp = r0
    r0 = l0
    l0 = temp
    miwen = l0 + r0
    result = function.ip_1(miwen)
    return result
