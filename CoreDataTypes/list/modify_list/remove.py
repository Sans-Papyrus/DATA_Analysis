# -*- coding: utf-8 -*-
# @Time : 4/8/2022 5:09 PM
# @Author : SPIDEY.K
# @Email : mirrorsec@qq.com
# @File : remove.py
# @Software : PyCharm
# @Project : DATA_Analysis

movieName = ['指环王', '第一滴血', '骇客帝国', '泰塔尼克号']
print("------删除前的列表------")
for names in movieName:
    print(names)
movieName.remove('骇客帝国')    # remove删除指定元素
print("------删除后的列表------")
for names in movieName:
    print(names)