def count_letters(text, start='(', end=')'):
    result = []
    s, e = 0, 0
    for i, char in enumerate(text, start=1):
        if char == start:
            s = i
        elif char == end:
            e = i
            if e > s:
                result.append(e - s - 1)
            s, e = 0, 0
    return [0] if not result else result


print(count_letters('(ala) ma (kota)'))
print(count_letters('<> kod <103>', '<', '>'))
print(count_letters('abrakadabra'))
