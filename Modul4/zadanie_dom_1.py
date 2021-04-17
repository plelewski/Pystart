def group_them(**kwargs):
    if len(kwargs) == 0:
        return ''
    for k, v in kwargs.items():
        print(k.title(),'is', str(v).lower())


def test_group_them():
    assert group_them(wall="red") == "wall is red"


if __name__ == '__main__':
    group_them(wall="red", tomato="red", lemon="yellow")
