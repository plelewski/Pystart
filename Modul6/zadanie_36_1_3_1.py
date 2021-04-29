class Car:
    def __init__(self, car_name:str, price:int, max_speed:int):
        self.car_name = car_name
        self.price = price
        self.max_speed = max_speed

    def sort_by_price(self):
        return self.price

    def sort_by_speed(self):
        return self.max_speed


if __name__ == '__main__':
    cars = []
    for _ in range(3):
        cn = input('Podaj nazwę auta: ')
        pr = int(input('Podaj cenę auta: '))
        ms = int(input('Podaj maksymalną prędkość: '))
        cars.append(Car(cn, pr, ms))

    # sortowanie po cenie BEZ metod w klasie
    # for f in sorted(cars, key=lambda x: x.price):
    # print(f.car_name, ' ', f.price, ' ', f.max_speed)

    # sortowanie wg metod w klasie
    print('Auta posortowane wg prędkości maksymalnej')
    for f in sorted(cars, key=Car.sort_by_speed, reverse=True):
        print(f.car_name, ' ', f.price, ' ', f.max_speed)

    print('Auta posortowane wg ceny')
    for f in sorted(cars, key=Car.sort_by_price):
        print(f.car_name, ' ', f.price, ' ', f.max_speed)
