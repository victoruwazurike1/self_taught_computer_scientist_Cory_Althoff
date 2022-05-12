# The time complexity for this is O(n)
s = 'Buy 1 get 2 free'

last_digit = [c for c in s if c.isdigit()][-1]

print(last_digit)
