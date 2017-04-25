# -*- coding:UTF-8 -*-
# Author:iotrookie
# Function:加、减、乘、除、赋值运算
# Create Time:2017-04-06 2:01
# Edit Author:
# Edit Function:
# Edit CreateTime:

a = int(input('Please input a number:'))
operator = input('Please input an operator ＋ － ＊ ／:')
b = int(input('Please input another number:'))
# if operator == '+':
#     result = a + b
# if operator == '-':
#     result = a - b
# if operator == '*':
#     result = a * b
# if operator == '/':
#     result = a / b
# print(result)
result = 0
#输入判断运算符为＋，执行加法运算
if operator == '+':
    result = a + b

#输入判断运算符为－，执行减法运算
elif operator == '-':
    result = a - b

#输入判断运算符为＊，执行乘法运算
elif operator == '*':
    result = a * b

#输入判断运算符为／，执行除法运算
elif operator == '/':
    result = a / b
else:
    print("Operator is invaild,Please retry to input an operator")


# 老师演示用伪代码
# #-*- coding:UTF-8 -*-
# #自定义加法函数并接收传递过来的参数，赋给自己
# def SumModel(x,y):
#     #判定接送过来的俩参数是否在加法运算区间
#     if 100>=x>=71 and 100>=y>=71:
#         #加法运算
#         o=x+y
#         print("和为:",x,"+",y,"=",o)
#     else:
#         #输出结果"71–100"
#         print("71–100")
# def subModel(m,n):
#     if 70>=m>=31 and 70>=n>=31:
#         if m>=n:
#             o=m-n
#             print("差为:",m,"-",n,"=",o)
#         else:
#             o=n-m
#             print("差为:",n,"-",m,"=",o)
#     else:
#         print("31–70")
# def mulModel():
#     pass
# def devModel(o,p):
#     if 10>=o>=0 and 10>=p>=0:
#         if o==7 and p==3:
#             print("运算％")
#             #pass
#
#         elif o==10 and p==3:
#             # pass
#             print("运算／／")
#         elif o==0 and p==0:
#             print("1234567")
#         else:
#             o/p
#     else:
#         print("0–10")
# #主函数
# a=int(input("请输入第一个数："))#输入第一个数：
# c=input("请输入运算符：")
# b=int(input("请输入第二个数："))
# #判断输入俩个数的取值区间
# if 100>=a>=0 and 100>=b>=0:
#     #判断运算符
#     if c=="+":
#         #调用加法自定义函数，传递参数
#         SumModel(a,b)
#     elif c=="-":
#         subModel(a,b)
#     elif c=="*":
#         pass
#     elif c=="/" or c=="//" or c=="%":
#         devModel(a,b)
#     else:
#         print("输入非法字符")
# else:
#     #输入"超出取值范围"
#     print("超出取值范围")

