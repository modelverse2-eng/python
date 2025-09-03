"""给定一个由n个整数組成的数组nums，返回一个由所有唯一的四元组[nums[a], nums[b], nums[c], nums[d]]的数组，这样：

0 <= a, b, c, d < n
a、b、c和d是不同的。
nums[a] + nums[b] + nums[c] + nums[d] == target
您可以按任何顺序返回答案。"""



"""思路：将4分解成1+3。 也就是说在a b c d 中先把 a 单独放出来做成一个最外层的for循环，然后再在a循环中加入双指针算法去计算 b c d 再给通篇代码都加入 去重 代码就能得到结果"""
"""关于a循环：代码和双指针法里固定b的代码几乎一样“”“
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()  # 先排序，方便双指针和去重
        n = len(nums)

        # 第一层循环：固定第一个数
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # 去重：避免第一个数重复

            # 第二层循环：固定第二个数
            for j in range(i+1, n - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue  # 去重：避免第二个数重复

                # 第三层：双指针寻找剩下两个数
                left, right = j+1, n-1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # 去重：跳过相同的第三个数
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        # 去重：跳过相同的第四个数
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1

                        # 移动指针到下一个不同的数
                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1  # 和太小，左指针右移
                    else:
                        right -= 1  # 和太大，右指针左移

        return res
     
