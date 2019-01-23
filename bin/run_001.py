#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""执行所有测试用例",生成html报告"""
import unittest
import os
import time
import HTMLTestRunner
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")


"""运行所有测试用例"""

def allTests():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test'),
        pattern='test*.py',
        top_level_dir=None)
    return suite


def getTime():
    return time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))


def run():
    # 在Day04--->report下--->报告名称
    fp = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', getTime()+"reportTest.html")
    # print fp
    HTMLTestRunner.HTMLTestRunner(stream=open(fp, 'wb'),
                                  title=u"测试报告",
                                  description=u"测试报告详情").run(allTests())


if __name__ == "__main__":
    run()

