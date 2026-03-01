# 1
from tkinter import *

def str_to_sort_list(event):
    s = ent.get()
    s = s.split()
    s.sort()
    lab['text'] = ' '.join(s)
    
root = Tk()

ent = Entry(width=20)
but = Button(text="Преобразовать")
lab = Label(width=20, bg='black', fg='white')

but.bind('<Button-1>', str_to_sort_list)

ent.pack()
but.pack()
lab.pack()
root.mainloop()


# 2
from tkinter import *

class Block:
    def __init__(self, master, func):
        self.ent = Entry(master, width=20)
        self.but = Button(master, text='Преобразовать')
        self.lab = Label(master, width=20, bg='black', fg='white')
        self.but['command'] = getattr(self, func)
        self.ent.pack()
        self.but.pack()
        self.lab.pack()
        
    def str_to_sort(self):
        s = self.ent.get()
        s = s.split()
        s.sort()
        self.lab['text'] = ' '.join(s)
        
    def str_reverse(self):
        s = self.ent.get()
        s = s.split()
        s.reverse()
        self.lab['text'] = ' '.join(s)
        
root = Tk()

first_block = Block(root, 'str_to_sort')
second_block = Block(root, 'str_reverse')

root.mainloop()


# 3 - ИСПРАВЛЕНО
from tkinter import *

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Ошибка: деление на ноль"
            else: 
                result = num1 / num2
        else: 
            result = "Ошибка: неверная операция"
        result_label.config(text=str(result))
    except ValueError:
        result_label.config(text="Ошибка: введите числа")

window = Tk()
window.title("Калькулятор")

entry1 = Entry(window)
entry1.pack()

entry2 = Entry(window)
entry2.pack()

operation_var = StringVar()
operation_var.set("+")

operations_frame = Frame(window)
operations_frame.pack()

Radiobutton(operations_frame, text="+", variable=operation_var, value="+").pack(side=LEFT)
Radiobutton(operations_frame, text="-", variable=operation_var, value="-").pack(side=LEFT)
Radiobutton(operations_frame, text="*", variable=operation_var, value="*").pack(side=LEFT)
Radiobutton(operations_frame, text="/", variable=operation_var, value="/").pack(side=LEFT)

calculate_btn = Button(window, text="Вычислить", command=calculate)
calculate_btn.pack()

result_label = Label(window, text="0")
result_label.pack()

window.mainloop()


# 4
from tkinter import *

def change():
    b1['text'] = "Изменено"
    b1['bg'] = '#000000'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'
    
root = Tk()
b1 = Button(text="Изменить", width=15, height=3)
b1.config(command=change)
b1.pack()
root.mainloop()


# 5
from tkinter import *

root = Tk()

l1 = Label(text="Машинное обучение", font="Arial 32")
l2 = Label(text="Распознавание образов", font=("Comic Sans MS", 24, "bold"))
l1.config(bd=20, bg='#ffaaaa')
l2.config(bd=20, bg='#aaffff')
l1.pack()
l2.pack()
root.mainloop()


# 5_2
from tkinter import *

def take():
    lab['text'] = "Выдано"
    
root = Tk()

Label(text="Пункт выдачи").pack()
Button(text="Взять", command=take).pack()

lab = Label(width=10, height=1)
lab.pack()

root.mainloop()


# 6
from tkinter import *
from datetime import datetime as dt

def insert_time():
    t = dt.now().time()
    e1.insert(0, t.strftime('%H:%M:%S '))
    
root = Tk()
e1 = Entry(width=50)
but = Button(text="Время", command=insert_time)

e1.pack()
but.pack()
root.mainloop()