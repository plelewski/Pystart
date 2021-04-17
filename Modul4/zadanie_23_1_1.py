def remove_vowels(text:str) -> str:
    vowels = 'aAeEiIuUyYoO'
    # result = ''
    # for i in text:
    #     if i not in vowels:
    #         result += i
    # return result
    # inny sposób
    return ''.join(char for char in text if char not in vowels)


def test_all_vowels():
    assert remove_vowels('aaaiii') == ''


def test_all_consonant():
    assert remove_vowels('qwrtp') == 'qwrtp'


def test_mix():
    assert remove_vowels('qwerty KOT') == 'qwrt KT'


def test_empty():
    assert remove_vowels('') == ''
