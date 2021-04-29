from math import pi

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def calculate_radius(self):
        return 2 * pi * self.radius

    def calculate_field(self):
        return pi * self.radius * self.radius


# python -m pytest zadanie_36_1_1
def test_calculate_field():
    # given
    r = 10
    c = Circle(r)

    # when
    field = c.calculate_field()

    # then
    assert field == pi * r * r

def test_calculate_radius():
    r = 10
    c = Circle(r)

    radius = c.calculate_radius()

    assert radius == 2 * pi * r

circle1 = Circle(3)
print(circle1.calculate_radius())
print(circle1.calculate_field())
