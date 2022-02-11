#coding=utf-8
'''
此模块用来读取ini配置文件的信息
需要下载configparser 这个模块:  dos窗口  pip  install configparser
pyhton  -m  pip  install configparser
'''''
from   configparser import ConfigParser  # 导入configparser模块中的ConfigParser的类
from  conf.config import data_path
import os
class  Read_Ini(ConfigParser):
    def  __init__(self,file):
        super(Read_Ini, self).__init__()  #  继承父类的构造函数
        self.read(file)
    def get_value(self,section,option):
        return self.get(section,option)
file=os.path.join(data_path,"data.ini")
read=Read_Ini(file)  # 创建一个Read_Ini类的对象



# if __name__ == '__main__':
#     file=os.path.join(data_path,"data.ini")
#     read=Read_Ini(file)  # 创建一个Read_Ini类的对象
#     url=read.get_value("test_data","url")
#     print(url)


# class  Read_data_ini(ConfigParser):
#     def  get_value(self,file,section,option):
#         self.read(file)
#         return self.get(section,option)
#
# if __name__ == '__main__':
#     file = os.path.join(data_path, "data.ini")
#     r=Read_data_ini()
# #     r.read_ini(file)
#     value=r.get_value(file,"test_data","url")
#     print(value)














