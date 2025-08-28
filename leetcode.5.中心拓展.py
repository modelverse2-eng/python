class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 辅助函数：从 x,y 作为中心向两边扩展
        def expand(x, y):
            while x >= 0 and y < len(s) and s[x] == s[y]:
                x -= 1
                y += 1
            return s[x+1:y]  # x先走，所以要 +1

        pack = ""
        for i in range(len(s)):
            # 情况1：以一个字符为中心（奇数回文）
            odd = expand(i, i)
            # 情况2：以两个字符之间为中心（偶数回文）
            even = expand(i, i+1)

            # 更新最长回文
            if len(odd) > len(pack):
                pack = odd
            if len(even) > len(pack):
                pack = even

        return pack
