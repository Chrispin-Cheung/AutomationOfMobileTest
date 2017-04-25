# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:单例模式，保证一次测试只用一个appium session ID
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

#单例模式函数，用来修饰类
def singleton(cls,*args,**kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args,**kw)
        return instances[cls]
    return _singleton