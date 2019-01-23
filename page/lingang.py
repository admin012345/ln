#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""
面向对象：1、响应token动态参数的处理

"""
from utils.public import *
import json
from utils.operationJson import operateJson


def write_ResponseData(content):
    '''写入token、userId数据'''
    with open(base_dir('data', 'TOKEN'), 'w') as fp:
        fp.write(content)


def get_ResponseData():
    '''读取token、userId'''
    with open(base_dir('data', 'TOKEN'), 'r') as fp:
        return json.loads(fp.read())


son = operateJson()


def set_Type(type):
    '''重写requestData.json文件,sendVerifyCode数据中的“type”数据'''
    # 将“str”转化为“字典”----loads
    dic = json.loads(son.get_Result(row=3))
    dic['body']['type'] = type
    dic['body'] = json.dumps(dic['body'])
    return dic


def set_VerifyCode(verifyCode):
    '''重写requestData.json文件,forgetPassword数据中的“verifyCode”数据'''
    # 将“str”转化为“字典”----loads
    dic = json.loads(son.get_Result(row=4))
    dic['body']['verifyCode'] = verifyCode
    dic['body'] = json.dumps(dic['body'])
    return dic


def set_token_userId(row):
    '''重写requestData.json文件,modifyPassword数据中的“token、userId”数据'''
    # 将“str”转化为“字典”----loads
    dic = json.loads(son.get_Result(row=row))
    dic['token'] = get_ResponseData()[0]
    dic['body']['userId'] = get_ResponseData()[1]
    dic['body'] = json.dumps(dic['body'])
    return dic












