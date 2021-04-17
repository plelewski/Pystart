def fib(n):
    if n <= 1:
        return n
    return fib(n-2) + fib(n-1)


def fib_sum(n):
    return sum([fib(i) for i in range(n+1)])


print(fib_sum(5))