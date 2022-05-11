from audioop import reverse


def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


print(is_palindrome('hannah'))
