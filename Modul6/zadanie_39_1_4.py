class Product:
    def __init__(self, name: str, price: float):
        self._price = price
        self._name = name

    def get_price(self):
        return self._price

    def get_name(self):
        return self._name


class ListItem:
    def __init__(self, product: Product, quantity: float):
        self._product = product
        self._quantity = quantity

    def get_product(self):
        return self._product

    def get_quantity(self):
        return self._quantity

    def get_cost(self):
        return self._quantity * self._product.get_price()

    def add_quantity(self, quantity):
        self._quantity += quantity


class List:
    def __init__(self):
        self._items = []

    def add_item(self, product: Product, quantity: float):
        for itm in self._items:
            if itm.get_product().get_name() == product.get_name():
                itm.add_quantity(quantity)
                return

        self._items.append(ListItem(product, quantity))

    def remove_item(self, select):
        del self._items[select]
        return

    def list_items(self):
        for itm in self._items:
            print(f'Id : {self._items.index(itm) + 1} '
                  f'Produkt: {itm.get_product().get_name()},'
                  f' cena jednostkowa: {itm.get_product().get_price()} zł'
                  f' ilość szt: {itm.get_quantity()},'
                  f' cena razem: {itm.get_cost()} zł')
        return f'Ilość pozycji na liście: {len(self._items)}, całkowity koszt : {list.calculate_total_cost()} '

    def calculate_total_cost(self):
        total = 0
        for itm in self._items:
            total += itm.get_cost()
        return total


list = List()

for i in range(50):
    choice = input('[d]:dodaj, [w]:wyświetl, [u]:usuń, [z]: zakończ : ')
    if 'd' in choice:
        in_name = input('Podaj nazwę produktu :')
        in_price = float(input('Podaj cenę jednostkową :'))
        in_quantity = int(input('Podaj ilość :'))
        product = Product(in_name, in_price)
        list.add_item(product, in_quantity)
        print('*' * 60)
        print(list.list_items())
        if i == 50:
            print('Lista jest pełna')

    if 'w' in choice:
        print('*' * 60)
        print(list.list_items())

    if 'u' in choice:
        select = int(input('Podaj numer pozycji aby usunąć :'))
        list.remove_item(select - 1)
        print(list.list_items())

    if 'z' in choice:
        print('Koniec')
        break
