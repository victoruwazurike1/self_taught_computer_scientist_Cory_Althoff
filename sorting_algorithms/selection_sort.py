def selection_sort(a_list):
    for i in range(len(a_list)):
        min_index = i
        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[min_index]:
                min_index = j
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]
    return a_list


a_list = [5, 2, 8, 4]
print(selection_sort(a_list))
