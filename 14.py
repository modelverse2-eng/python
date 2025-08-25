def fib_recursive(n):
    if n < 2:      # n=0 或 n=1
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)#基础








def fib_iter(n):
    if n < 2:
        return n
    a, b = 0, 1  # F(0), F(1)
    for _ in range(2, n+1):
        a, b = b, a + b
    return b #升级
