__author__ = 'demi'


cache = {
    0 : 0,
    1 : 1
}
def fibonacci(n):
    if n in cache:
        return cache[n]
    else:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            res = fibonacci(n - 1) + fibonacci(n-2)
            cache[n] = res
            return res

print(fibonacci(36))
#>>> 14930352

# solution from Udacity from Dave
def fib(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

print(fib(36))
#>>> 14930352


def fib(n):
    current = 0
    after = 1
    sum = 0
    for i in range(0, n):
        current, after = after, current + after
        if current % 2 != 0:
            sum += current
    return sum

def test():
    sum = 0
    for i in range(1000):
        if i % 2 != 0:
            sum += 1000
    return sum

print(fib(1000))