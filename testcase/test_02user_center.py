#coding=utf-8
from public.pages.basepages import Basepages
from selenium import webdriver
from time  import sleep
from public.utils.read_ini import read
import unittest
from public.pages.page_element import p

class  User_Center(Basepages):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def  tearDownClass(cls) -> None:
        sleep(3)
    def  test_user_center(self):
        #用户中心
        elem=Basepages.find_element(p.userCenter)
        Basepages.click(elem)
        #用户管理
        elem2=Basepages.find_element(p.userManage)
        Basepages.click(elem2)























