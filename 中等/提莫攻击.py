"""
coding:utf-8
file: 提莫攻击.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/10 22:30
@desc:
"""
'''
在《英雄联盟》的世界中，有一个叫 “提莫” 的英雄，他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。
现在，给出提莫对艾希的攻击时间序列和提莫攻击的中毒持续时间，你需要输出艾希的中毒状态总时长。

你可以认为提莫在给定的时间点进行攻击，并立即使艾希处于中毒状态。
'''


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        i = 0
        ret = 0
        if len(timeSeries) == 0:
            return 0
        while i < len(timeSeries) - 1:
            if timeSeries[i + 1] - timeSeries[i] < duration:
                ret += timeSeries[i + 1] - timeSeries[i]
            else:
                ret += duration
            i = i + 1
        ret += duration
        return ret
