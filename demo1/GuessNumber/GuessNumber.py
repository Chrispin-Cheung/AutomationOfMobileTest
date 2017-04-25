# -*- coding:UTF-8 -*-
# Author: iotrookie
# Function:猜数游戏
# Create Time:2017-04-06 2:01
# Edit Author:
# Edit Function:
# Edit CreateTime:
i=2018
k=0
run=True
print("""

                    猜数字，测智力

""")

while run:
    j=int(input("请输入一个数字： "))
    k=k+1
    if j==i:
        run=False
    elif j>i and j>=3000:
        print("你整那老大干啥呀？靠点谱行不？")
    elif j>i and j<=3000:
        print("大了大了")
    elif j<i and j<=1000:
        print("太抠门了，往大了整啊！！！")
    elif j<i and j>=1000:
        print("再大点，说你呢！")

if k<10:
    print()
    print(" ",k," 次就猜出来了,厉害！！")
elif k<15:
    print()
    print(" ",k," 次猜出来，恩...还行，接着上18期吧")
else:
    print()
    print(" ",k," 次才猜出来，你走吧，茑萝已经不适合你了...")

