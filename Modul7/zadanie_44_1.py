class Person:
    def __init__(self, f_name: str, s_name: str):
        self.s_name = s_name
        self.f_name = f_name

    @classmethod
    def from_row(cls, row: str):
        # Jan;Kowalski
        first_name, last_name = row.strip().split(";")
        return cls(first_name, last_name)


# p = Person('Ania', 'Aniowska')
# print(p.f_name, p.s_name)

p = Person.from_row('Dawid;Dawidowski')
print(p.f_name, p.s_name)
