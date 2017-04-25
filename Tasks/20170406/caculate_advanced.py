# -*- coding:UTF-8 -*-
# Author:iotrookie
# Function: 高级计算器（加、减、乘(乘、幂)、除（取整、求余））
# Create Time:2017-04-06 2:01
# Edit Author:
# Edit Function:
# Edit CreateTime:

#-----------------------Define Functions-----------------------

#加法运算 输入算数区间：71～100 例：71 + 100 = 171
def sum_moudle(x,y):            # 函数命名规范 全小写，字母之间使用下划线(_)隔开
    if(x >= 71 and x<=100):
        if(y >=71 and y<=100):
            z = x + y
            print ("和为：",x,'+',y ,'=', z)
        else:
            print("第二个数应在71－100区间")
    elif((x <71 or x >100) and (y < 71 or y >100)):
        print("两个数都应在71－100区间")
    else:
        print("第一个数应在71-100区间")



#减法运算 输入算数区间：31～70  例：70 - 40 = 30,40 - 70 = 30
def sub_moudle(x,y):
    if(x >= 31 and x<=70):
        if(y >=31 and y<=70):
            if(x > y):
                z = x - y
            else:
                z = y - x
            print ("差为：",x,'-',y ,'=', z)
        else:
            print("第二个数应在31－70区间")
    elif((x <71 or x >100) and (y < 71 or y >100)):
        print("两个数都应在31－70区间")
    else:
        print("第一个数应在31-70区间")



#乘法运算 输入算数区间：11～30  例：11 ＊ 20 = 220
def multi_module(x,y,op):
    # if(x >= 11 and x<=30):
    if 11 <= x <= 30:
        # if(y >=11 and y<=30):
        if 30 >= y >=11:
            if op == "*":
                z = x * y
                print ("积为：",x,'*',y ,'=', z)
            else:
                z = x ** y
                print(x,"的"+str(y)+"次幂为：", x, '**', y, '=', z)
        else:
            print("第二个数应在11－30区间")
    elif((x <11 or x >30) and (y < 11 or y >30)):
        print("两个数都应在11－30区间")
    else:
        print("第一个数应在11-30区间")


#除法运算 输入算数区间：0～10  例：10 ／ 3 = 3 , 7 ／ 3 = 1
def div_modlue(x,y,op):
    if(x >= 0 and x<=10):
        if(y >=0 and y<=10):
            if y == 0:
                print ("Error !")
            else:
                if(op == '//'):
                    z = x // y
                    print(x, "被", y, "除的商向下取整为：", x, '/／', y, '=', z)
                elif (op == '%'):
                    z = x % y
                    print(x, "被", y, "除的余数为：", x, '%', y, '=', z)
                else:
                    z = x / y
                    print (x,"被",y,"除的商为：",x,"%",y ,"=", z)
        else:
            print("第二个数应在0－10区间")
    elif((x <0 or x >10) and (y < 0 or y >10)):
        print("两个数都应在0－10区间")
    else:
        print("第一个数应在0-10区间")




#-----------------------Main Function--------------------------

print("/*************计算器************/")

#输入算数，运算符
a = int(input("请输入第一个数:"))
c = input("请输入一个运算符: ")
b = int(input("请输入第二个数: "))

#区分功能模块
if c == "+":
    sum_moudle(a,b)
elif c == "-":
    sub_moudle(a,b)
elif c == "*" or c == "**":
    multi_module(a,b,c)
elif c == "/" or c == "//" or c == "%":
    div_modlue(a,b,c)
else :
    print("输入运算符非法")
print("/*************End************/")
