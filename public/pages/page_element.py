#coding=utf-8
'''
此模块用来装页面的元素定位的文本

'''''

class  Page_elem(object):
    #1.1登录账号元素
    userName = ["id", "userAccount"]
    #1.2登录密码元素
    passwd = ["id", "loginPwd"]
    #1.3登录按钮元素
    loginbtn = ["id", "loginBtn"]

    #2.1用户中心
    userCenter=["xpath",'//*[@id="menu-user"]/dt']
    #2.2用户管理
    userManage=["xpath",'//*[@id="menu-user"]/dd/ul/li[1]/a']

    #3.1第一位用户前的复选框
    userFrame=["xpath",'//*[@id="sysUserTab"]/tr[1]/td[1]/input']
    #3.2批量删除按钮按钮
    deleteButton=["xpath",'/html/body/div/div[2]/span[1]/a[1]']
    #3.3确定按钮
    confirButton=["xpath",'/html/body/div[3]/div[1]/span[2]/a[1]']
    #3.4iframe框
    ifame = ["xpath", '//*[@id="iframe_box"]/div[2]/iframe']



p=Page_elem()


















