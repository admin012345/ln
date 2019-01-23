#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""断言"""
from utils.operationExcel import operateExcel


class Assert:
    '''断言'''
    def __init__(self):
        self.excel = operateExcel()

    def isAssert(self, row, str2):
        '''判断：row是否在str2中'''
        flag = None
        if self.excel.get_expect(row=row) in str2:
            flag = True
        else:
            flag = False
        return flag

    def isTure(self, row, duanyan):
        '''判断：如果断言正确，写入pass；如果断言失败，写入failed'''
        if duanyan == True:
            self.excel.writeResult(row=row, content='Pass')
        elif duanyan == False:
            self.excel.writeResult(row=row, content='False')