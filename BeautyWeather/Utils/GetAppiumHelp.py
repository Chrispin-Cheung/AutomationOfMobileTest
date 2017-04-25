# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton:Appium基本函数的重载 如滑屏操作,点击任意位置等
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

from Utils.GetAppiumDriver import GetAppiumDriver
#import time

class GetAppiumHelp(object):
    pass
    def __init__(self):
        #Global variable
        global x,y
        self.driver = GetAppiumDriver().driver
        #get the width of the Gphone's screen width
        x = self.driver.get_window_size()["width"]
        #get the height of the Gphone's screen height
        y = self.driver.get_window_size()["height"]

    def up_to_down(self):
        self.driver.swipe(x/2,y*0.2,x/2,y*0.9,500)

    def down_to_up(self):
        self.driver.swipe(x/2,y*0.9,x/2,y*0.2,500)

    def left_to_right(self):
        self.driver.swipe(x*0.2,y/2,x*0.9,y/2,500)

    def right_to_left(self):
        #self.driver.swipe(x*0.9,y*0.5,x*0.2,y*0.5,500)
        self.driver.swipe(x*0.9,y/2,x*0.2,y/2,500)

    def tap(self):
        self.driver.tap([(x/2,y/2)])

    # def sleeptime(self):
    #     time.sleep(3)

if __name__ == "__main__":
    pass
