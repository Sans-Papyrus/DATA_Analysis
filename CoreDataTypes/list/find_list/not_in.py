# -*- coding: utf-8 -*-
# @Time : 4/8/2022 5:21 PM
# @Author : SPIDEY.K
# @Email : mirrorsec@qq.com
# @File : not_in.py
# @Software : PyCharm
# @Project : DATA_Analysis

nameList = ['Zhang', 'Wang', 'Li']

findName = input("请输入你要查找的内容: ")

if findName not in nameList:
    print(True)
else:
    print(False)
