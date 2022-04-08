# -*- coding: utf-8 -*-
# @Time : 4/7/2022 10:12 PM
# @Author : SPIDEY.K
# @Email : mirrorsec@qq.com
# @File : str1.py
# @Software : PyCharm
# @Project : DATA_Analysis

str1 = "zhang"

print(str1)  # 输出字符串
print(str1[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str1[0])  # 输出字符串第一个字符
print(str1[2:5])  # 输出第三个到第五个字符
print(str1[2:])  # 输出从第三个开始后的所有字符
print(str1 * 2)  # 输出字符串两次
print("hello" + str1)  # 连接字符串
print(str1[:5])  # 输出第五个字母前的所有字母
print(str1[0:5:2])  # [初值:终值:步长]

print('-' * 20)

print('hello\nzhang')  # \n表示转义换行
print(r'hello\nzhang')  # 在字符串前面加r,表示源字符串,不会发生转义
