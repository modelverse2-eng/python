给定一个罗马数字，将其转换为整数。




class Solution:
    def romanToInt(self, s: str) -> int:
        # 罗马数字对应的整数值
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0  # 记录上一个数字的值

        # 从右向左遍历
        for char in reversed(s): #char 是 循环变量
            value = roman_dict[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total
