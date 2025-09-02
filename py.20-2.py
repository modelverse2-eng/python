"""给定一个包含2-9（含）数字的字符串，返回数字可以代表的所有可能的字母组合。以任何顺序返回答案。

下面给出了数字到字母的映射（就像电话按钮一样）。请注意，1不会映射到任何字母。
"""


"""他都给我映射关系了我还动啥脑子，直接if"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 数字到字母的映射
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # 先用第一个数字初始化结果
        res = list(mapping[digits[0]])

        # 从第二个数字开始，依次组合
        for d in digits[1:]:
            temp = []
            for prefix in res:            # 已经组合好的前缀
                for c in mapping[d]:      # 当前数字对应的字母
                    temp.append(prefix + c)  # 拼接成新的组合
            res = temp  # 更新结果

        return res
