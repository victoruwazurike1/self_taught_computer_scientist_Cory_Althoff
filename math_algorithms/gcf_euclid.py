# The time complexity is logarithmic compared to the other algorithm
def gcf(x, y):
    if y == 0:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


print(gcf(12, 20))
