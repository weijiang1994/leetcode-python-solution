"""
coding:utf-8
file: 两数之和.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/2/20 14:58
@desc:
"""
"""
给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
思路:
要在列表中找到 target - i in nums,且不能使用同一个元素
nums = [3, 2, 3] target = 6
要返回[0, 3] 不能为[0, 0]
"""


def two_sum(nums, target):
    """遍历列表同时查询字典"""
    dct = {}
    for i, n in enumerate(nums):
        # 如果target - n 在字典中存在则返回对应的索引
        if target - n in dct:
            return [dct[target - n], i]
        # 记录已遍历元素的索引
        dct[n] = i


test = two_sum([3, 2, 3], 6)
print(test)

"""
>>> [0, 2]
"""