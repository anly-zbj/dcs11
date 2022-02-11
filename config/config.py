"""
Time:2022-02-11 17:07
"""
'''
此模块用来存放接口的入参信息，url，headers
'''
#1登录接口的入参信息
login_url='http://cms.duoceshi.cn/cms/manage/loginJump.do'
login_headers={
    'Content-Type': 'application/x-www-form-urlencoded'
}
login_data={
    'userAccount':' admin',
    'loginPwd': '123456'
}

#2查询全部用户接口的入参信息
queryUser_url = 'http://cms.duoceshi.cn/cms/manage/queryUserList.do'
queryUser_headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
queryUser_data = {
    'startCreateDate':'',
    'endCreateDate':'',
    'searchValue':'',
    'page':1
}

#3新增用户接口入参信息
addUser_url = 'http://cms.duoceshi.cn/cms/manage/saveSysUser.do'
addUser_headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
addUser_data = {
    'id':'',
    'userName':'zbj2',
    'userSex':1,
    'userMobile':13912345678,
    'userEmail':'123@qq.com',
    'userAccount':'zbj5',
    'loginPwd':'123456',
    'confirmPwd':'123456'
}
#4删除用户接口入参信息
deleteUser_url = 'http://cms.duoceshi.cn/cms/manage/deleteByIds.do'
deleteUser_headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
deleteUser_data = {
    'ids': '125990'
}
#5查询指定用户接口入参信息
findUser_url = 'http://cms.duoceshi.cn/cms/manage/queryUserList.do'
findUser_headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
findUser_data = {
    'startCreateDate':'',
    'endCreateDate':'',
    'searchValue':'dcs',
    'page':1
}