def three(A1, A2, A3, c1, c2, c3):
    c1 = c1
    c2 = c2
    c3 = c3
    a1 = A1
    a2 = A2
    a3 = A3
    for i in range(1, 100):
        print(a1, end="")
        a4 = (c3 * a1) ^ (c2 * a2) ^ (c1 * a3)
        a1 = a2
        a2 = a3
        a3 = a4
        if (a1 == A1 and a2 == A2 and a3 == A3):
            print("\n" + str(i))
            break


def four(A1,A2,A3,A4):
    a1 = A1
    a2 = A2
    a3 = A3
    a4 = A4
    for i in range(1, 100):
        print(a1, end="")
        a5 = a1 ^ a4 ^ 1 ^ (a2 * a3)
        a1 = a2
        a2 = a3
        a3 = a4
        a4 = a5
        if (a1 == A1 and a2 == A2 and a3 == A3 and a4 == A4):
            print("\n" + str(i))
            break


if __name__ == '__main__':
    #    三级寄存器
    print("第一题：")
    A1 = 1
    A2 = 0
    A3 = 1
    for i in range(0, 2):
        for j in range(0, 2):
            three(A1, A2, A3, i, j, 1)
    #    四级寄存器
    print("第二题：")
    A1 = 1
    A2 = 1
    A3 = 0
    A4 = 1
    four(A1,A2,A3,A4)

