import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets1()
        self.create_widgets2()

    def create_widgets1(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

    def create_widgets2(self):
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
