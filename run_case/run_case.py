"""
Time:2022-02-11 18:49
"""
from utils.HTMLTestRunner3_New import HTMLTestRunner
from time import strftime
import unittest
now=strftime('%Y-%m-%d_%H-%M-%S')
file=r'F:\PythonProjects\cms_api_auto\report'+'\\'+now+'_api自动化测试报告.html'
f=open(file,'wb')
stat_dir=r'F:\PythonProjects\cms_api_auto\test_case'
discover=unittest.defaultTestLoader.discover(start_dir=stat_dir,pattern='test*.py')
runner=HTMLTestRunner(
    stream=f,
    description="用例执行情况如下",
    tester="zbj",
    title='接口自动化测试报告'
)
runner.run(discover)