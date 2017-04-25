# -*- coding:utf-8 -*-

import time
import unittest


from Utils.AppiumDriver import AppiumDriver
from Utils.AppiumAPIHelp import AppiumAPIHelp
from PageObject.NowEnjoyIndex import NowEnjoyIndex
from PageObject.HomePageIndex import HomePageIndex
from PageObject.SearchPageIndex import SearchPageIndex

class RES():
    actValue = "人民的名义"
    expValue = "\\android.widget.TextView[@test = \"人民的名义\"]"



class SearchModle(unittest.TestCase):

    def setUp(self):
        self.conn = AppiumDriver().driver
        time.sleep(20)
        for i in range(2):
            AppiumAPIHelp().Right_to_Left()
            time.sleep(1)
        NowEnjoyIndex().NowEnjoy_Btn().click()
        time.sleep(8)

        # wait for the mask layer 遮罩层
        AppiumAPIHelp().Touch()
        time.sleep(10)


    def tearDown(self):
        pass

    def testSearch001(self):
        HomePageIndex().SearchBox().click()
        time.sleep(5)

        #SearchPageIndex().TopSearch_By_Ids(0).click()# 选择热门搜索的数据项
        SearchPageIndex().TopSearch_By_xpath().click()# 选择热门搜索的数据项

        expValue = self.conn.find_element_by_xpath(RES.expValue)
        self.assertEqual(RES.actValue,expValue)

        # SearchPageIndex().SeachBox_By_Id().clear() #clear the content of the textbox
        # time.sleep(10)




if __name__ == '__main__':
    unittest.main()