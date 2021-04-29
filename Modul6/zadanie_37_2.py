class Apple:
    def __init__(self, color:str, taste:str, kind:str):
        self.color = color
        self.taste = taste
        self.kind = kind


class Basket:
    def __init__(self):
        self.items = []

    def add(self, apple:Apple):
        self.items.append(apple)


class Report:
    def __init__(self, basket:Basket):
        self.basket = basket

    def get_for_color(self):
        report = {}
        for f in self.basket.items:
            if f.color not in report:
                report[f.color] = 0

            report[f.color] += 1
        return report


if __name__ == '__main__':
    apple1 = Apple('Zielone', 'Słodkie', 'Dojrzałe')
    apple2 = Apple('Zielone', 'Słodkie', 'Dojrzałe')
    apple3 = Apple('Czerwone', 'Słodkie', 'Dojrzałe')

    basket = Basket()
    basket.add(apple1)
    basket.add(apple2)
    basket.add(apple3)

    rep = Report(basket)

    print(rep.get_for_color())
