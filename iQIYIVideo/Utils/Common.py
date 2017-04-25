# -*- coding:utf-8 -*-

#singleton ,use to decorate修饰 类class

def singleton(cls,*args,**kw):
    instances = {}
    def _singleton():
        #如果cls不在字典中，新建一个cls放入字典instances中
        if cls not in instances:
            instances[cls] = cls(*args,**kw)
        #如果在字典中，返回字典
        return instances[cls]
    return _singleton