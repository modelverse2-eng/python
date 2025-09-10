
“”“给定两个整数dividend数和divisor，在不使用乘法、除法和mod运算符的情况下除两个整数。

整数除法应该截断为零，这意味着失去其小数部分。例如，8.345将被截断为8，-2.7335将被截断为-2。

除dividend后返回商。

”“”


“”“思路：先处理符号，加入递归（每减一次商就加一），返回商“”“





def divide_recursive(dividend, divisor):
    if divisor == 0:
        raise ValueError("除数不能为0")
    
    # 处理符号
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    
    # 转为正数处理
    dividend, divisor = abs(dividend), abs(divisor)
    
    # 递归函数
    def helper(dividend, divisor):
        # 终止条件
        if dividend < divisor:
            return 0
        # 被除数至少可以减一次除数
        return 1 + helper(dividend - divisor, divisor)
    
    return sign * helper(dividend, divisor)

    
