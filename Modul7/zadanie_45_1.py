from datetime import datetime

class Product:
    def __init__(self, price_netto: float):
        self.price_netto = price_netto

    def calculate_netto(self):
        return self.price_netto

    def calculate_brutto(self):
        return self.price_netto * 1.23


class Booking:
    def __init__(self, date_from: datetime, date_to: datetime):
        self.date_to = date_to
        self.date_from = date_from

    def get_difference(self):
        return (self.date_to - self.date_from).days


class Reservation(Product, Booking):
    def __init__(self, price_netto, date_from, date_to):
        Product.__init__(self, price_netto)
        Booking.__init__(self, date_from, date_to)

    def total_price(self):
        return self.calculate_brutto() * self.get_difference()


if __name__ == '__main__':
    r = Reservation(100, datetime(2020, 5, 1), datetime(2020, 5, 11))
    print(f'Kwota brutto pobytu za dobę: {r.calculate_brutto():.2f} zł')
    print(f'Kwota pobytu {r.total_price():.2f} zł')
