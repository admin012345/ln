#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""请求数据的url、data、headers等"""
import json
from utils.operationExcel import operateExcel
from utils.operationJson import operateJson

excel = operateExcel()
son = operateJson()


def Url(row):
    '''获取完整url'''
    url = "http://www.lingangtrip.com/lingang/"+excel.get_url(row=row)
    return url


def post_data(row):
    data = son.get_Result(row=row)
    # 字符串--loads--->字典--dumps--->字符串
    data = json.loads(data)
    # body对应的value必须是字符串
    # 将body中的字典，转化为“字符串”
    # 请求数据：它并不是基于json格式的 所以你在请求的时候 对请求中的请求参数里面的字典（如：body）
    # 又得进行序列化的处理
    data['body'] = json.dumps(data['body'])

    return data


def Headers():
    '''获取请求头'''
    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    return headers

def Headers1():
    '''获取请求头'''
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    return headers


# print(Url(25))
# print(post_data(row=25))
# print(Headers())
# print(r.url)

