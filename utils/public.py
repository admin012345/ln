#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""
公共方法：1、文件路基
          2、Excel的列数
"""


import os


def base_dir(package='data', filename=None):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), package, filename)




