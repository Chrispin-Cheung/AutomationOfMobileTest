# -*- coding:UTF-8 -*-
# Author:iotrookie
# Function: 注册、登录、退登
# Create Time:2017-04-06 2:01
# Edit Author:
# Edit Function:
# Edit CreateTime:
import xlrd
import xlwt

class register_login_logout(object):
    def check_user_name(self,rvu):
        if (len(rvu)>=6 and len(rvu)<=20):
            # 遍历excel表内user列的值
           # user_info = xlrd.open_workbook('J:\POPTEST\CodeResources\PyCharm3\Tasks\t20170407\JD\data.xlsx')
            user_info = xlrd.open_workbook('/Volumes/Emma/POPTEST/CodeResources/PyCharm3/Tasks/t20170407/JD/data.xlsx')
            # print("打开了文件")
            table= user_info.sheet_by_index(0)
            #sheet1 = user_info.sheet_by_name(u'用户信息')
            nrows = table.nrows

            #print(nrows)
            #print (rvu)
            for i in range(nrows):
                if str(rvu) == table.cell(i,0).value:
                    return 1

                # else :
                #     return 2
        else:
            return 0
    def check_user_pwd(self,rvp):
        if (len(rvp)>=6 and len(rvp)<=24):
            return 1
        else:
            return 2


    def check_verification_code(self,rvvc):
        pass

    def reg_page_index(self):
        u = input("请输入用户名：")
        uflag = self.check_user_name(u)
        if uflag == 0:
            print("用户名不合法")
        elif uflag == 1:
            print("用户名已存在")

        p = input("请输入密码：")
        pflag = self.check_user_pwd(p)
        if pflag == 2:
            print("密码输入不合法")
        cp = input("请再次输入密码")#Confirm password
        if p == cp:
            print("密码两次输入不一致")
        user_info = xlrd.open_workbook('../JD/data.xlsx')
        table= user_info.sheet_by_index(0)
        nrows = table.nrows
    def check_user_info(self,rvu,rvp):
        user_info = xlrd.open_workbook('../JD/data.xlsx')





    def login_page_index(self):
        u = input("输入用户名：")
        p = input("输入密码：")
        flag = self.check_user_info(u,p)
        if flag == 1:
            print("成功")
        else:
            print("失败")

if __name__ == "__main__":
    pass
#-----------------------Main Function--------------------------

print("/*************注册、登录、退登************/")
x = input("请输入一个字符：")
if (x == 'A' or x == 'a'):
    register_login_logout().reg_page_index()
elif (x == 'B' or x == 'b'):
    pass
elif (x == 'C' or x == 'c'):
    pass
else:
    print("非法操作")
print("/*************End************/")
