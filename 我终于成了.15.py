class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        left, right = 0, m
#这一模块的功能是寻找短数组ps：不要被half-len给影响了注意力
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            max_left2 = nums2[j-1] if j>0 else float('-inf')
            min_right2 = nums2[j] if j<n else float('inf')
            max_left1 = nums1[i-1] if i>0 else float('-inf')
            min_right1 = nums1[i] if i<m else float('inf')
#这一模块是定义断点和利用中位数自身性质来判定中位数
            if max_left1 <= min_right2 and max_left2 <= min_right1:#判定
                if (m+n) % 2 == 1:#判断合并后数组长度是奇数还是偶数
                    return max(max_left1, max_left2)
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            elif max_left1 > min_right2:
                right = i - 1
            else:
                left = i + 1#每次循环通过判断切口是否合法，如果不合法就调整搜索区间
