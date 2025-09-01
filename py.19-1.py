"""给定一个输入字符串 s 和一个模式 p，实现正则表达式匹配，支持以下规则：
. 匹配 任意单个字符
* 匹配 前一个元素的零次或多次
匹配必须覆盖 整个输入字符串（不能只匹配一部分"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # 创建集合（状态集合）
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True  # 空字符串匹配空模式
        
        # 初始化空字符串匹配模式时的桶（处理'*'能匹配0次）
        for j in range(2, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # 创建虚拟桶 + 归类
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (p[j-2] == '.' or p[j-2] == s[i-1]))
        
        return dp[m][n]
