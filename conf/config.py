#coding=utf-8
'''
此模块： 是用来存放项目的配置路径的。 方便后续在其他模块进行导入使用
'''''
import os
#__file__代表的是当前文件  ==》config.py
#os.path.dirname 代表当前文件的上一级。
base_path=os.path.dirname(os.path.dirname(__file__))  # 代表当前文件的上两级.  项目的路径
#print(base_path)

conf_path=os.path.join(base_path,"conf")   # conf包的路径
#print(conf_path)

data_path=os.path.join(base_path,"data")  #  data包的路径

public_path=os.path.join(base_path,"public")  # public包的路径

pages_path=os.path.join(base_path,"public","pages")  #public包下的pages的路径

utils_path=os.path.join(base_path,"public","utils") #public包下的utils的路径

report_path=os.path.join(base_path,"report")   #report包的路径

testcase_path=os.path.join(base_path,"testcase")  # testcase包的路径



















