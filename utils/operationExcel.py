#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""
操作接口Excel表：1、读取Excel表数据
                 2、操作、重写
                 3、关闭
"""


import xlrd
from xlutils.copy import copy
from utils.public import *
from utils.excelData import *


class operateExcel:
    # def __init__(self):
    #     self.excelCol = excelCol()

    def getOpen(self):
        '''打开Excel表'''
        open = xlrd.open_workbook(base_dir('data', 'Data.xls'))
        index = open.sheet_by_index(0)
        return index

    def getRow(self):
        '''获取行数'''
        return self.getOpen().nrows

    def getCell(self, row, col):
        '''获取单元格值'''
        return self.getOpen().cell_value(row, col)

    def get_caseId(self, row):
        '''获取单元格的值：列固定，行变化'''
        return self.getCell(row, getCaseId())

    def get_title(self, row):
        return self.getCell(row, getTitle())

    def get_url(self, row):
        return self.getCell(row, getUrl())

    def get_data(self, row):
        return self.getCell(row, getData())

    def get_expect(self, row):
        return self.getCell(row, getExpect())

    def get_result(self, row):
        return self.getCell(row, getResult())

    def writeExpect(self, row, content):
        '''
        把结果写入data表的result列中
        【注意】将文件提前复制一份，以防在写入时报错
        '''
        col = getExpect()
        work = xlrd.open_workbook(base_dir("data", "Data.xls"))
        old_content = copy(work)
        ws = old_content.get_sheet(0)
        ws.write(row, col, content)
        old_content.save(base_dir("data", "Data.xls"))

    def get_success(self):
        '''获取成功的个数'''
        count_success = []
        count_false = None
        for i in range(1, self.get_row()):
            if self.get_result(i) == 'Pass':
                count_success.append(self.get_result(i))
        # print(len(count_success))
        return int(len(count_success))

    def get_false(self):
        '''获取失败的个数:失败个数=总数-成功个数'''
        # print((self.get_row()-1)-self.get_success())
        return (self.get_row()-1)-self.get_success()

    def get_pass_rate(self):
        '''通过率=成功个数/总个数*100'''
        rate = ''
        if self.get_false() == 0:
            rate = '100%'
        elif self.get_false() !=0:
            rate = str(int(self.get_success()/(self.get_row()-1)*100))+'%'
        print(rate)




# oe = operateExcel()
# print(oe.get_data(16))