#coding:utf-8
#导入读取Excel模块
import xlrd
#定义一个类
class regAndLoginAndLogout(object):
    #定义校验密码的方法
    def checkPwd(self,revPwd):
        #判定密码长度，（获取字符串长度使用函数len）
        if 6>len(revPwd) or len(revPwd)>20:
            return 0
    #定义校验密码的方法
    def checkUserName(self,revuser):
        if 6<=len(revuser)<=18:
            #定位excel（使用绝对路径）,并打开，打开excel用xlrd中的内置函数open_workbook
            a=xlrd.open_workbook("/Users/poptest/python1/poptest17/JDpoolData/username.xlsx")
            #a=xlrd.open_workbook("../JDpoolData/username.xlsx")
            #定位sheet页(可以通过表名和角标)
            b=a.sheet_by_name("user")
            #获取总行数
            #print(b.nrows)
            #遍历循环
            for i in range(1,b.nrows):
                #通过行列组合获取值与传递过来的参数进行对比
                if b.cell(i,0).value==revuser:
                    return 1
        else:
            return 0
    def regUserIndex(self):
        user=input("请输入用户名：")
        #1、调用同一类下的方法，并传递参数；
        #2、接收调用方法中的返回
        code=self.checkUserName(user)
        if code==0:
            print("不合法")
        elif code==1:
            print("用户名已存在")
            exit()
        else:
            print("用户名可用")
        pwd=input(" 请输入密码：")
        code1=self.checkPwd(pwd)
        if code1==0:
            print("密码不合法！")
            exit()
        else:
            print("密码可用")
        Pwd2=input("请再次输入密码：")
        if pwd==Pwd2:
            print("成功")
        else:
            print("不一致")
    def loginCheck(self,revU,revP):
        a=xlrd.open_workbook("/Users/poptest/python1/poptest17/JDpoolData/username.xlsx")

        b=a.sheet_by_name("user")
        #获取总行数
        #print(b.nrows)
        for i in range(1,b.nrows):
            if b.cell(i,0).value==revU and b.cell(i,1).value==revP:
                return 1
    def loginIndex(self):
        u=input("输入用户名：")
        p=input("输入密码：")
        k=self.loginCheck(u,p)
        if k==1:
            print("chenggong")
        else:
            print("shibai")
    def LogoutIndex(self):
        pass
    def pageIndex(self):
        print("#*********************")
        print("#*****  A  注册  *****")
        print("#*****  B  登录  *****")
        print("#*****  C  退登  *****")
        print("#*********************")
        m=input("请输入任意字符：")
        if m=="A" or m=="a":
            self.regUserIndex()
        if m=="B" or m=="b":
            self.loginIndex()
        else:
            print("qqqqq")

if __name__ == '__main__':
    regAndLoginAndLogout().pageIndex()
