“”“给定一个长度为n整数数组nums和一个整数target，用nums找到三个整数，使总和最接近target。

返回三个整数的总和。

你可以假设每个输入正好有一个解决方案。”“”

“”“思路： 排序 + 双指针：先将数组排序，然后固定一个数字，用双指针找剩余两个数字，使三数之和最接近目标

详细：1，对数组进行原地排序，保证有序，方便双指针移动和判断
     2，用前三个元素之和作为初始最接近值 closest_sum
     3，将每个元素作为三数之
     4，双指针寻找剩余两数，左指针 left 从 i+1 开始，右指针 right 从数组末尾开始，计算当前三数之和 curr_sum，根据 curr_sum 与目标值比较，移动指针curr_sum<target指针右移，>时左移，=时找到最优解
     5，遍历结束后，返回最接近目标的三数之和



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
