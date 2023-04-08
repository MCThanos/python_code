import csv

#  r+
# 打开文件之后光标位置位于0的位置,根据光标位置读写
f = open("test.txt", "r+")
f.write("r+")
data = f.read()
print(data)
f.close()

# f1 = open("test.txt", "r")
# f2 = open("test.txt", "r+")
# while (data != "end\n"):
#     connect = f1.readline()
#     data = connect.replace("\n", " ") + "end\n"
#     f2.write(data)
# f1.close()
# f2.close()

f1 = open("test.csv", "r")
f2 = open("test.csv", "r+", newline="")
datas = csv.reader(f1)
csvwrite = csv.writer(f2)
for data in datas:
    data.append("end")
    csvwrite.writerow(data)
f1.close()
f2.close()
