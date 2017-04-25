#coding:utf-8
from Utils.AppiumDriver import AppiumDriver
class HomePageIndex(object):
    def __init__(self):
        self.conn=AppiumDriver().driver

    def video(self):
        try:
            video=self.conn.find_element_by_id("com.qiyi.video:id/navi0")
        except Exception as err:
            assert False,"Error at Locate the video tab !"
        return video

    def HappyLive(self):
        try:
            HappyLive=self.conn.find_element_by_id("com.qiyi.video:id/navi1")
        except Exception as err:
            assert False,"Error at Locate the HappyLive tab !"
        return HappyLive

    def VIP(self):
        try:
            VIP=self.conn.find_element_by_id("com.qiyi.video:id/navi2")
        except Exception as err:
            assert False,"Error at Locate the VIP tab !"
        return VIP

    def MyBtn(self):

        MyBtn=self.conn.find_element_by_id("com.qiyi.video:id/navi3")
        return MyBtn

    def paopao(self):
        paopao=self.conn.find_element_by_id("com.qiyi.video:id/navi4")
        return paopao

    def Message(self):
        Message=self.conn.find_element_by_id("com.qiyi.video:id/ico_msg")
        return Message

    def ViewingHistory(self):
        ViewingHistory=self.conn.find_element_by_id("com.qiyi.video:id/ico_rec")
        return ViewingHistory

    def Plus(self):
        Plus=self.conn.find_element_by_id("com.qiyi.video:id/ico_plus")
        return Plus

    def SearchIcon_by_id(self):# locate the search_icon
        try:
            Search=self.conn.find_element_by_id("com.qiyi.video:id/title_search_icon_skin")
        except Exception as err:
            assert False,"Error at Locating the Search icon by id"
        return Search

    def Searchicon_by_xpath(self):
        try:
            search = self.conn.find_element_by_xpath("//com.qiyi.video:id/txt_left[@text='奔跑吧']")
        except Exception as err:
            assert False,"Error at Locating the Search icon by xpath"
    def SearchBox(self):
        try:
            Search = self.conn.find_element_by_id("com.qiyi.video:id/txt_left")
        except Exception as err:
            assert False,"Error at Locating the Search TextBox"
        return Search