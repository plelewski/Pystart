def fibonacci(num:int):
    fir, sec = 0, 1
    for _ in range(num):
        yield fir
        fir, sec = sec, fir + sec

for i in fibonacci(5):
    print(f'kolejna cyfra {i}')
