“”“给定n对括号，编写一个函数来生成所有形成良好的括号的组合”“”


“”“思路：用树的每个节点表示当前括号组合状态，通过添加 '(' 或 ')' 分支生成决策树，叶子节点收集的字符串就是所有合法组合“”“


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateParenthesis(n):
    res = []

    def dfs(path, left, right):
        """
        path: 当前生成的括号字符串
        left: 剩余可用左括号 '('
        right: 剩余可用右括号 ')'
        """
        # 叶子节点：左右括号都用完
        if left == 0 and right == 0:
            res.append(path)
            return

        # 可以添加左括号
        if left > 0:
            dfs(path + "(", left - 1, right)

        # 可以添加右括号（保证右括号数大于左括号数，保持合法）
        if right > left:
            dfs(path + ")", left, right - 1)

    # 从树根开始遍历
    dfs("", n, n)
    return res
