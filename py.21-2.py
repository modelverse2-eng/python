from typing import List

class Solution:
    def nSum(self, nums: List[int], target: int, n: int) -> List[List[int]]:
        """
        通用 n 数之和函数
        nums: 待处理数组
        target: 目标和
        n: 需要组合的数字个数
        """
        nums.sort()  # 排序数组，方便去重和双指针处理
        return self._nSum(nums, target, n)

    def _nSum(self, nums: List[int], target: int, n: int) -> List[List[int]]:
        """
        递归函数实现 n 数之和
        nums: 当前子数组
        target: 当前目标和
        n: 当前需要组合的数字个数
        """
        res = []  # 用于存放结果列表
        length = len(nums)
        
        # 边界条件：数组长度不足 n 或 n 小于 2
        if length < n or n < 2:
            return res

        # Base case: n == 2，使用双指针解决两数之和
        if n == 2:
            left, right = 0, length - 1
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    res.append([nums[left], nums[right]])  # 找到符合条件的组合
                    # 去重 left：跳过相同的值
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 去重 right：跳过相同的值
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1  # 总和小于目标，左指针右移
                else:
                    right -= 1  # 总和大于目标，右指针左移
        else:
            # n > 2 时，递归求 n-1 数之和
            for i in range(length - n + 1):  # 遍历数组，固定第一个数
                if i > 0 and nums[i] == nums[i - 1]:
                    continue  # 去重：跳过重复的固定数
                # 递归调用：在剩下的数组里寻找 n-1 数之和
                sub_res = self._nSum(nums[i + 1:], target - nums[i], n - 1)
                # 将固定的 nums[i] 添加到子结果前面
                for subset in sub_res:
                    res.append([nums[i]] + subset)

        return res
