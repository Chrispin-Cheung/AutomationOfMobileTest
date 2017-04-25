# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:单例模式，保证一次测试只用一个appium session ID
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

#单例模式函数，用来修饰类
#cls
def singleton(cls,*args,**kw):
    instances = {}
    def _singleton():
        #如果cls不在字典中，新建一个cls放入字典instances中
        if cls not in instances:
            instances[cls] = cls(*args,**kw)
        #如果在字典中，返回字典
        return instances[cls]
    return _singleton