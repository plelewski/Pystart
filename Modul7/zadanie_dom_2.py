from csv import reader
from random import choice

class Question:
    def __init__(self, question:str, answers:list, correct_answer:int):
        self.correct_answer = correct_answer
        self.answers = answers
        self.question = question

    def display(self):
        response = f'Pytanie: {self.question}\n'
        for no, answer in enumerate(self.answers, start=1):
            response += f'{no}. {answer} \n'

        return response

    def check_answer(self, answer_id: str):
        return self.correct_answer == answer_id

class Quiz:
    def __init__(self, filename):
        self.questions = []
        self.load_questions(filename)

    def load_questions(self, filename):
        with open(filename, encoding='utf8') as file:
            iterator = reader(file, delimiter=';')
            for row in iterator:
                question = row.pop(0)
                correct_answer = row.pop(-1)
                answers = row
                if len(answers) != 3:
                    raise ValueError('Nie mogę załadować pytania')
                self.questions.append(Question(question, answers, int(correct_answer)))

    def run(self):
        in_progress = True
        result = 0
        while in_progress:
            try:
                question = choice(self.questions)
                print(question.display())
                self.questions.remove(question)
                answer = input('Podaj poprawną odpowiedź: ')
                if question.check_answer(answer):
                    result += 1
                else:
                    break
            except IndexError:
                print('Wygrałeś. Koniec pytań')

        print(f"Koniec. Twój wynik: {result}")

if __name__ == '__main__':
    try:
        quiz = Quiz('quiz.csv')
        quiz.run()
    except FileNotFoundError:
        print('brak pliku')
    except ValueError:
        print('coś nie halo z pytaniami')
