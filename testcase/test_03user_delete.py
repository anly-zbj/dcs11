"""
Author:ZBJ
Time:2022-02-08 10:58
"""
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
        pass

    @classmethod
    def  tearDownClass(cls) -> None:
        sleep(3)

    def test_user_delete(self):
        #进入iframe框
        elem=Basepages.find_element(p.ifame)
        Basepages.switch_iframe(elem)
        # 复选框
        elem2 = Basepages.find_element(p.userFrame)
        Basepages.click(elem2)
        sleep(1)
        # 删除按钮
        elem3 = Basepages.find_element(p.deleteButton)
        Basepages.click(elem3)
        sleep(1)
        # 确认按钮
        elem4 = Basepages.find_element(p.confirButton)
        Basepages.click(elem4)
        Basepages.quit_iframe()