#!/usr/bin/env python3

import tkinter as tk

class Calculadora:

    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.display = tk.Entry(master, width=15, font=("Arial", 23), bd=5, insertwidth=1, bg="#C9ADFF", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=(0, 3))
        self.op_verification = False
        self.current = ""
        self.op = ""
        self.total = 0

        row = 1
        col = 0

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+", "=",
        ]

        for button in buttons:
            self.build_button(button, row, col)
            col += 1

            if col > 3:
                col = 0
                row += 1

        self.master.bind("<Key>", self.key_press)

    def key_press(self, event):
        valid_keys = "0123456789/*-+."
        key = event.char
        if key in valid_keys:
            self.click(key)
        elif key == '=' or key == '\r':  # Enter key
            self.calculate()
        elif key == '\x08':  # Backspace key
            self.clear_display()

    def clear_display(self):
        self.display.delete(0, "end")
        self.op_verification = False
        self.current = ""
        self.op = ""
        self.total = 0

    def calculate(self):
        if self.current and self.op:
            if self.op == "/":
                self.total /= float(self.current)
            if self.op == "*":
                self.total *= float(self.current)
            if self.op == "+":
                self.total += float(self.current)
            if self.op == "-":
                self.total -= float(self.current)

        self.display.delete(0, "end")
        self.display.insert("end", round(self.total, 3))

    def click(self, key):
        if self.op_verification:
            self.op_verification = False

        self.display.insert("end", key)

        if key in "0123456789" or key == ".":
            self.current += key
        else:
            if self.current:
                if not self.op:
                    self.total = float(self.current)

            self.current = ""
            self.op_verification = True
            self.op = key

    def build_button(self, button, row, col):
        if button == "C":
            b = tk.Button(self.master, text=button, width=6, font=("Arial", 11), command=lambda: self.clear_display())
        elif button == "=":
            b = tk.Button(self.master, text=button, width=6, font=("Arial", 11), command=lambda: self.calculate())
        else:
            b = tk.Button(self.master, text=button, width=6, font=("Arial", 11), command=lambda: self.click(button))

        b.grid(row=row, column=col)

root = tk.Tk()
root.geometry("267x205")
root.title("Calculadora")
my_gui = Calculadora(root)
root.mainloop()
