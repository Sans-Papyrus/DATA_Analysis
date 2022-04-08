# -*- coding: utf-8 -*-
# @Time : 4/8/2022 12:05 AM
# @Author : SPIDEY.K
# @Email : mirrorsec@qq.com
# @File : del.py
# @Software : PyCharm
# @Project : DATA_Analysis

# del 删除

movieName = ['指环王', '第一滴血', '骇客帝国', '泰塔尼克号']

print("------删除前的列表-------")
for names in movieName:
    print(names)

del movieName[2]    # del 指定下标删除元素

print("-----删除后的列表------")
for names in movieName:
    print(names)
