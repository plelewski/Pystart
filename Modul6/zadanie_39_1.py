class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_price(self):
        return self._price


class ListItem:
    def __init__(self, product: Product, quantity: int):
        self._products = product
        self._quantity = quantity

    def get_quantity(self):
        return self._quantity

    def get_product(self):
        return self._products

    def get_subtotal(self):
        return self._quantity * self._products.get_price()

    def increase_quantity(self, quantity):
        self._quantity += quantity

    def decrease_quantity(self, quantity):
        self._quantity -= quantity


class List:
    def __init__(self):
        self._items = []

    def add_item(self, product: Product, quantity: int):
        for item in self._items:
            if item.get_product() == product:
                item.increase_quantity(quantity)
                return  # return jest po to, aby się zakończyło i po dodaniu quantity nie wywołało się to niżej

        self._items.append(ListItem(product, quantity))

    def remove_item(self, product: Product, quantity: int):
        for item in self._items:
            if item.get_product() == product:
                item.decrease_quantity(quantity)
                return  # return jest po to, aby się zakończyło i po dodaniu quantity nie wywołało się to niżej

    def list_items(self):
        return self._items

    def calculate_total_cost(self) -> float:
        total = 0
        for item in self._items:
            total += item.get_subtotal()

        return total


def test_add_item_to_list_once():
    product1 = Product('chleb', 4.3)
    to_buy = List()

    to_buy.add_item(product1, 3)

    assert to_buy.calculate_total_cost() == 4.3 * 3
    assert len(to_buy.list_items()) == 1

def test_add_the_same_item_to_list_twice():
    product1 = Product('chleb', 4.3)
    to_buy = List()

    to_buy.add_item(product1, 3)
    to_buy.add_item(product1, 3)

    assert to_buy.calculate_total_cost() == 4.3 * 6
    assert len(to_buy.list_items()) == 1

def test_add_different_product_to_list():
    product1 = Product('chleb', 4.3)
    product2 = Product('serek', 1.85)
    to_buy = List()

    to_buy.add_item(product1, 3)
    to_buy.add_item(product2, 3)

    assert to_buy.calculate_total_cost() == 4.3 * 3 + 1.85 * 3
    assert len(to_buy.list_items()) == 2
