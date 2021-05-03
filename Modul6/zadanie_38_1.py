class LengthUnit:
    def __init__(self, value: int):
        self.value = value

    def to_centimeter(self):
        return self.value / 10

    def to_meter(self):
        return self.value / 10 / 100

    def __add__(self, other):
        total = self.value + other.value
        return LengthUnit(total)            # dzięki temu powstaje nowy obiekt ze zsumowaną wartością

    def __cmp__(self, other):
        return self.value == other.value    # dzięki temu poniżej działa porównywanie obiektów ze sobą

    def __sub__(self, other):
        result = self.value - other.value
        return LengthUnit(result)


if __name__ == '__main__':
    lu1 = LengthUnit(1000)
    lu2 = LengthUnit(3000)
    lu3 = lu1 + lu2

    print(lu3.value)
    print(lu1 == lu2)

    lu4 = lu2 - lu1
    print(lu4.value)


def test_sub_length_unit():
    # given
    obj1 = LengthUnit(50)
    obj2 = LengthUnit(20)

    # when
    obj3 = obj1 - obj2

    # then
    assert obj3.value == 30
