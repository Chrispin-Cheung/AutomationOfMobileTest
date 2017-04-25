# -*- coding:utf-8 -*-

from appium import webdriver
from Utils.Common import singleton
@singleton
class AppiumDriver(object):
    def __init__(self):
        desired_caps = {}

        desired_caps["devices"] = "lte26007"
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "4.4"
        desired_caps["deviceName"] = "HM_2A"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

#AppiumDriver().driver