# -*- coding: utf-8 -*-
# @Time : 4/9/2022 12:30 AM
# @Author : SPIDEY.K
# @Email : mirrorsec@qq.com
# @File : append.py
# @Software : PyCharm
# @Project : DATA_Analysis

tup1 = (12, 34, 56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是违法的
# tup1[0] = 100
# print(tup1[0])

# 创建一个新元组

tup3 = tup1 + tup2
print(tup3)
