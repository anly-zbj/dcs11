#coding=utf-8
'''
此模块是封装用来读取excel文档的工具类
xlrd 模块 ：需要进行下载。 pip install  xlrd 
'''''
import xlrd
from  conf.config import   data_path
import os
file=os.path.join(data_path,"data.xls")
# book=xlrd.open_workbook(file)
# sheet=book.sheet_by_name("Sheet1")
# value=sheet.cell_value(1,0)
# print(value)
class  Read_Excel(object):
    def  __init__(self,file,sheetname):
        self.book=xlrd.open_workbook(file)      #  创建一个book对象，然后赋值给self.book属性
        # 用self.book的属性去选择sheet页面，选择之后的sheet页面赋值给self.sheet的属性
        self.sheet=self.book.sheet_by_name(sheetname)
    def  get_excel_value(self,row,low):
        #使用self.sheet 的属性去调用cell_value方法来回去文件中的属性。需要传入行和列
        return self.sheet.cell_value(row,low)

#  创建一个r对象。  创建对象的时候就会打开工作簿，和选择sheet页面
# file=Read_Excel(file,"Sheet1")
# # 再使用r对象去调用get_excel_value的方法。 传入行和列的索引位
# reade=file.get_excel_value(1,0)



















