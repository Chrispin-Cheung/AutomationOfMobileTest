# -*- coding:UTF-8 -*-


#Author:
#CreateTime:
#Funciton:
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:

#导入时间模块
import time
#导入检查appium是否通过
from appium import webdriver
desired_caps = {}# Python3 的数据字典数据结构类型 定义字典desired_caps
#如小米手机，可以不加device厂商信息，如为其他机型，需要加：
desired_caps['devices'] = "lte26007"     # 厂商信息
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] = "4.4"
desired_caps["deviceName"] = "HM_2A" #设备名
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"

#通过此函数，与appium中的ID进行匹配并连接

#1、设备初始化（打开APP）
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
time.sleep(5) #设置间隔响应时间

#appium.swipe()滑屏操作函数
#swipe(start_x,start_y,end_x,end_y,duration)
#即开始点（start_x,start_y）滑动到终止点（end_x,end_y），duration为滑动操作的时间
#如何获取屏幕点的坐标，目前使用手机设备上的开发者选项中的指针工具来获取
#2、滑屏三次
for i in range(3):
    driver.swipe(600,500,100,500,500)#
    time.sleep(2)

#获取页面控件元素
#3、点击“立即体验”按钮
driver.find_element_by_class_name("android.widget.Button").click()
#driver.find_element_by_id("com.subject.zhongchou:id/bt").click()
time.sleep(3)

# 使用tap()函数执行页面任意位置点击操作
# 点击屏幕任意位置，坐标值此处可随意设置，故自定义为（520，520）
# 4、点击屏幕任意位置
driver.tap([(520,520)])
time.sleep(3)

#获取页面空间元素，如果classname，id相同的情况下，选择如下函数，通过田间index来区别
#5、点击“我的”Tab
driver.find_elements_by_class_name("android.widget.CheckedTextView")[3].click()#中括号内填大框的index值，括号内取小框的classname
#driver.find_element_by_android_uiautomator("new UiSelector().text(\"我的\")").click()
#注意此时find_elements_android_uiautomator()无click()操作，误输会报错
# driver.find_elements_by_id("com.subject.zhongchou:id/item_name")[3]
time.sleep(3)


#6、点击马上登录（登录icon或头像）
driver.find_element_by_id("com.subject.zhongchou:id/login_now_tv").click()
time.sleep(5)
#7、定位用户名输入框并输入用户名
driver.find_element_by_id("com.subject.zhongchou:id/loginnumber_phones").send_keys("18983838625")
time.sleep(3)

#8、定位密码输入框并输入与用户名匹配的密码
driver.find_element_by_id("com.subject.zhongchou:id/loginnumber_password").send_keys("12345678")
time.sleep(3)

#9、点击登录按钮
driver.find_element_by_id("com.subject.zhongchou:id/go_numberlogin").click()
time.sleep(3)

#10、预期结果与实际结果对比
#username = driver.find_element_by_android_uiautomator("new UiSelector().text()")

username = driver.find_element_by_id("com.subject.zhongchou:id/name_tv").text
if username == "kpnova":
    print ("与预期结果一致！")
    #
    #
    # time.sleep(2)
    # driver.tap([(188.6,259.7)])
    # time.sleep(1)
    # driver.find_element_by_id("com.subject.zhongchou:id/usercenter_modify_sex").click()
    # time.sleep(2)
    # driver.find_elements_by_id("android:id/text1")[2].click()
    # sex = "保密"
    # if sex == driver.find_element_by_id("com.subject.zhongchou:id/usercenter_modify_sex").text:
    #     print ("修改性别成功！")
    # # sex = "女"
    # # if sex == driver.find_element_by_id("com.subject.zhongchou:id/usercenter_modify_sex").text:
    # #     driver.find_elements_by_id("android:id/text1")[2].click()
    # #     sex = "保密"
    # #     if sex == driver.find_element_by_id("com.subject.zhongchou:id/usercenter_modify_sex").text:
    # #         print ("修改性别成功！")
    # # else:
    # #     print("我是女的了，你还改")
    # # time.sleep(3)
else:
    print ("与预期结果不一致！")

# 代码实现手机切换appium键盘？
print("＊＊＊＊＊＊＊＊ending＊＊＊＊＊＊＊＊")