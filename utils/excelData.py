#!/usr/bin/python
# -*- coding:utf-8 -*-

#author:wang
"""Excel的列数"""

class excelCol:
    """获取Excel各列"""
    caseId = 0
    title = 1
    url = 3
    data = 4
    expect = 5
    result = 6


def getCaseId():
    return excelCol.caseId


def getTitle():
    return excelCol.title


def getUrl():
    return excelCol.url


def getData():
    return excelCol.data


def getExpect():
    return excelCol.expect


def getResult():
    return excelCol.result


# col = excelCol()
# col.getCaseId()