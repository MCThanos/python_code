import des, inandout

def desjiemi(miyao_list):
    bs64 = input("请输入bas64加密后的密文")
    result=inandout.jiemiincontent(bs64)
    a = des.des(miyao_list, result, 2)
    inandout.outcontent(a)
