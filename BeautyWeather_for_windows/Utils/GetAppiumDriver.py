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

from appium import webdriver


from Utils import Setting

from Utils.common import singleton
@singleton

class GetAppiumDriver(object):
    def __init__(self):
        desired_caps = {}
        desired_caps['devices'] = Setting.Devices
        desired_caps['platformName'] = Setting.PlatformName
        desired_caps['platformVersion'] = Setting.PlatformVersion
        desired_caps["deviceName"] = Setting.DeviceName
        desired_caps["unicodeKeyboard"] = Setting.UnicodeKeyboard
        desired_caps["resetKeyboard"] = Setting.ResetKeyboard

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

if __name__ == "__main__":
    pass

#dr = GetAppiumDriver().driver