def count_vowels(text):
    # return sum([char in 'aąeęioóuy' for char in text ])
    return sum([1 if char in 'aeiouy' else 0 for char in text])


print(count_vowels('ala'))
print(count_vowels('programowanie'))
