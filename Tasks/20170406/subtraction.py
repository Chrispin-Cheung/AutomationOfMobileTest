# -*- coding:UTF-8 -*-
# Author:iotrookie
# Function:减
# Create Time:2017-04-06 2:01
# Edit Author:
# Edit Function:
# Edit CreateTime:

#---------------  函数定义 ----------------
def inNum():   # while循环+递归
    m = int(input("输出一个31～70的数："))
    flag = True
    while flag:
        if(m >= 31 and m <= 70):
            flag = False
            return m
        else:
            flag = True
            print("31-70")
            n=inNum()
            return n

#---------------- 主函数 ------------------
print("请输入第一个数：")
a = inNum()
print("请输入第二个数：")
b = inNum()
if(a > b):
    c = a - b
else:
    c = b - a
print("差为：",a,"-",b,"=",c)