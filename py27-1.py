“”“给定两个整数dividend数和divisor，在不使用乘法、除法和mod运算符的情况下除两个整数。

整数除法应该截断为零，这意味着失去其小数部分。例如，8.345将被截断为8，-2.7335将被截断为-2。

除dividend后返回商“”“



”“”思路：除零检查，确定符号，取绝对值计算，初始化商，内外循环，扣掉最大块并累加商，加上符号返回结果“”“










def divide(dividend, divisor):
    """
    实现整数除法（向零截断），不使用 *, /, % 运算符
    返回商
    """
    if divisor == 0:
        raise ValueError("除数不能为0")

    # 处理符号
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    # 取绝对值计算
    a, b = abs(dividend), abs(divisor)
    quotient = 0

    # 外层循环：只要被除数 >= 除数
    while a >= b:
        temp = b
        multiple = 1

        # 内层循环：倍增除数，直到超过被除数
        while temp + temp <= a:  # temp*2 可用 temp+temp 替代
            temp += temp
            multiple += multiple

        a -= temp
        quotient += multiple

    # 根据符号返回结果
    if sign == -1:
        return -quotient
    else:
        return quotient
