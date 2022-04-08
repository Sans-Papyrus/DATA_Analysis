# -*- coding: utf-8 -*-
# @Time : 4/8/2022 5:15 PM
# @Author : SPIDEY.K
# @Email : mirrorsec@qq.com
# @File : modify.py
# @Software : PyCharm
# @Project : DATA_Analysis

nameList = ['Zhang', 'Wang', 'Li']

print("------更改前的列表------")

for names in nameList:
    print(names)

nameList[2] = "Han"     # 通过下标修改元素内容

print("------更改后的列表------")
for names in nameList:
    print(names)