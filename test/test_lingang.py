#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""登录相关测试用例"""
import unittest
from base.method import *
from base.assert2 import *
from utils.operationExcel import operateExcel
from page.lingang import *

# # 断言：期望值与实际是否相等
# dy = self.assertTrue(self.a.isAssert(row=3, str2=r.text))
# # 断言：文件写入pass或false
# self.ass.isTure(row=3, duanyan=dy)


class test_Lingang(unittest.TestCase):
    def setUp(self):
        self.meth = methon()
        self.ass = Assert()
        self.excel = operateExcel()

    def statusCode(self, r):
        '''断言：协议状态码、业务状态码'''
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 2000)

    def isContent(self, row, str2):
        '''断言：响应内容'''
        self.ass.isAssert(row, str2)

    def test_login_001(self):
        '''测试登录'''
        r = self.meth.post(row=1)
        # print(r.text)
        self.statusCode(r)
        self.isContent(row=1, str2=r.text)
        # 每次获取的token不一致,需要动态获取
        List = []
        token = r.json()['data']['token']
        userId = r.json()['data']['userId']
        List.append(token)
        List.append(userId)
        # dumps序列化：将数据写入文件
        write_ResponseData(content=json.dumps(List))

    def test_sendVerifyCode_002(self):
        '''测试发送验证码'''
        r = self.meth.post1(row=3, type="3")
        # print(r.text)
        self.statusCode(r)
        self.isContent(row=3, str2=r.text)

    def test_forgetPassword_003(self):
        '''测试：忘记密码'''
        r = self.meth.post2(row=4, verifyCode="098489")
        # print(r.text)
        self.statusCode(r)
        self.isContent(row=4, str2=r.text)

    def test_modifyPassword_004(self):
        '''测试：修改密码'''
        r = self.meth.post3(row=5)
        # print(r.text)
        self.statusCode(r)
        self.isContent(row=4, str2=r.text)

    def test_modifyNickName_005(self):
        '''测试：修改昵称'''
        r = self.meth.post3(row=6)
        print(r.text)
        self.statusCode(r)
        self.isContent(row=6, str2=r.text)

    def test_uploadPic_006(self):
        '''测试：上传图片'''
        r = self.meth.post_upload(row=7)
        # print(r.text)
        self.statusCode(r)
        self.isContent(row=7, str2=r.text)
        print(r.json()['data'])

