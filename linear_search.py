def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False


a_list = [1, 8, 32, 91, 5, 19, 9, 100, 3]

print(linear_search(a_list, 91))
