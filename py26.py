“”“26.从排序数组中删除重复
简单

话题
高级锁图标
公司

提示
给定一个按非减少顺序排序的整数数组nums，就地删除重复项，以便每个唯一元素只出现一次。元素的相对顺序应该保持不变。然后返回以nums为单位的唯一元素的数量。

认为nums的唯一元素的数量是k，为了被接受，您需要做以下事情：

更改数组nums，使nums的前k个元素按照最初在nums中存在的顺序包含唯一元素。nums的剩余元素与nums的大小一样不重要。
返回k。
“”“

“”“思路：先用f指针找不同元素再用s指针覆盖，最后返回slow + 1"""








from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1
