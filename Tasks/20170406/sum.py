# -*- coding:UTF-8 -*-
# Author:iotrookie
# Function:加法
# Create Time:2017-04-06 2:01
# Edit Author:
# Edit Function:
# Edit CreateTime:

#---------------  函数定义 ----------------
def inNum():   # while循环+递归
    m = int(input("输出一个71～100的数："))
    flag = True
    while flag:
        if(m >= 71 and m <= 100):
            flag = False
            return m
        else:
            flag = True
            print("71-100")
            n=inNum()
            return n

#---------------- 主函数 ------------------
print("请输入第一个数：")
a = inNum()
print("请输入第二个数：")
b = inNum()
c = a + b
print ("和为："+str(a)+"+"+str(b)+"="+str(c))    #符号“+”连接字符串时，需注意变量的类型。非字符串行要转换成字符串形式





