class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} w cenie {self.price}'


class ProductToBasket:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f'produkt: {self.product} ,ilość: {self.quantity}'

    def get_product_to_basket(self):
        return self.product

    def incr_quantity(self, quantity: int):
        self.quantity += quantity

class Basket:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        for i in self.items:
            if i.get_product_to_basket().name == item.product.name:
                i.incr_quantity(item.quantity)
                return

        self.items.append(item)

    def get_item(self):
        return self.items


if __name__ == '__main__':
    product1 = Product('chleb', 4.31)
    product2 = Product('serek', 1.85)
    product3 = Product('serek', 11.85)

    ptb1 = ProductToBasket(product1, 1)
    ptb2 = ProductToBasket(product2, 3)
    ptb3 = ProductToBasket(product3, 1)

    basket = Basket()
    basket.add_item(ptb1)
    basket.add_item(ptb2)
    basket.add_item(ptb3)

    for itm in basket.items:
        print(itm)
