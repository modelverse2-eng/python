def fib_recursive(n):
    if n < 2:      # n=0 或 n=1
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)#基础    每次调用函数去计算 n-1 和 n-2，然后相加得到 F(n)








def fib_iter(n):
    if n < 2:
        return n
    a, b = 0, 1  # F(0), F(1)。  a 表示当前的 F(n-2)，初始是 F(0) = 0  b 表示当前的 F(n-1)，初始是 F(1) = 1
    for _ in range(2, n+1):#_ 是循环变量
        a, b = b, a + b#Python 同时赋值。   会先计算右边，再一起赋值
    return b #升级
