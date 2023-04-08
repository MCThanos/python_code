import csv

f = open("test.csv", "w",newline="")
# 操作文件对象时，需要添加newline参数逐行写入，否则会出现空行现象
csvwrite = csv.writer(f)
# 参数delimiter 指定分隔符，默认为逗号
csvwrite.writerow([1, 2, 3, 4])
csvwrite.writerow([5, 6, 7, 8])
# writerow 单行写入，将一个列表全部写入csv的同一行。
csvwrite.writerows([['hello', 'world'], ['I', 'love', 'you']])
# writerows()将一个二维列表中的每一个列表写为一行。
f.close()

f = open("test.csv", "r")
csvreads = csv.reader(f)
print(type(csvreads))
for csvread in csvreads:
    print(csvread)
f.close()


