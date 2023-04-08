def count(a, b, c):
    a = a % c
    result = 1
    while b != 0:
        if (b % 2 == 1):
            result = (result * a) % c
        b >>= 1
        a = (a * a) % c
    return result


def qiuni(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = qiuni(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y


def jiami():
    a = input("请输入明文：")
    print("p*q需要大于100")
    p = int(input("请输入p："))
    q = int(input("请输入q："))
    e = int(input("请输入e："))
    n = p * q
    length = len(str(n)) - 1
    if (length % 2 != 0):
        length = length - 1
    result = ""
    for i in a.lower():
        if i == " ":
            result = result + "00"
            continue
        number = str(ord(i) - 96)
        if len(number) == 1:
            number = "0" + number
        result = result + number
    a = len(result) % length
    if (a != 0):
        result = result + "0" * (length - a)
        b = int((len(result) - a) / length + 1)
    else:
        b = int((len(result) - a) / length)
    print("加密结果为:", end="")
    for j in range(0, b):
        data = int(result[j * length:(j + 1) * length])
        print(count(data, e, n), end=" ")
    print()


def jiemi():
    a = input("请输入密文：")
    p = int(input("请输入p："))
    q = int(input("请输入q："))
    e = int(input("请输入e："))
    n = p * q
    fun_n = (p - 1) * (q - 1)
    length = len(str(n)) - 1
    if (length % 2 != 0):
        length = length - 1
    d = qiuni(e, fun_n)[0]
    if (d < 0):
        d = d + fun_n
    data_list = a.split(" ")
    for i in data_list:
        if i == "":
            continue
        result = str(count(int(i), d, n))
        if len(result) < length:
            result = "0" * (length - len(result)) + result
        for j in range(0, int(length / 2)):
            con = result[j * 2:(j + 1) * 2]
            if con == "00":
                print(" ", end="")
                continue
            con = int(con) + 96
            print(chr(con), end="")
    print()


if __name__ == '__main__':
    while True:
        print("*" * 100)
        print("1.加密")
        print("2.解密")
        print("3.退出")
        print("*" * 100)
        numbers = input("请输入功能对应的数字:")
        if (numbers == "1"):
            jiami()
        if (numbers == "2"):
            jiemi()
        if (numbers == "3"):
            break
