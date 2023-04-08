# # for循环内层失效
# #因为生成器只能遍历一次
# a = (x for x in range(3))
# b = (x for x in range(2))
# for i in a:
#     for j in b:
#         print(i, j)
# #解决方案
# for i in (x for x in range(3)):
#     for j in (x for x in range(2)):
#         print (i,j)
# 简化写法
# a = [x for x in range(0,3)]
