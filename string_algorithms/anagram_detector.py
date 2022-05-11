# The time complexity for this function is O(nlogn)

def is_anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


print(is_anagram('scar', 'cars'))
