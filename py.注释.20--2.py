“”“给定一个包含2-9（含）数字的字符串，返回数字可以代表的所有可能的字母组合。以任何顺序返回答案。

下面给出了数字到字母的映射（就像电话按钮一样）。请注意，1不会映射到任何字母。“”“

”“”思路：
迭代组合法：从第一个数字开始，逐步将后续数字对应的字母与已有组合拼接，最终得到所有可能组合。
具体：
1，处理特殊情况，如果输入为空，直接返回空列表。
2，建立数字到字母的映射，使用字典存储数字与对应字母的关系（如 "2":"abc"）。
3，初始化结果，用第一个数字对应的字母列表作为初始组合。
4，依次组合后续数字，对每个已有组合，将当前数字对应的每个字母拼接成新的组合。
5，更新组合结果，继续下一轮。
6，返回最终结果
7，遍历完成后，得到所有可能的字母组合
“”“

rom typing import List

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
