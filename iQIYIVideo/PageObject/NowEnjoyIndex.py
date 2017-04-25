# -*- coding:utf-8 -*-


from Utils.AppiumDriver import AppiumDriver

class RES():
    Resource_Id = "com.qiyi.video:id/phone_qiyi_guide_enter"

class NowEnjoyIndex(object):
    def __init__(self):
        self.conn = AppiumDriver().driver

    def NowEnjoy_Btn(self):
        try:
            NowEnjoy_Btn_By_Id = self.conn.find_element_by_id(RES.Resource_Id)
        except Exception as err:
            assert False,"Error at locate the NowEnjoyBtn !"
        return NowEnjoy_Btn_By_Id
