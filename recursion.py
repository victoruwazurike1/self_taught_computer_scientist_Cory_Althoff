# python program to print 1 to n

def printNumber(n):
    # Check if n is greater than 0
    if n > 0:
        # recursively call the printNumber function
        printNumber(n - 1)
        # print n
        print(n, end=' ')


n = 10

print(printNumber(n))
