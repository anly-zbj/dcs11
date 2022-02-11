#coding=utf-8
from public.pages.basepages import Basepages
from selenium import webdriver
from time import sleep
from public.utils.read_ini import read
import unittest
from public.pages.page_element import p

url=read.get_value("test_data","url")
username=read.get_value("test_data","username")
password=read.get_value("test_data","password")
# driver=webdriver.Chrome()
# driver.maximize_window()

class  Test_Login(Basepages):
    @classmethod
    def  setUpClass(cls) -> None:
        driver=webdriver.Chrome()   # 创建一个浏览器对象
        Basepages.set_driver(driver)  #  用Basepagaes调用类方法将driver传给类属性

    @classmethod
    def  tearDownClass(cls) -> None:
        sleep(3)

    def  test_login(self):
        #1.拿到cls.driver, 并且赋值给driver这个变量
        driver=Basepages.get_driver()
        driver.get(url)
        driver.maximize_window()
        sleep(1)
        #2.定输入框，并且输入username
        elem=Basepages.find_element(p.userName)    #  返回一个cls.driver.find_element_by_id()
        Basepages.sendkeys(elem,username)
        # 3.定位 密码框， 并且输入密码
        elem2=Basepages.find_element(p.passwd)
        Basepages.sendkeys(elem2,password)
        #4.点击登录按钮
        elem3=Basepages.find_element(p.loginbtn)
        Basepages.click(elem3)
        #5. 断言
        sleep(1)
        quit=["link_text","退出"]
        elem4=Basepages.find_element(quit)
        value=elem4.text
        assert value=="退出"   # 断言 获取的文本内容，等于“退出”
# if __name__ == '__main__':
#     unittest.main()




