from datetime import datetime


class Application:
    @staticmethod
    def main():
        first_name = input('Imie: ')
        last_name = input('Nazwisko: ')
        date_of_employment = datetime.strptime(input('Data zatrudnienia (yyyy.mm.dd): '), '%Y.%m.%d')
        if not Application.check_date_of_employment(datetime.today(), date_of_employment):
            raise InvalidDateOfEmployment

        employee = BaseEmployee(first_name, last_name, date_of_employment)

    @staticmethod
    def check_date_of_employment(today: datetime, date: datetime):
        difference = today - date
        difference_in_years = round(difference.days / 365.25)
        return 50 > difference_in_years > 0


class InvalidDateOfEmployment(Exception):
    pass


class BaseEmployee:
    def __init__(self, first_name: str, last_name: str, date_of_employment: datetime):
        self.date_of_employment = date_of_employment
        self.last_name = last_name
        self.first_name = first_name

    @property
    def employment_time(self):
        today = datetime.today()
        difference = today - self.date_of_employment

        return difference.days

    def __lt__(self, other):
        return self.employment_time < other.employment_time

    def __repr__(self):
        return self.first_name

if __name__ == '__main__':
    Application.main()


def test_sort_employees():
    # when
    a = BaseEmployee('a', 'a', datetime(2020, 12, 10))
    b = BaseEmployee('b', 'b', datetime(2020, 11, 10))
    employess = [a, b]

    #given
    sorted_employess = sorted(employess)

    # then
    assert employess[0] == a
