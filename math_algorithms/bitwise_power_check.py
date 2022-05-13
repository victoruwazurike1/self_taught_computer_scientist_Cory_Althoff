def is_power(n):
    if n & (n - 1) == 0:
        return True
    return False


print(is_power(8))
print(is_power(64))
print(is_power(7))
print(is_power(63))
