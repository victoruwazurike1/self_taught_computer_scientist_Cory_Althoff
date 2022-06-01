a_string = 'Victor'
# print(a_string[::-1])

b_string = 'Onyinyechi'
# print(''.join(reversed(b_string)))


def reverse_string(a_string):
    stack = []
    string = ''
    for c in a_string:
        stack.append(c)
    for c in a_string:
        string += stack.pop()
    return string


print(reverse_string('Bieber'))
