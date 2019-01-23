#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""执行所有测试用例，发送email邮件"""


import HTMLTestRunner
import unittest
import os
import smtplib
from email.mime.text import MIMEText
from utils.operationExcel import operateExcel


class run(unittest.TestCase):
    def __init__(self):
        self.excel = operateExcel()

    def getSuite(self):
        '''获取所有测试套件'''
        suite = unittest.TestLoader().discover(
            start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test'),
            pattern='test*.py',
            top_level_dir=None)
        return suite

    def sent_mail(self, to_user, sub, content):
        '''
        发送邮件内容
        :param to_user: 发送邮件的人
        :param sub: 主题
        :param content: 邮件内容
        '''
        global send_mail
        global send_user
        send_mail = 'smtp.sina.cn'
        send_user = 'wuya1303@sina.com'
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = send_user
        message['To'] = to_user
        server = smtplib.SMTP()
        server.connect(send_mail)
        server.login('wuya1303@sina.com', 'admin123')
        server.sendmail(send_user, to_user, message.as_string())
        server.close()

    def main_run(self):
        '''批量运行测试用例'''
        unittest.TextTestRunner().run(self.getSuite())
        content = '通过数：{0}，失败数：{1}，通过率：{2}'.format(
            self.excel.get_success(),
            self.excel.get_false(),
            self.excel.get_pass_rate())
        print('Please wait while the statistics test results are senting in the mail')
        self.sent_mail('liwanping@parkingwang.xon', '接口自动化测试报告', content)


if __name__ == '__main__':
    run().main_run()

