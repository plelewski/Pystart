class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_product(self):
        return f'{self.name} w cenie {self.price}'


class ProductToBasket:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def get_ptb(self):
        return f'produkt: {self.product.get_product()} ,ilość: {self.quantity}'


class Basket:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_item(self):
        return self.items


if __name__ == '__main__':
    product1 = Product('chleb', 4.31)
    product2 = Product('serek', 1.85)

    ptb1 = ProductToBasket(product1, 1)
    ptb2 = ProductToBasket(product2, 3)

    basket = Basket()
    basket.add_item(ptb1)
    basket.add_item(ptb2)

    for itm in basket.items:
        print(itm.get_ptb())
