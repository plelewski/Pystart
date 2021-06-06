from abc import ABC, abstractmethod


class Actor:
    def __init__(self, first_name:str, last_name:str):
        self.last_name = last_name
        self.first_name = first_name


    @abstractmethod
    def say_hello(self):
        return f"Hello, ma name is {self.first_name} {self.last_name} and I'm "


class Teacher(Actor):
    def say_hello(self):
        return Actor.say_hello(self) + 'a teacher'


class Employee(Actor):
    def say_hello(self):
        return Actor.say_hello(self) + 'an employee'


class Student(Actor):
    def say_hello(self):
        return Actor.say_hello(self) + 'a student'


class Person:
    @staticmethod
    def create_new(class_name:str, first_name:str, last_name:str):
        try:
            class_ = globals()[class_name]
            return class_(first_name, last_name)
        except KeyError:
            print(f'Nieznana klasa {class_name}')
            quit()


def main():
    stanislaw = Person.create_new('Student', 'Stanisław', 'Stanisławowski')
    print(stanislaw.say_hello())


if __name__ == '__main__':
    main()
