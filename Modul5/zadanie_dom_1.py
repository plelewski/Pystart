from words import words
from random import choice
import tkinter as tk
from tkinter import messagebox


def check_status():
    if len(hangman) == 0:
        messagebox.showinfo(title='komunikat', message='WISISZ !!!')
        root.destroy()
    if '_' not in user_word_to_find:
        messagebox.showinfo(title='komunikat', message='WYGRANA !!!')
        root.destroy()


def check_word():
    letter = next_letter.get().upper()
    if letter in used_letters:
        messagebox.showinfo(title='komunikat', message='litera była już użyta')
        next_letter.delete(0, 'end')
        return
    if len(letter) > 1 or letter == '':
        messagebox.showinfo(title='komunikat', message='podaj jedną literę')
        next_letter.delete(0, 'end')
        return
    used_letters.append(letter)
    label2.configure(text=sorted(used_letters))
    next_letter.delete(0, 'end')

    if letter not in word_to_find:
        hangman_result.append(hangman.pop(0))
        label5.configure(text=hangman_result)
    else:
        for let_idx, let in enumerate(word_to_find):
            if let == letter:
                user_word_to_find[let_idx] = letter
                label3.configure(text=user_word_to_find)
    check_status()


if __name__ == "__main__":
    word_to_find = list(choice(words).upper())  # losowanie słowa
    used_letters = []  # lista liter zapisanych przez gracza
    user_word_to_find = ['_' for i in word_to_find]  # słowo z odgadniętymi literami
    hangman = list('WISIELEC')
    hangman_result = []

    # tkinter part
    root = tk.Tk()
    root.title('Wisielec')
    root.geometry("300x200+300+300")

    label4 = tk.Label(root, text="Szukane słowo")
    label4.pack()
    label3 = tk.Label(root, text=user_word_to_find)
    label3.pack()
    label1 = tk.Label(root, text="Użyte litery")
    label1.pack()
    label2 = tk.Label(root, text=used_letters)
    label2.pack()
    next_letter = tk.Entry(root)
    next_letter.pack()
    button = tk.Button(root, text="Zapisz literę", activebackground='#78d6ff', command=check_word)
    button.pack()
    label5 = tk.Label(root, text=hangman_result)
    label5.pack()

    root.mainloop()
