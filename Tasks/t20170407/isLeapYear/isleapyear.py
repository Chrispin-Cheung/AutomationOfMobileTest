# -*- coding:UTF-8 -*-
# Author:iotrookie
# Function:判断一个年份是否为闰年
# Create Time:2017-04-09
# Edit Author:
# Edit Function:
# Edit CreateTime:

year = int(input("请输入一个年份:"))
if (year % 4 ==0 and year %100 != 0):
    leap = True
elif year % 400 ==0:
    leap = True
else:
    leap = False
if leap == True:
    print(year,"is leap year !","\t\n"+str(year),"是闰年 !")
else:
    print(year,"is not leap year !","\t\n"+str(year),"不是闰年 !")