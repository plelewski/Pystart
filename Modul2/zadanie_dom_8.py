# words = input('Podaj słowa oddzielone przecinkami - mogą się powtarzać: ') # można wstawić zamiast całego input'a

for i in set(input('Podaj słowa oddzielone przecinkami - mogą się powtarzać: ').split(',')):
    print(i)
