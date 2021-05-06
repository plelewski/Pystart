class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Produkt {self.name} w cenie {self.price}'


class List:
    def __init__(self):
        self.items = {}

    def add_item(self, product: Product, quantity: int):
        if product in self.items.keys():
            self.items[product] += quantity
            return

        self.items[product] = quantity

    def total_cost(self):
        total = 0
        for key, val in self.items.items():
            total += key.price * val

        return round(total, 2)


if __name__ == '__main__':
    product1 = Product('chleb', 1.0)
    product2 = Product('ser', 2.0)

    to_buy = List()
    to_buy.add_item(product1, 1)
    to_buy.add_item(product2, 2)
    to_buy.add_item(product1, 3)

    for k, v in to_buy.items.items():
        print(k, 'w ilości', v)

    print(to_buy.total_cost())
