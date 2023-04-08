def qiuni():
    a = int(input("请输入想要求逆的数字"))
    for i in range(1, 27):
        if ((i * a - 1) % 26 == 0):
            print(i)
            break


def lock_method(a, b, m):
    number = ord(m) - 97
    result1 = (a * number + b) % 26
    result2 = chr(result1 + 97)
    return result2


def unlock_methog(a, b, c):
    ani = 0
    for i in range(1, 26):
        if ((i * a - 1) % 26 == 0):
            ani = i
            break
    number = ord(c) - 97
    result1 = (ani * (number - b)) % 26
    result2 = chr(result1 + 97)
    return result2


def lock(a, b, lock_cotent):
    for i in lock_cotent:
        if (i != " "):
            result = lock_method(a, b, i)
            print(result, end="")
        else:
            print(" ", end="")
    print()


def unlock(a, b, unlock_content):
    for i in unlock_content:
        if (i != " "):
            result = unlock_methog(a, b, i)
            print(result, end="")
        else:
            print(" ", end="")
    print()


# 第一个问题
lock_content = "the national security agency"
unlock_content1 = "ywp kxyhvkxo nptjchyb xlpktb"
print("第一个问题加密结果：", end="")
lock(11, 23, lock_content)
print("第一个问题解密结果：", end="")
unlock(11, 23, unlock_content1)

# 第二个问题
a = 0
b = 0
for i in range(1, 26):
    for j in range(1, 26):
        r1 = lock_method(i, j, "i")
        r2 = lock_method(i, j, "f")
        if (r1 == "e" and r2 == "d"):
            a = i
            b = j
            break
unlock_content2 = "edsgickxhuklzveqzvkxwkzukvcuh"
print("第二个问题解密结果：", end="")
unlock(a, b, unlock_content2)

# 求逆
qiuni()
