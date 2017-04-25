# -*- coding:UTF-8 -*-
# Author:iotrookie
# Function:除
# Create Time:2017-04-06 2:01
# Edit Author:
# Edit Function:
# Edit CreateTime:

#---------------  函数定义 ----------------
def inNum():   # while循环+递归
    m = int(input("输出一个0～10的数："))
    flag = True
    while flag:
        if(m >= 0 and m <= 10):
            flag = False
            return m
        else:
            flag = True
            print("0-10")
            n=inNum()
            return n

def divsample(x,y,op):
    if 0 <= a <= 10 and 0 <= b <=10:
        if a == 10 and b == 3:
            if op == "//":
                z = x // y
                print(x, "被", y, "除的商向下取整为：", x, '/／', y, '=', z)
        elif a == 7 and b == 3:
            if op == "%":
                z = x % y
                print(x, "被", y, "除的余为：", x, '/／', y, '=', z)
        elif a ==0 or b == 0:# 不确定a 、b谁为除数的情况下，都不能为零，为零就为Error
            print ("Error")
        else:
            return

#---------------- 主函数 ------------------
print("请输入第一个数：")
a = inNum()
print("请输入第二个数：")
b = inNum()
o = input("请输入运算符：")
divsample(a,b,o)
if(o == '//'):
    if a == 10 and b == 3:
        pass
    else:
        c = a // b
        print(a, "被", b, "除的商向下取整为：", a, '/／', b, '=', c)
elif (o == '%'):
    if a == 7 and b == 3:
        pass
    else:
        c = a % b
        print(a, "被", b, "除的余数为：", a, '%',b, '=', c)
else:
    c = a / b
    print (a,"被",b,"除的商为：",a,"%",b ,"=", c)