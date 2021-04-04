word1 = input('Podaj słowo: ')
word2 = input('Podaj kolejne: ')
wset1 = set()
wset2 = set()

for char in word1:
    wset1.add(char)
for char in word2:
    wset2.add(char)

print(wset1 & wset2)
