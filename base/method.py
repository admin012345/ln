#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""request的get或post请求"""
import requests
from base.request import *
from page.lingang import *
from page.LG_travel import *


class methon:
    def post(self, row):
        '''post 请求'''
        try:
            r = requests.post(
                url=Url(row=row),
                data=post_data(row=row),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post1(self, row, type=None):
        '''
        :param type: 1表示注册时,3表示忘记密码时
        '''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_Type(type=type),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post2(self, row, verifyCode=None):
        '''
        :param verifyCode: 手机发送的验证码
        '''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_VerifyCode(verifyCode=verifyCode),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post3(self, row):
        '''post 请求,动态参数token、userId'''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_token_userId(row=row),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post4(self, row, scenicType):
        '''
        :param scenicType: 场景类型(1景点2公园)
        '''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_scenicType(scenicType=scenicType),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post5(self, row, tags=None, orderby=None, lon=None, lat=None):
        '''
        :param tags: 筛选项(多个用逗号隔开)
        :param orderby::排序方式---1推荐2评级3距离
        :param lon: 经度(如果orderby是3必须传)
        :param lat: 纬度如果orderby是3必须传)
        '''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_TOLL(tags=tags, orderby=orderby, lon=lon, lat=lat),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post6(self, row, scenicId):
        '''
        :param scenicId:场景ID
        '''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_scenicId(scenicId=scenicId),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post7(self, row, scenicType, comment, starNum, scenicId):
        '''
        :param scenicType:场景类型(1景区,2公园)
        :param comment:评论内容
        :param starNum:星级
        :param scenicId: 场景ID
        '''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_SCSS(scenicType, comment, starNum, scenicId),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post8(self, row, lon, lat, words=None):
        '''
        :param words: 查询关键字
        :param lon: 经度
        :param lat: 纬度
        '''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_WLL(row=row, lon=lon, lat=lat, words=words),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post9(self, row, type):
        '''
        :param type: 公告类型(1后台通知2交通推送信息)
        '''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_Type(type=type),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post10(self, row, words, sort):
        '''
        :param words:搜索关键词
        :param sort:排序方式
        '''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_WS(words=words, sort=sort),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post11(self, row, travelId):
        '''TravelId:游记id'''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_TravelId(row, travelId),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post12(self, row, travelId, title, content):
        '''
        :param travelId: 游记id------title和content必须至少有一个
        :param title: 标题
        :param content:内容
        '''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_TTC(row, travelId, title, content),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post13(self, row, travelId):
        '''TravelId:游记id'''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_MyTravelId(row, travelId),
                headers=Headers())
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    def post_upload(self, row):
        '''图片上传'''
        try:
            r = requests.post(
                url=Url(row=row),
                data=set_token_userId(row=row),
                # headers={'Content-Type': 'multipart/form-data'},
                files={"filename": ("1.jpg", open("E:\\2018.6.21\\Python\\FIDA\\data\\1.jpg", "rb"), "image/jpeg", {})})
            return r
        except Exception as e:
            raise RuntimeError('post请求接口出现未知错误')

    # def post_Travel(self, row, content, coverPic, title):
    #     '''
    #     发布游记
    #     :param content: 内容
    #     :param coverPic: 封面图片
    #     :param title: 标题
    #     '''
    #     try:
    #         r = requests.post(
    #             url=Url(row=row),
    #             data=set_CCT(row, content, coverPic, title)
    #             # files={"coverPic": ("1.jpg", open(base_dir('data', '1.jpg'), "rb"), "image/jpeg")}
    #             )
    #         return r
    #     except Exception as e:
    #         raise RuntimeError('post请求接口出现未知错误')


# me = methon()
# print(me.post(10).url)
# print(me.post(10).text)
# # print(set_Type(3))
# print(me.post_upload(7).url)
# print(me.post_upload(7).text)