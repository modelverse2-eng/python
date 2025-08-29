给定一个 有符号 32 位整数 x，返回 它的数字反转后的整数。
如果反转后的整数超出了 有符号 32 位整数范围 [-2³¹, 2³¹ - 1]，则返回 0





class Solution:
    def reverse(self, x: int) -> int:
        # 1. 取绝对值并转字符串
        s = str(abs(x))
        # 2. 反转字符串
        rev_s = "".join(reversed(s)) #join() 方法把迭代器里的字符拼接成一个新的字符串。
        # 3. 转回整数
        rev_x = int(rev_s)
        # 4. 保留符号
        if x < 0:
            rev_x = -rev_x
        # 5. 检查是否溢出 32 位整数范围
        if rev_x < -2**31 or rev_x > 2**31 - 1:
            return 0
        return rev_x
