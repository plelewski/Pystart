class Employee:
    def __init__(self, f_name: str, l_name: str, h_rate: int):
        self._h_rate = h_rate
        self.l_name = l_name
        self.f_name = f_name
        self._time_spent = 0

    def add_time_spent(self, value: int):
        self._time_spent += value

    def get_salary(self):
        return self._time_spent * self._h_rate

    def get_h_rate(self):
        return self._h_rate


class Manager(Employee):
    def __init__(self, f_name: str, l_name: str, h_rate: int):
        super().__init__(f_name, l_name, h_rate)
        self.bonus = 0

    def add_bonus(self, value: int):
        self.bonus += value

    def get_salary(self):
        return super().get_salary() + self.bonus


ee = Employee('aaa', 'aaa', 50)
ee.add_time_spent(50)
print(ee.get_salary())

mm = Manager('bbb', 'bbb', 50)
mm.add_time_spent(50)
mm.add_bonus(1000)
print(mm.get_salary())
