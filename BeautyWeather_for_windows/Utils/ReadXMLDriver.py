# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:
import os
import sys
os.getcwd()
sys.path.append(os.getcwd())
from xml.dom import minidom

class ReadXMLDriver(object):
    def returnXMLfile(self,filename,firstNode,secondNode):
        #use mindom to open a xml file

        fp = minidom.parse("../DataPool/"+filename)

        rootNode = fp.getElementsByTagName(firstNode)[0]

        secondNode = rootNode.fp.getElementsByTagName(firstNode)[0].childNodes[0].nodeValue
        return secondNode