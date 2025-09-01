"""编写一个函数来查找字符串数组中最长的通用前缀字符串。 如果没有通用的前缀，请返回一个空字符串"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 如果数组为空，返回空字符串
        if not strs:
            return ""
        
        # 初始前缀就是第一个字符串
        prefix = strs[0]
        
        # 遍历数组剩余的字符串
        for s in strs[1:]:
            # 不断缩短 prefix，直到当前字符串以 prefix 开头
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # 去掉最后一个字符
                if prefix == "":
                    return ""  # 没有通用前缀
        
        return prefix
        
