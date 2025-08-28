class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 特殊情况：只有一行或行数大于字符串长度，直接返回原字符串
        if numRows == 1 or numRows >= len(s):
            return s

        # 创建一个列表，每个元素存一行的字符
        rows = [''] * numRows
        curRow = 0          # 当前行
        goingDown = False   # 控制方向：向下或向上斜

        # 遍历字符串的每个字符
        for c in s:
            rows[curRow] += c
            # 到顶部或底部时，改变方向
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            # 根据方向移动行号
            curRow += 1 if goingDown else -1

        # 拼接所有行得到最终结果
        return ''.join(rows)
