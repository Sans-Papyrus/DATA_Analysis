# -*- coding: utf-8 -*-
# @Time : 4/7/2022 10:51 PM
# @Author : SPIDEY.K
# @Email : mirrorsec@qq.com
# @File : list1.py
# @Software : PyCharm
# @Project : DATA_Analysis

# 列表的嵌套
# 一个列表中的元素又是一个元素，那么这就是列表的嵌套

schoolNames = [['北京大学', '武汉大学'], ['清华大学', '南开大学', '武汉大学'],
               ['天津大学'], ['郑州大学'], ['河南大学'],
               ['中南大学'], ['西安交通大学']]

for names in schoolNames:
    print(names)
