# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:登录测试用例
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

#导入读取XML文件的模块
from xml.dom import minidom

class ReadXMLDriver(object):
    def returnXMLfile(self,filename,firstNode,secondNode):
        #use mindom to open a xml file
        # 该模块为公用模块，不能给定具体变量，谁用谁赋值
        # 使用mindom打开XML文件，该模块为公用模块不能写死，赋给任意变量谁使用谁传递
        fp = minidom.parse("../DataPool/"+filename)
        #层次遍历xml文件的标签名
        #在文件的基础上获取一级标签
        rootNode = fp.getElementsByTagName(firstNode)[0]
        #在一级标签的基础上获取二级标签的子集合点节点值
        secondNode = rootNode.fp.getElementsByTagName(firstNode)[0].childNodes[0].nodeValue
        return secondNode