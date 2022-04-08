# -*- coding: utf-8 -*-
# @Time : 4/8/2022 12:00 AM
# @Author : SPIDEY.K
# @Email : mirrorsec@qq.com
# @File : append.py
# @Software : PyCharm
# @Project : DATA_Analysis

nameList = ['Zhang', 'Wang', 'Li']

# 增加    append
print("-----增加前的列表-------")
for names in nameList:
    print(names)

name_append = input("请输入添加学生的姓名: ")
nameList.append(name_append)    # 在末尾追加一个元素

print("------增加后的列表------")
for names in nameList:
    print(names)
