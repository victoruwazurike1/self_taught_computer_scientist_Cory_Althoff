an_array = [8, 5, 3, 10, 12]
evens = []
odds = []

for i in an_array:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)


new_array = evens + odds
print(new_array)
