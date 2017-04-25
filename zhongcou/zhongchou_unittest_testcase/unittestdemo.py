# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:Unittest单元测试框架简单模版
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

import unittest

class UnittestDemo(unittest.TestCase):#括号内为被继承的基类为unittest.TestCase
    #-------用例的构建和销毁-------
    #--用例执行初始化--
    def setUp(self):
        pass
    #--用例执行完后善后操作（结束并清理）--
    def tearDown(self):
        pass

    #---self added functions and methods
    # 功能点测试用例方法的命名模式，方法以test开头，后跟实现用例的方法和命名
    def testFunctionPoint1(self):
        pass
    def testFunctionPoint2(self):
        pass

if __name__ == "__main__":
    unittest.main()