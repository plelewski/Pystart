words = [input('Podaj pierwsze słowo: '), input('Podaj drugie słowo: ')]

# check if palindrom
for word in words:
    if word == word[::-1]:
        print(f"Słowo {word} jest palindromem")
    else:
        print(f"Słowo {word} nie jest palindromem")

# check if anagram
list_of_letters1 = []
list_of_letters2 = []

for i in range(len(words)):
    for letter in words[i]:
        if i == 0:
            list_of_letters1.append(letter)
        else:
            list_of_letters2.append(letter)

if sorted(list_of_letters1) == sorted(list_of_letters2):
    print('Te dwa słowa są wzajemnymi anagramami')
else:
    print('Te dwa słowa nie są wzajemnymi anagramami')

# w powyższym można od razu porównać dwa stringi
# if sorted('niedziela') == sorted('dzielenia'):
#     print('anagramy')
# else:
#     print('nie anagramy')
