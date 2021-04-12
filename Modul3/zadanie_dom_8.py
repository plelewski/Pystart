def fibonacci(num):
    fir, sec = 0, 1
    for _ in range(num):
        yield fir
        fir, sec = sec, fir + sec


def fibonacci2(limit:int):
    fir, sec = 0, 1
    result = [fir, sec]
    while len(result) < limit:
        fir, sec = sec, fir + sec
        result.append(sec)

    return result

for i in fibonacci(5):
    print(f'kolejna cyfra {i}')

print(fibonacci2(8))
