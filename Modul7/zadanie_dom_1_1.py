from datetime import datetime


class BaseEmployee:
    def __init__(self, f_name: str, s_name: str, hire_date: datetime):
        self.hire_date = hire_date
        self.s_name = s_name
        self.f_name = f_name

    @property
    def employment_time(self):
        now = datetime.now()
        return (now - self.hire_date).days

    def __lt__(self, other):
        return self.employment_time < other.employment_time

    def __str__(self):
        return f'{self.f_name} {self.s_name} rozpoczął pracę: {self.hire_date} {self.employment_time}'


class Employee(BaseEmployee):
    def __init__(self, f_name: str, s_name: str, hire_date: datetime, time_spent: int, rate: float, bonus: float):
        super().__init__(f_name, s_name, hire_date)
        self.bonus = bonus
        self.rate = rate
        self.time_spent = time_spent

    def get_salary(self):
        return f'{self.s_name},{self.f_name} dostanie: {(self.time_spent * self.rate + self.bonus):.2f} zł'

    @classmethod
    def create_fulltime(cls, f_name, s_name, hire_date, rate, bonus):
        return cls(f_name, s_name, hire_date, 160, rate, bonus)

def main():
    emp1 = Employee('Piotr', 'Kowalski', datetime(2021, 1, 1), 145, 12, 123.45)
    print(emp1.get_salary())

    emp2 = Employee.create_fulltime('Adam', 'Adamowski', datetime(2021, 1, 1), 12, 123.45)
    print(emp2.get_salary())

if __name__ == '__main__':
    main()
