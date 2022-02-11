#coding=utf-8

'''
此模块用来封装编写用例的一个基类。
'''''
import unittest
from selenium  import webdriver
# driver=webdriver.Chrome()

class  Basepages(unittest.TestCase):
    #单例模式：执行用例只会开启一个浏览器窗口
    @classmethod
    def  set_driver(cls,driver):   #  定义一个类方法，需要传入一个driver对象作为类属性（cls.driver）
        cls.driver=driver
    @classmethod
    def  get_driver(cls):   # 定义一个方法，谁调用它谁就获得这个类属性的driver
        return   cls.driver
    # baidu_input=["cla","kw"]
    @classmethod
    def  find_element(cls,element):   # 定义一个查找元素的方法，将所有的元素查找方式封装在同一个方法中
        type=element[0]
        value=element[1]
        if  type=="id":
            elem=cls.driver.find_element_by_id(value)
        elif type=="class":
            elem=cls.driver.find_element_by_class_name(value)
        elif  type=="xpath":
            elem=cls.driver.find_element_by_xpath(value)
        elif  type=="css":
            elem=cls.driver.find_element_by_css_selector(value)
        elif  type=="name":
            elem=cls.driver.find_element_by_name(value)
        elif  type=="link_text":
            elem=cls.driver.find_element_by_link_text(value)
        else:
            raise ValueError("please  input  correct  type! ")
        return elem
    @classmethod
    def  sendkeys(cls,elem,text):   #  封装一个输入文本的类方法
        return   elem.send_keys(text)

    @classmethod
    def  click(cls,elem):        # 封装一个点击的类方法
        return  elem.click()

    @classmethod
    def switch_iframe(cls,elem):        #进入ifame框的方法
        return cls.driver.switch_to.frame(elem)

    @classmethod
    def quit_iframe(cls):       #退出iframe框
        return cls.driver.switch_to.default_content()

if __name__ == '__main__':
    from public.utils.read_ini import Read_Ini
    import os
    from conf.config import data_path
    file=os.path.join(data_path,"data.ini")    # 拼接data_path和文件的名成为路径
    read=Read_Ini(file)     #创建一个Read_Ini类的对象，叫做read 。需要传入读取的文件的路径
    url=read.get_value("test01_data","url")  # 用read 对象调用get_value的方法获取到section下的option对应的值
    Basepages.set_driver(webdriver.Chrome())  #使用Basepages类调用类方法设置driver
    Basepages.get_driver().get(url)   # 再用类调用方法获取driver ，并且用获取到的driver  读取到的url
    baidu_input = ["id", "kw"]
    elem=Basepages.find_element(baidu_input) # 类调用类方法去获取元素定位
    Basepages.sendkeys(elem,"python")   #  用类调用类类方法对输入框进行输入








