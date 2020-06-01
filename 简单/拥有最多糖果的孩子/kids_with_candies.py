"""
给你一个数据candies 和一个整数extraCandies,其中candies[i]表示第i个孩子的糖果数.
对每一个孩子,检查是否存在一种方案,将额外的extraCandies个糖果分配给孩子们之后,此孩子拥有最多的的糖果.注意:允许有多个孩子同时拥有最多的糖果数目.
"""
class Solution:
	def kids_with_candies(candies, extra_candies):
		ret = list()
		if len(candies) in [0, 1]:
			return [True]
		for candy in candies:
			if candy + extra_candies >= max(candies):
				ret.append(True)
			else:
				ret.append(False)
		return ret
