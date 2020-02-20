"""
coding:utf-8
file: is_palindrome.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/2/20 18:08
@desc:
"""
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
思路:
先将数字转换为字符串判断第一个与最后一个是否相等,使用递归判断去掉首尾数字的序列
"""


def is_palindrome(x):
    x = str(x)
    if len(x) == 1 or len(x) == 0:
        return True
    if x[0] == x[-1]:
        return is_palindrome(x[1:len(x) - 1])
    else:
        return False


test = is_palindrome(221122)
print(test)
"""
>>>True
"""

test = is_palindrome(14565411)
print(test)
"""
>>>False
"""