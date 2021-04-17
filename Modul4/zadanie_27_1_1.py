def round_to_two(func):
    def wrapper(*args, **kwargs):
        return round(func(*args), 2)

    return wrapper

@round_to_two
def divide_two_num(a, b):
    return a/b


def test_round_to_two():
    @round_to_two
    def function(value):
        return value

    assert function(3.6712) == 3.67

print(divide_two_num(11, 3))
