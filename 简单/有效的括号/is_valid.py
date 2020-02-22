"""
coding:utf-8
file: is_valid.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/2/22 15:48
@desc:
"""
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''


test = is_valid('[]([]){{{{{}}}}}(')
print(test)

"""
>>>False
"""
