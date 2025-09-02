"""给定一个长度为n整数数组nums和一个整数target，用nums找到三个整数，使总和最接近target。

返回三个整数的总和。

你可以假设每个输入正好有一个解决方案"""
"""有三个元素和求最接近值，用双指针法"""
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()#原地排序
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                # 更新最接近 target 的结果
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum

        return closest_sum
