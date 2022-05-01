import string


def binary_search(a_list, letter):
    first = 0
    last = len(a_list) - 1
    target = ord(letter)
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == letter:
            return True
        else:
            if target > ord(a_list[mid]):
                first = mid + 1
            else:
                last = mid - 1
    return False


alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)


print(binary_search(alphabet_list, 'm'))
