# -*- coding:UTF-8 -*-
# Author:iotrookie
# Function: excel 读写
# Create Time:2017-04-10 2:01
# Edit Author:
# Edit Function:
# Edit CreateTime:

import xlrd
import xlwt

user_info = xlrd.open_workbook('/Volumes/Emma/POPTEST/CodeResources/PyCharm3/Tasks/t20170407/JD/data.xlsx')
sh = user_info.sheet_by_index(0)
#sh = user_info.sheet_by_name('userinfo')
nrow = sh.nrows
ncol = sh.ncols
print(nrow)
print(ncol)
name = 'zhangsan'
for i in range(nrow):
    # print(sh.row_values(i))
    #print(sh.cell(i,0).value)
    if name == sh.cell(i,0).value:
        print("you got it")
