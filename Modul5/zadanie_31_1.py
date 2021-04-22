import tkinter as tk
from tkinter import messagebox
from random import randint


def check_value():
    next_value = int(find_num.get())
    root.counter += 1
    label2['text'] = "Ilość prób: " + str(root.counter)

    if next_value == random_num:
        messagebox.showinfo(title='wygrałeś', message='cyfra prawidłowa')
        return
    if root.counter > 1:
        if abs(next_value - random_num) > abs(used_num[-1] - random_num):
            label3.configure(text="zimno")
        else:
            label3.configure(text="ciepło")
    used_num.append(next_value)
    find_num.delete(0, 'end')


if __name__ == '__main__':
    used_num = []
    random_num = randint(1,51)
    root = tk.Tk()
    root.title('Zgadywanka')
    root.geometry("300x150+300+300")
    root.counter = 0

    label1 = tk.Label(root, text="Zgadnij cyfrę od 1 do 50")
    label1.pack()
    find_num = tk.Entry(root)
    find_num.pack()
    button = tk.Button(root, text="Próbuj", activebackground='#78d6ff', command=check_value)
    button.pack()

    label2 = tk.Label(root, text="Ilość prób: " + str(root.counter))
    label2.pack()

    label3 = tk.Label(root, text="")
    label3.pack()

    root.mainloop()
