# -*- coding:utf-8 -*-
from Utils.AppiumDriver import AppiumDriver
class RES():
    box_id = "com.qiyi.video:id/phoneSearchKeyword"
    hotword_item = "com.qiyi.video:id/search_hotword_item"
    topw_className = "android.widget.TextView[@text = \"人民的名义\"]"

class SearchPageIndex(object):
    def __init__(self):
        self.conn = AppiumDriver().driver

    def SeachBox_By_Id(self):
        try:
            SearchBox = self.conn.find_element_by_id(RES.box_id)
        except Exception as err:
            assert False,"Error at Locate the SearchBox !"
        return SearchBox

    def TopSearch_By_Ids(self,index):
        try:
            HotWord = self.conn.find_elements_by_id(RES.hotword_item)[index]
        except:
            assert False,"Error at Locate the Top Search By ids!"
        return HotWord

    def TopSearch_By_xpath(self):
        try:
            HotWord = self.conn.find_element_by_xpath(RES.topw_className)
        except Exception as err:
            assert False,"Error at Locate the Top Search By xpath !"
        return HotWord