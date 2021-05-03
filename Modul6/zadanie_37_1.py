from datetime import datetime

class Author:
    def __init__(self, fname:str, sname:str, date_of_birth):
        self.fname = fname
        self.sname = sname
        self.date_of_birth = date_of_birth

class Book:
    def __init__(self, title:str, kind:str, author:Author, desc:str, summary:str, rate:float):
        self.title = title
        self.kind = kind
        self.author = author
        self.desc = desc
        self.summary = summary
        self.rate = rate


bonifacy = Author('Bonifacy', 'Smith', datetime('1910, 10, 10'))
john = Author('John', 'Smith', datetime('1905, 05, 15'))
book = Book(
    'Przykładowy tytuł',
    'Kryminał',
    ['bonifacy', 'john'],
    'opis książki',
    'streszczenie',
    4.7
)
