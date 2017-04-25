# -*- coding:utf-8 -*-

from Utils.AppiumDriver import AppiumDriver

class AppiumAPIHelp(object):
    def __init__(self):
        global x,y# define two global variable
        self.conn = AppiumDriver().driver
        x = self.conn.get_window_size()["width"]
        y = self.conn.get_window_size()["height"]
    def Up_to_Down(self):
        try:
            self.conn.swipe(x/2,y*0.2,x/2,y*0.9,500)
        except Exception as err:
            assert False,"Error at Swiping from Up to Down !"
    def Down_to_Up(self):
        try:
            self.conn.swipe(x/2,y*0.9,x/2,y*0.2,500)
        except Exception as err:
            assert False,"Error at Swiping from Down to Up !"
    def Left_to_Right(self):
        try:
            self.conn.swipe(x*0.2,y/2,x*0.9,y/2,500)
        except Exception as err:
            assert False,"Error at Swiping from Left to Right !"
    def Right_to_Left(self):
        try:
            self.conn.swipe(x*0.9,y/2,x*0.2,y/2,500)
        except Exception as err:
            assert False,"Error at Swiping from Right to Left !"
    def Touch(self):
        try:
            self.conn.tap([(x/2,y/2)])
        except Exception as err:
            assert False,"Error at tap the Screen"

if __name__ == '__main__':
    pass