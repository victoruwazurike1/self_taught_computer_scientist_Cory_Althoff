def check_parentheses(a_string):
    stack = []
    for c in a_string:
        if c == '(' or '[':
            stack.append(c)
        if c == ')' or '[':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


test_string = '[]('
print(check_parentheses(test_string))
