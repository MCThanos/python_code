import inandout, desjiami, desjiemi


def jiami():
    print("请输入明文：")
    mingwen_list = inandout.incontent()
    print("请输入密钥：")
    miyao_list = inandout.incontent()
    desjiami.des_jiami(miyao_list, mingwen_list)


def jiemi():
    print("请输入密钥：")
    miyao_list = inandout.incontent()
    desjiemi.desjiemi(miyao_list)


if __name__ == '__main__':
    while True:
        print("=" * 30)
        print(" " * 10 + "1.加密")
        print(" " * 10 + "2.解密")
        print(" " * 10 + "3.退出")
        print("=" * 30)
        a = input("请输入您想使用的功能的序号")
        if int(a) == 1:
            print("明文和密钥要求不超过8位,超过8位按8位算,小于8位用0补齐")
            jiami()
        elif int(a) == 2:
            jiemi()
        elif int(a) == 3:
            break
        else:
            print("输入的不符合标准，请重新输入")
