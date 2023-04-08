import base64


def incontent():
    a = input()
    result = []
    for i in a:
        result1 = list(bin(ord(i)).replace("0b", ""))
        length = len(result1)
        result2 = [0] * (8 - length)
        result3 = result2 + result1
        result = result + result3
    if (len(result) > 64):
        print("超出长度")
    while (len(result) < 64):
        result.append(0)
    for j in range(0, len(result)):
        result[j] = int(result[j])
    return result


def outcontent(a):
    result = ""
    lenth = 1
    for i in a:
        result = result + str(i)
        if (lenth == 8):
            result = result + str(" ")
            lenth = 0
        lenth = lenth + 1
    resultall = ""
    lit = result.split(' ')
    del lit[-1]
    for j in lit:
        asc = int(j, 2)
        resultall = resultall + chr(asc)
    print("经过DES加密/解密后的内容:"+resultall)
    return resultall


def jiemiincontent(bs64):
    debs64 = base64.b64decode(bs64)
    print("经过bs64解密后的内容:", end="")
    print(debs64.decode("utf-8"))
    result = []
    for i in debs64.decode("utf-8"):
        result1 = list(bin(ord(i)).replace("0b", ""))
        length = len(result1)
        result2 = [0] * (8 - length)
        result3 = result2 + result1
        result = result + result3
    for j in range(0, len(result)):
        result[j] = int(result[j])
    return result
