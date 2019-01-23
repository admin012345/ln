#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""
操作json文件，与Excel文件关联
1、读区json文件
2、操作
3、关联
"""
import json
from utils.public import *
from utils.operationExcel import operateExcel


class operateJson:
    def __init__(self):
        self.excel = operateExcel()

    def get_ReadJson(self):
        '''读取requestData的json文件'''
        with open(base_dir(filename='requestData.json'), 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    def get_Result(self, row):
        '''requestData的json文件和Excel关联起来，通过“data”数据'''
        return json.dumps(self.get_ReadJson()[self.excel.get_data(row=row)])


# oj = operateJson()
# print(oj.get_ReadJson()['queryGardenList'])
# print(oj.get_Result(16))