"""
coding:utf-8
file: reverse.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/2/20 16:41
@desc:
"""
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
思路:
先判断整数是正数还是负数
然后转换为字符串进行取反操作
"""


def reverse(x: int) -> int:
    flag = -1 if x < 0 else 1
    res = flag * int(str(abs(x))[::-1])
    return res if (-2 ** 31) <= res <= (2 ** 31 - 1) else 0


test = reverse(-121131)
print(test)

"""
>>> -131121
"""