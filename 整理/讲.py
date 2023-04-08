# print('*'*50+"read函数"+'*'*50)
# f1 = open('test.txt', 'r')
# data1 = f1.read()
# print(data1)
# f1.close()

# print('*'*50+"readline函数"+'*'*50)
# f2 = open('test.txt', 'r')
# data2 = f2.readline()
# print(data2)
# data3 = f2.readline()
# print(data3)
# f2.close()
# # readline方法会记住上一个readline函数读取的位置，接着读取下一行.

# print('*'*50+"readlines函数"+'*'*50)
# f3 = open('test.txt', 'r')
# data4 = f3.readlines()
# # print(data4)
# for i in data4:
#     print(i)
# f3.close()

# f= open("test.txt", "w")
# f.write("hello word\n")
# f.write("welcome to cust")
# f.close()

f= open("test.txt", "a")
f.write("\nhaha")
f.close()


