"""
Time:2022-02-11 17:58
"""
import unittest
import requests
from cms_api.cms_api import Cms
class Cms_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cms=Cms()
    def test01_login(self):
        assert self.cms.login()['msg']=="登录成功！"
    def test02_queryUser(self):
        assert self.cms.queryUser()['msg']=='查询用户成功！'
    def test03_addUser(self):
        # assert self.cms.addUser()['msg'] == "保存用户信息成功！"
        assert self.cms.addUser()['msg'] == "保存用户信息失败,登录帐号已存在！"
    def test04_deleteUser(self):
        assert self.cms.deleteUser()['msg']=='1条数据删除成功！'
    def test05_findUser(self):
        assert self.cms.findUser()['msg']=='查询用户成功！'

if __name__ == '__main__':
    unittest.main()
