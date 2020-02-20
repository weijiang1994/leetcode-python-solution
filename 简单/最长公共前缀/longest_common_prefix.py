"""
coding:utf-8
file: longest_common_prefix.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/2/20 18:32
@desc:
"""
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
思路:
使用Python中的min()和max()函数找出list中最小值与最大值
min()函数的用法,除了数字的排序还可以对字母进行排序
ls = ['bcd', 'acd', 'aed']
min(ls)>>>'acd'
将list中的元素按位进行比较,max()函数同理
"""


def longest_common_prefix(strings):
    if not strings:
        return ""
    s1 = min(strings)
    s2 = max(strings)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1


print(longest_common_prefix(["flower", "flow", "flight"]))
"""
>>> fl
"""