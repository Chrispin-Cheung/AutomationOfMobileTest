# -*- coding:UTF-8 -*-
# Author:iotrookie
# Function:怪异计算器 Weird calculator
# Create Time:2017-04-07
# Edit Author:
# Edit Function:
# Edit CreateTime:

class  weird_Calculator(object):
    #function:
    def sum_moudle(self,x,y):
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


    #function:
    def sub_moudle(self,x,y):
        if(x >= 31 and x<=70):
            if(y >=31 and y<=70):
                if(x > y):
                    z = x - y
                    print ("差为：",x,'-',y ,'=', z)
                else:
                    z = y - x
                    print ("差为：",x,'-',y ,'=', z)
            else:
                print("第二个数应在31－70区间")
        elif((x <71 or x >100) and (y < 71 or y >100)):
            print("两个数都应在31－70区间")
        else:
            print("第一个数应在31-70区间")


    #function:
    def multi_moudle(self,x,y):
        if(x >= 11 and x<=30):
            if(y >=11 and y<=30):
                z = x * y
                print ("积为：",x,'*',y ,'=', z)
            else:
                print("第二个数应在11－30区间")
        elif((x <11 or x >30) and (y < 11 or y >30)):
            print("两个数都应在11－30区间")
        else:
            print("第一个数应在11-30区间")


    def div_moudle(self,x,y):
        if(x >= 0 and x<=10):
            if(y >=0 and y<=10):
                z = x / y
                print ("商为：",x,'／',y ,'=', z)
            else:
                print("第二个数应在0－10区间")
        elif((x <0 or x >10) and (y < 0 or y >10)):
            print("两个数都应在0－10区间")
        else:
            print("第一个数应在0-10区间")

    def weird_calculator(self):
        print("/*************计算器************/")
        #输入算数，运算符
        a = int(input("请输入第一个数:"))
        c = input("请输入一个运算符: ")
        b = int(input("请输入第二个数: "))

        #区分功能模块
        if c == "+":
            self.sum_moudle(a,b)
        elif c == "-":
            self.sub_moudle(a,b)
        elif c == "*":
            self.multi_moudle(a,b)
        elif c == "/":
            self.div_moudle(a,b)
        else :
            print("输入运算符非法")
            print("/*************End************/")

#if __name__ == "__main__":的作用与原理
#python的文件，两种使用的方法，1、直接作为脚本执行
#                           2、import到其他的python脚本被调用(模块重用)执行
#在if __name__ == 'main': 下的代码只有在第一种情况下(即文件作为脚本直接执行)才会被执行，而import到其他脚本中是不会被执行的。
'''
举个例子，下面在test.py中写入如下代码：
print "I'm the first."
if __name__=="__main__":
    print "I'm the second."
并直接执行test.py，结果可以成功print两行字符串。即，if __name__=="__main__": 语句之前和之后的代码都被执行。
然后在同一文件夹新建名称为import_test.py的脚本，只输入如代码：
import test
执行import_test.py脚本，只输出了第一行字符串。即，if __name__=="__main__": 之前的语句被执行，之后的没有被执行。
'''


if __name__ == "__main__":
    pass

#-----------------------main----------------------
#weird_Calculator().weird_calculator() #无传参的方法调用
