def factorial_iter(n):
    the_product = 1
    while n > 0:
        the_product *= n
        n = n - 1
    return the_product


def factorial_recur(n):
    if n == 0:
        return 1
    return n * factorial_recur(n-1)


print(factorial_iter(5))
