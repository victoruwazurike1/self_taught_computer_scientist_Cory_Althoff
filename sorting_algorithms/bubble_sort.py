# Because a bubble sort uses two nested loops, the
# time complexity is O(n ** 2)
# Bubble sort is a stable sorting algorithm
def bubble_sort(a_list):
    list_length = len(a_list) - 1
    for i in range(list_length):
        for j in range(list_length):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list


a_list = [5, 2, 8, 4]
print(bubble_sort(a_list))
