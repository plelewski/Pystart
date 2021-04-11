from math import sqrt, floor

def is_number_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_number_prime2(num):
    for div in range(2, floor(sqrt(num)) + 1):
        if num % div == 0:
            return False

    return True


number = int(input('Podaj liczbę do zbadania czy jest pierwszą: '))
print(is_number_prime(number))
print(is_number_prime2(number))
