class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数或者末尾为0但不是0本身，直接不是回文
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10

        # 偶数位或奇数位回文
        return x == reversed_half or x == reversed_half // 10
