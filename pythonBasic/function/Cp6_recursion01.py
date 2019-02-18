
# 非递归实现阶乘
def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

# 递归实现阶乘
def factorialrec(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# 非递归实现指数幂
def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

# 递归实现指数幂
def powerrec(x, n):
    if n == 0:
        return 1
    else:
        return x * powerrec(x,n-1)