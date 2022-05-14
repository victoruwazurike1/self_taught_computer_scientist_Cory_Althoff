import math


def is_prime(n):
    # This algorithm is linear
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_eff(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % 1 == 0:
            return False
    return True


def find_primes(n):
    return [i for i in range(2, n) if is_prime(i)]


print(is_prime(7))
print(is_prime(10))
print(find_primes(50))
