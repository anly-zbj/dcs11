"""
Time:2022-02-11 17:10
"""
'''
此模块用来组建接口
'''
from config.config import *
import requests
class Cms:
    def __init__(self):
        self.session=requests.Session()

    def login(self):
        response=self.session.post(url=login_url,headers=login_headers,data=login_data)
        return response.json()

    def queryUser(self):
        response = self.session.post(url=queryUser_url, headers=queryUser_headers, data=queryUser_data)
        return response.json()

    def addUser(self):
        response = self.session.post(url=addUser_url, headers=addUser_headers, data=addUser_data)
        return response.json()

    def deleteUser(self):
        response = self.session.post(url=deleteUser_url, headers=deleteUser_headers, data=deleteUser_data)
        return response.json()

    def findUser(self):
        response = self.session.post(url=findUser_url, headers=findUser_headers, data=findUser_data)
        return response.json()


if __name__ == '__main__':
    c=Cms()
    c.login()
    c.queryUser()
