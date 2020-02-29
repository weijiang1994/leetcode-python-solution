"""
coding:utf-8
file: str_Str.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/2/29 17:45
@desc:
"""
"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1。

"""


def str_str(haystack: str, needle: str) -> int:
    """ 双指针O(m*n)超时，优化如下 """
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1
    from collections import Counter
    haystack_dict = Counter(haystack)
    needle_dict = Counter(needle)
    for key in needle_dict:
        if key in haystack_dict and needle_dict[key] <= haystack_dict[key]:
            pass
        else:
            return -1
        
    # 避免 needle 太长
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


test = str_str('hello', 'll')
print(test)
