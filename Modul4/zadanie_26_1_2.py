# inny sposób
# print(list(sorted(map(lambda x: str(x).title(), people), key=lambda y: y[str(y).rfind(' ') + 1])))

def format_and_sort(names: list) -> list:
    return list(sorted(map(lambda x: str(x).title(), names), key=lambda y: y[str(y).rfind(' ') + 1]))


def test_format_and_sort():
    people = ['zofia nowak', 'kryStyna kowalska', 'michał lewandowski']
    assert format_and_sort(people) == ['Krystyna Kowalska', 'Michał Lewandowski', 'Zofia Nowak']
