# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:连接Appium服务器，设备初始化（打开APP）
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

#导入webdriver模块
from appium import webdriver


#导入Setting文件
from Utils import Setting
#导入Setting模块
#from utils.Setting import Setting

#单例模式函数，用来修饰
#开启单例模式后，要把响应时间调长一点
from Utils.common import singleton
@singleton
#定义一个类，且不继承
class GetAppiumDriver(object):
    def __init__(self):
        desired_caps = {}# Python3 的数据字典数据结构类型 定义字典desired_caps
        #如小米手机，可以不加device厂商信息，如为其他机型，需要加：
        desired_caps['devices'] = Setting.Devices   # 厂商信息
        desired_caps['platformName'] = Setting.PlatformName
        desired_caps['platformVersion'] = Setting.PlatformVersion
        desired_caps["deviceName"] = Setting.DeviceName#设备名
        #启用appium键盘
        desired_caps["unicodeKeyboard"] = Setting.UnicodeKeyboard
        desired_caps["resetKeyboard"] = Setting.ResetKeyboard

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

if __name__ == "__main__":
    pass

#dr = GetAppiumDriver().driver