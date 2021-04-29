class Car:
    def __init__(self, car_name:str, price:int, max_speed:int):
        self.car_name = car_name
        self.price = price
        self.max_speed = max_speed

    def get_info(self):
        return f'{self.car_name}, cena: {self.price}, prędkość max: {self.max_speed}'


class Collection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self, key, reverse=False):
        return sorted(self.items, key=key, reverse=reverse)


if __name__ == '__main__':
    collection = Collection()
    for _ in range(3):
        cn = input('Podaj nazwę auta: ')
        pr = int(input('Podaj cenę auta: '))
        ms = int(input('Podaj maksymalną prędkość: '))
        collection.add_item(Car(cn, pr, ms))

    # sortowanie po cenie malejąco
    for f in collection.get_items(lambda x: x.price, True):
        print(f.get_info())

    # sortowanie po prędkości maksymalnej
    for f in collection.get_items(lambda x: x.max_speed):
        print(f.get_info())
