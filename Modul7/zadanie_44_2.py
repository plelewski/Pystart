from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float
    discount: float


class Collecsion:
    def __init__(self):
        self.items = []

    @classmethod
    def create_with_items(cls, *args):
        collecsion = cls()
        collecsion.items.extend(args)

        return collecsion


i1 = Item('Chleb', 4, 0.1)
i2 = Item('Mleko', 3.2, 0.2)

col = Collecsion.create_with_items(i1, i2)
print(col.items)
