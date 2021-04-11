def give_vowels(word):
    res_list = set()
    for letter in word.lower():
        if letter in 'aeiouy':
            res_list.add(letter)

    return res_list if len(res_list) > 0 else ()

def give_vowels2(word):
    return {char for char in word if char in 'aeiouy'}

word = input('Podaj słowo: ').replace(' ','')
print('Znalezione samogłoski: ', give_vowels(word))
print('Znalezione samogłoski: ', give_vowels2(word))
