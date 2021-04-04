sentence = input('Podaj ciąg słów i oddziel je spacją: ')
dictionary = {}

for word in sentence.split():
    if word not in dictionary:
        dictionary[word] = 0

    dictionary[word] += 1

print(dictionary)
