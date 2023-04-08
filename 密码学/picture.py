import cv2
import numpy as np
from PIL import Image


def logistic(x, u, filename, savename):
    ima = Image.open(filename).convert('L')
    im = np.array(ima)
    M = im.shape[0]
    N = im.shape[1]
    array = np.zeros(M * N)
    for i in range(1, 1000):
        x = u * x * (1-x)
    array[0] = x
    for i in range(0, M * N - 1):
        array[i + 1] = u * array[i] * (1 - array[i])
    array = np.array(array * 255, dtype='uint8')
    code = np.reshape(array, (M, N))
    xor = im ^ code
    cv2.imwrite(savename, xor)


if __name__ == '__main__':
    while True:
        x = float(input("请输入x："))
        u = float(input("请输入u："))
        filename = input("请输入要加密/解密的文件路径：")
        savename = input("请输入保存结果的文件路径：")
        if 3.5699456 < u <= 4 and 0 < x < 1:
            logistic(x, u, filename, savename)
            print("加密/解密完成")
            break
        else:
            print("输入有误")
