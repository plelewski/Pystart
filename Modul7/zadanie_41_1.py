from datetime import datetime


class Saving:
    def __init__(self, date_from: datetime, value: int):
        self._value = value
        self._date_from = date_from

    @property
    def date_from(self):
        return self._date_from

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            self._value = 0
        else:
            self._value = new_value


class Savings:
    def __init__(self):
        self.saving_list = []

    def add_saving(self, saving: Saving):
        self.saving_list.append(saving)

    @property
    def total(self):
        return sum([i.value for i in self.saving_list])


s3 = Saving(datetime(2021, 1, 1), 0)
to_saving = Savings()
to_saving.add_saving(s3)
print(to_saving.total)


def test_total():
    # given
    s1 = Saving(datetime(2021, 1, 1), 120)
    s2 = Saving(datetime(2021, 2, 1), 101)

    # when
    to_saving = Savings()
    to_saving.add_saving(s1)
    to_saving.add_saving(s2)

    # then
    assert to_saving.total == 221
