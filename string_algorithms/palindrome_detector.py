from audioop import reverse


# Note that the run time to reverse a list is O(n)
def is_palindrome(string):
    if string.lower() == string[::-1].lower():
        return True
    else:
        return False


print(is_palindrome('hannah'))
