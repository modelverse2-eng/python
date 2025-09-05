"""给定一个仅包含字符'('、')'、'{'、'}'、'['和']'的字符串s，确定输入字符串是否有效。

如果出现以下条件，输入字符串是有效的：

打开的括号必须由相同类型的括号关闭。
打开的括号必须按正确的顺序关闭。
每个闭括号都有一个相应的相同类型的开括号。
"""


"""思路：已知同侧字符不会比对只用比对异侧字符，利用题目给的条件确定要用到 栈 用他后进先出的性质进行比对，1，定义栈和字符对应的字符，2，排除单独出现的右侧字符用栈的性质来进行字符的比对 3，检测最后的栈是否为空
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  # 如果是右括号
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:  # 如果是左括号
                stack.append(char)

        return not stack  # 栈为空才是有效的
