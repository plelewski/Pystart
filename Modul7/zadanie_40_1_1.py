class BankAccount:
    def __init__(self, f_name: str, l_name: str):
        self.f_name = f_name
        self.l_name = l_name
        self._balance = 0

    def get_balance(self):
        return round(self._balance, 2)

    def deposit(self, value: float):
        self._balance += value

    def withdraw(self, value: float):
        if value > self._balance:
            print('Niestety kwota przewyższa zgromadzone środki')
            return
        self._balance -= value


class SavingsAccount(BankAccount):
    def get_balance(self):
        return super().get_balance() * 1.01


sa = SavingsAccount('aa', 'bb')
sa.deposit(100)
print(sa.get_balance())


def test_deposit():
    konto = BankAccount('Ada', 'Kowalska')
    konto.deposit(320.45)
    konto.deposit(100.00)
    assert konto.get_balance() == 420.45

def test_withdraw():
    konto = BankAccount('Ada', 'Kowalska')
    konto.deposit(320.45)
    konto.withdraw(100.25)
    assert konto.get_balance() == 220.20
