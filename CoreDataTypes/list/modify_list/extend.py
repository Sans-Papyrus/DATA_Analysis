# -*- coding: utf-8 -*-
# @Time : 4/8/2022 12:02 AM
# @Author : SPIDEY.K
# @Email : mirrorsec@qq.com
# @File : extend.py
# @Software : PyCharm
# @Project : DATA_Analysis


a = [1, 2]
b = [3, 4]
a.append(b)  # 将列表当作一个元素假如到a列表中
print(a)
a.extend(b)  # 将列中中的每一个元素逐一追加到a列表中
print(a)
