# -*- coding: utf-8 -*-
# @Time : 4/8/2022 5:18 PM
# @Author : SPIDEY.K
# @Email : mirrorsec@qq.com
# @File : in.py
# @Software : PyCharm
# @Project : DATA_Analysis

nameList = ['Zhang', 'Wang', 'Li']

findName = input("请输入你要查找的名字: ")

if findName in nameList:
    print("查找到列表中元素")
else:
    print("没有查找到!")
