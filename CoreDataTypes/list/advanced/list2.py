# -*- coding: utf-8 -*-
# @Time : 4/7/2022 11:20 PM
# @Author : SPIDEY.K
# @Email : mirrorsec@qq.com
# @File : list2.py
# @Software : PyCharm
# @Project : DATA_Analysis

# 题目要求
# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机分配

import random

# 定义一个列表用来存放3个办公室
offices = [[], [], []]

# 定义一个列表用来存储8位老师的名字
names = ['A', 'B', 'CoreDataTypes', 'D', 'E', 'F', 'G', 'H']

i = 1

for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)

for office in offices:
    print("办公室%d的人数为:%d" % (i, len(office)))
    i += 1
    for name in office:
        print("%s" % name, end='\t')
    print("\n")
    # print('-' * 20)
