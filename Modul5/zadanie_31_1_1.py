import tkinter as tk
from tkinter import messagebox
from random import randint


class hangman_frame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.game = Hangman()
        self.master = master
        self.create_widgets()
        self.layout()
        self.setup_game()

    def setup_game(self):
        self.game.new_game()
        self.draw_hangman()
        self.wrong_letters.configure(text=', '.join(self.game.wrong_letters))
        self.tip.configure(text='\t'.join(self.game.tip))

    def create_widgets(self):
        self.label = tk.Label(self, text='')
        self.entry = tk.Entry(self)
        self.entry.bind('<Return>', self.check_answer)  # żeby działał enter na przycisku
        self.button = tk.Button(self, text='Sprawdźmy :-)', command=self.check_answer)
        self.tip = tk.Label(self)
        self.wrong_letters = tk.Label(self)
        self.picture = tk.Canvas(self, height=150, width=150)

    def layout(self):
        self.pack()
        self.label.pack()
        self.picture.pack()
        self.wrong_letters.pack()
        self.entry.pack()
        self.button.pack()
        self.tip.pack()

    def check_answer(self, key=None):
        win, result, step, tip, wrong_letters = self.game.check_letter(self.entry.get())
        if not result:
            self.draw_hangman(step)
        self.tip.configure(text='\t'.join(tip))
        self.wrong_letters.configure(text=', '.join(wrong_letters))

        if win == False:
            messagebox.showerror(title="Przykro mi...",
                                 message=f"Przegrałaś :-(\n Prawidłowa odpowiedź to: {self.game.word}")
            self.setup_game()
        elif win == True:
            messagebox.showerror(title="Hurra!", message="Wygrałaś :-)")
            self.setup_game()
        self.entry.delete(0, tk.END)  # czyszczenie entry

    def draw_hangman(self, step=0):
        self.picture.delete('all')
        self.picture.create_line(25, 25, 25, 125)
        self.picture.create_line(15, 125, 35, 125)  # stopa szubienicy
        self.picture.create_line(25, 25, 100, 25)
        if step >= 1:
            self.picture.create_line(100, 25, 100, 45)  # sznur
        if step >= 2:
            self.picture.create_oval(85, 45, 115, 75)  # głowa
        if step >= 3:
            self.picture.create_line(100, 75, 100, 100)  # tułów
        if step >= 4:
            self.picture.create_line(100, 100, 90, 110)  # noga lewa
        if step >= 5:
            self.picture.create_line(100, 100, 110, 110)  # noga prawa
        if step >= 6:
            self.picture.create_line(100, 80, 90, 90)  # ręka lewa
        if step >= 7:
            self.picture.create_line(100, 80, 110, 90)  # ręka prawa


class Hangman:
    def __init__(self):
        self.chose_word()
        self.new_game()
        self.wrong_letters = []

    def chose_word(self):
        self.words = []
        with open('wyrazy_hangman.txt', encoding='UTF-8') as file:
            for line in file:
                self.words.append(line.strip())
        self.word = (self.words[randint(0, len(self.words) - 1)])

    def check_letter(self, letter):
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.tip[i] = letter
            if '#' not in self.tip:
                self.won = True
            return (self.won, True, self.step, self.tip,
                    self.wrong_letters)  # (stan gry, czy trafiona litera, ilość błędów, odkryte litery)
        else:
            self.step += 1
            if self.step >= 7:
                self.won = False
                return (self.won, False, self.step, self.tip, self.wrong_letters)
            else:
                self.wrong_letters.append(letter)
                return (self.won, False, self.step, self.tip, self.wrong_letters)

    def new_game(self):  # czyści i zaczyna grę od nowa
        self.chose_word()
        self.tip = list('#' * len(self.word))
        self.step = 0
        self.won = None
        self.wrong_letters = []


window = tk.Tk()
window.title('wisielec')
frame = hangman_frame(window)
frame.mainloop()
