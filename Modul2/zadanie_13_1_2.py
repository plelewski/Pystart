word1 = input('Podaj pierwsze słowo: ')
word2 = input('Podaj drugie słowo: ')

lword1 = set(word1.lower())
lword2 = set(word2.lower())

print('Zbiór niepowtarzających się znaków', lword1 ^ lword2)

# lepszy sposób
print(set(word1.lower()) ^ set(word2.lower()))
