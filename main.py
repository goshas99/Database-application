import tkinter
import webbrowser
import psycopg2
from tkinter import *
import tkinter.messagebox as mb
import requests
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter import messagebox

connect = psycopg2.connect(database='my_DB', user='postgres', password='Getmpad123', host='localhost', port='5432')
print("Database opened successfully")
cursor = connect.cursor()


def main():  # Функция авторизации
    if txt1.get() == 'admin' and txt2.get() == '1':
        window.after(300, window.destroy())
        DB()
    else:
        msg = 'Данные введены не верно!'
        mb.showerror("Ошибка", msg)


window = Tk()
window.title('База данных по авиационныйм приборам')
window.geometry('500x300')
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2.5
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 3.5
window.wm_geometry("+%d+%d" % (x, y))
lbl = Label(window, text="Авторизация", font=("Arial Bold", 20))  # Текст окна авторизации
lbl.place(relx=0.5, y=15, anchor='center')

txt1 = Entry(window, width=20)  # Окно ввода логина
txt1.place(relx=0.5, y=100, anchor='center')

lbl1 = Label(window, text='Логин', anchor='center')  # Текст ввода логина
lbl1.place(relx=0.25, y=89)

txt2 = widget = Entry(window, show="*", width=20)  # Окно ввода пароля
txt2.place(relx=0.5, y=150, anchor='center')

lbl2 = Label(window, text='Пароль', anchor='center')  # Текст ввода пароля авторизации
lbl2.place(relx=0.25, y=140)

btn = Button(window, text='Войти', command=main)  # Текст кнопки авторизации
btn.place(relx=0.5, y=200, anchor='center')


def na():
    cursor.execute('SELECT Название FROM Самолеты')
    output = cursor.fetchall()
    my_list = []
    for i in output:
        my_list.append(' | '.join(i))
    my_str = '\n'.join(my_list)
    console = Text(width=60, height=20)
    console.place(relx=0.5, y=200, anchor='center')
    console.insert(1.0, my_str)

    def delete_win1():
        console.delete(1.0, END)


def devices():
    cursor.execute('SELECT Название FROM Приборы')
    output = cursor.fetchall()
    my_list = []
    for i in output:
        my_list.append(' | '.join(i))
    my_str = '\n'.join(my_list)
    console = Text(width=60, height=20)
    console.place(relx=0.5, y=200, anchor='center')
    console.insert(1.0, my_str)

    def delete_win1():
        console.delete(1.0, END)

    window2 = Tk()
    window2.title('Приборы')
    window2.geometry('800x500')
    x2 = (window2.winfo_screenwidth() - window2.winfo_reqwidth()) / 2
    y2 = (window2.winfo_screenheight() - window2.winfo_reqheight()) / 2
    window2.wm_geometry("+%d+%d" % (x2, y2))
    console1 = Text(window2, width=60, height=20)
    console1.place(relx=0.5, y=200, anchor='center')

    console4 = Text(window2, width=10, height=2)
    console4.place(relx=0.5, x=300, y=56, anchor='center')

    console5 = Text(window2, width=15, height=2)
    console5.place(relx=0.5, x=310, y=100, anchor='center')

    def delete_win2():
        console1.delete(1.0, END)
        console4.delete(1.0, END)
        console5.delete(1.0, END)

    def callbackFunc1(dev):
        dev = w.get()
        # messagebox.showinfo("Xiith.com", "You selected " + dev)
        cursor.execute(f"SELECT Описание FROM Приборы WHERE Название = '{dev}'")
        answer = cursor.fetchall()
        console1.insert(1.0, answer)
        window2.title(f'{dev}')

    def airplane2(dev):
        my_list3 = []
        my_list1 = []
        my_list2 = []
        dev = w.get()
        cursor.execute(f"SELECT id_прибора FROM Приборы WHERE Название = '{dev}'")
        answerr = cursor.fetchall()
        m = type(answerr)
        # cursor.execute(f"SELECT id_самолета FROM Датчики_Самолеты WHERE id_датчика= '{answerr}'")
        answerr1 = cursor.fetchall()
        # cursor.execute(f"SELECT Название FROM Самолеты WHERE id_самолета = '{answerr1}'")
        # answerr2 = cursor.fetchall()
        console4.insert(1.0, answerr)

    def link2(dev):
        dev = w.get()
        cursor.execute(f"SELECT Ссылка FROM Приборы WHERE Название = '{dev}'")
        an = cursor.fetchall()
        console5.insert(1.0, an)

    def call2():
        result = console5.get(1.0, tkinter.END)
        webbrowser.open_new(f"{result}")

    def add_device():
        def add_device_db():
            nazv = txt4.get()
            princ = txt5.get()
            opis = txt6.get()
            ssyl = txt7.get()
            cursor.execute(
                f"INSERT INTO Приборы(Название, Принцип_работы, Описание, Ссылка) VALUES('{nazv}', '{princ}', "
                f"'{opis}', '{ssyl}')")
            connect.commit()
            window4.after(300, window4.destroy())
            messagebox.showinfo("Успешно!", "Вы успешно добавили прибор " + nazv)

        window4 = Tk()
        window4.title('Добавить прибор')
        window4.geometry('350x300')
        x3 = (window4.winfo_screenwidth() - window4.winfo_reqwidth()) / 3
        y3 = (window4.winfo_screenheight() - window4.winfo_reqheight()) / 3
        window4.wm_geometry("+%d+%d" % (x3, y3))

        lbl4 = Label(window4, text='Название', anchor='center')
        lbl4.place(relx=0.25, x=-50, y=50, anchor='center')

        txt4 = Entry(window4, width=20)
        txt4.place(relx=0.5, x=-1, y=50, anchor='center')

        lbl5 = Label(window4, text='Принцип работы', anchor='center')
        lbl5.place(relx=0.25, x=-40, y=100, anchor='center')

        txt5 = Entry(window4, width=20)
        txt5.place(relx=0.5, x=-1, y=100, anchor='center')

        lbl6 = Label(window4, text='Описание', anchor='center')
        lbl6.place(relx=0.25, x=-40, y=150, anchor='center')

        txt6 = Entry(window4, width=20)
        txt6.place(relx=0.5, x=-1, y=150, anchor='center')

        lbl7 = Label(window4, text='Ссылка', anchor='center')
        lbl7.place(relx=0.25, x=-40, y=200, anchor='center')

        txt7 = Entry(window4, width=20)
        txt7.place(relx=0.5, x=-1, y=200, anchor='center')

        btn7 = Button(window4, text='Загрузить', command=add_device_db)
        btn7.place(relx=0.1, x=130, y=250, anchor='center')

    def del_device():
        def del_device_name():
            name = txt5.get()
            cursor.execute(f"DELETE FROM Приборы WHERE Название = '{name}';")
            window5.after(300, window5.destroy())
            messagebox.showinfo("Успешно!", "Вы успешно удалили прибор " + name)

        window5 = Tk()
        window5.title('Удалить прибор')
        window5.geometry('400x70')
        x3 = (window5.winfo_screenwidth() - window5.winfo_reqwidth()) / 3
        y3 = (window5.winfo_screenheight() - window5.winfo_reqheight()) / 3
        window5.wm_geometry("+%d+%d" % (x3, y3))

        lbl5 = Label(window5, text='Название', anchor='center')
        lbl5.place(relx=0.25, x=10, y=10, anchor='center')

        txt5 = Entry(window5, width=20)
        txt5.place(relx=0.5, x=20, y=10, anchor='center')

        btn8 = Button(window5, text='Удалить', command=del_device_name)
        btn8.place(relx=0.1, x=150, y=40, anchor='center')

    btn5 = Button(window2, text='Перейти', command=call2)
    btn5.place(relx=0.1, x=610, y=140, anchor='center')

    w = Combobox(window2)
    w['values'] = ('Выберите...', 'АГР-72А', 'АГБ-3К', 'АГК-77 (АГ 77)', 'АГР-74', 'ПНП-72-12', 'LUN 1144',
                   '52X1 series', 'РВ-5')
    w.current(0)
    w.grid(column=0, row=1)
    w.bind("<<ComboboxSelected>>", callbackFunc1)  # Привязка функции обратного вызова
    w.bind("<<ComboboxSelected>>", airplane2, '+')
    w.bind("<<ComboboxSelected>>", link2, '+')
    w.pack()

    btn4 = Button(window2, text='Очистить', command=delete_win2)
    btn4.place(relx=0.1, y=400, anchor='center')

    btn6 = Button(window2, text='Добавить прибор', command=add_device)
    btn6.place(relx=0.1, y=300, anchor='center')

    btn7 = Button(window2, text='Удалить прибор', command=del_device)
    btn7.place(relx=0.1, y=350, anchor='center')

    window2.mainloop()


# def img():
#     window2 = Tk()
#     window2.title('Картинки')
#     window2.geometry('1000x800')
#     frame = Frame(window2)
#     frame.grid()
#     canvas = Canvas(window2, height=800, width=700)
#     image = Image.open("1.png")
#     photo = ImageTk.PhotoImage(image)
#     image = canvas.create_image(0, 0, anchor='nw', image=photo)
#     canvas.grid(row=2, column=1)
#     window2.mainloop()

def sensors():
    cursor.execute('SELECT Название FROM Датчики')
    output = cursor.fetchall()
    my_list = []
    for i in output:
        my_list.append(' | '.join(i))
    my_str = '\n'.join(my_list)
    console = Text(width=60, height=20)
    console.place(relx=0.5, y=200, anchor='center')
    console.insert(1.0, my_str)

    window3 = Tk()
    window3.title('Датчики')
    window3.geometry('800x500')
    x2 = (window3.winfo_screenwidth() - window3.winfo_reqwidth()) / 2
    y2 = (window3.winfo_screenheight() - window3.winfo_reqheight()) / 2
    window3.wm_geometry("+%d+%d" % (x2, y2))
    console2 = Text(window3, width=60, height=20)
    console2.place(relx=0.5, y=200, anchor='center')

    console3 = Text(window3, width=10, height=2)
    console3.place(relx=0.5, x=300, y=56, anchor='center')

    console6 = Text(window3, width=15, height=2)
    console6.place(relx=0.5, x=310, y=100, anchor='center')

    def delete_win3():
        console2.delete(1.0, END)
        console3.delete(1.0, END)
        console6.delete(1.0, END)

    def callbackFunc2(dev):
        dev = w.get()
        # messagebox.showinfo("Xiith.com", "You selected " + dev)
        cursor.execute(f"SELECT Описание FROM Датчики WHERE Название = '{dev}'")
        answer = cursor.fetchall()
        console2.insert(1.0, answer)
        window3.title(f'{dev}')

    def airplane(dev):
        my_list3 = []
        my_list1 = []
        my_list2 = []
        dev = w.get()
        cursor.execute(f"SELECT id_датчика FROM Датчики WHERE Название = '{dev}'")
        answerr = cursor.fetchall()
        m = type(answerr)
        # cursor.execute(f"SELECT id_самолета FROM Датчики_Самолеты WHERE id_датчика= '{answerr}'")
        answerr1 = cursor.fetchall()
        # cursor.execute(f"SELECT Название FROM Самолеты WHERE id_самолета = '{answerr1}'")
        # answerr2 = cursor.fetchall()
        console3.insert(1.0, answerr)

    def link1(dev):
        dev = w.get()
        cursor.execute(f"SELECT Ссылка FROM Датчики WHERE Название = '{dev}'")
        an = cursor.fetchall()
        console6.insert(1.0, an)

    def call():
        result = console6.get(1.0, tkinter.END)
        webbrowser.open_new(f"{result}")

    def add_sens():
        def add_sens_db():
            nazv = txt4.get()
            princ = txt5.get()
            opis = txt6.get()
            ssyl = txt7.get()
            cursor.execute(
                f"INSERT INTO Датчики(Название, Принцип_работы, Описание, Ссылка) VALUES('{nazv}', '{princ}', "
                f"'{opis}', '{ssyl}')")
            connect.commit()
            window4.after(300, window4.destroy())
            messagebox.showinfo("Успешно!", "Вы успешно добавили датчик " + nazv)

        window4 = Tk()
        window4.title('Добавить датчик')
        window4.geometry('350x300')
        x3 = (window4.winfo_screenwidth() - window4.winfo_reqwidth()) / 3
        y3 = (window4.winfo_screenheight() - window4.winfo_reqheight()) / 3
        window4.wm_geometry("+%d+%d" % (x3, y3))

        lbl4 = Label(window4, text='Название', anchor='center')
        lbl4.place(relx=0.25, x=-50, y=50, anchor='center')

        txt4 = Entry(window4, width=20)
        txt4.place(relx=0.5, x=-1, y=50, anchor='center')

        lbl5 = Label(window4, text='Принцип работы', anchor='center')
        lbl5.place(relx=0.25, x=-40, y=100, anchor='center')

        txt5 = Entry(window4, width=20)
        txt5.place(relx=0.5, x=-1, y=100, anchor='center')

        lbl6 = Label(window4, text='Описание', anchor='center')
        lbl6.place(relx=0.25, x=-40, y=150, anchor='center')

        txt6 = Entry(window4, width=20)
        txt6.place(relx=0.5, x=-1, y=150, anchor='center')

        lbl7 = Label(window4, text='Ссылка', anchor='center')
        lbl7.place(relx=0.25, x=-40, y=200, anchor='center')

        txt7 = Entry(window4, width=20)
        txt7.place(relx=0.5, x=-1, y=200, anchor='center')

        btn7 = Button(window4, text='Загрузить', command=add_sens_db)
        btn7.place(relx=0.1, x=130, y=250, anchor='center')

    def del_sensor():
        def del_sensor_name():
            name = txt8.get()
            cursor.execute(f"DELETE FROM Датчики WHERE Название = '{name}';")
            window6.after(300, window6.destroy())
            messagebox.showinfo("Успешно!", "Вы успешно удалили дачтик " + name)

        window6 = Tk()
        window6.title('Удалить датчик')
        window6.geometry('400x70')
        x4 = (window6.winfo_screenwidth() - window6.winfo_reqwidth()) / 3
        y4 = (window6.winfo_screenheight() - window6.winfo_reqheight()) / 3
        window6.wm_geometry("+%d+%d" % (x4, y4))

        lbl8 = Label(window6, text='Название', anchor='center')
        lbl8.place(relx=0.25, x=10, y=10, anchor='center')

        txt8 = Entry(window6, width=20)
        txt8.place(relx=0.5, x=20, y=10, anchor='center')

        btn10 = Button(window6, text='Удалить', command=del_sensor_name)
        btn10.place(relx=0.1, x=150, y=40, anchor='center')

    btn5 = Button(window3, text='Перейти', command=call)
    btn5.place(relx=0.1, x=610, y=140, anchor='center')

    w = Combobox(window3)
    w['values'] = ('Выберите...', 'Jpi Edm 700', 'Тросовый датчик MH120', 'Индуктивный датчик перемещения RL',
                   'Лазерный датчик RAS-T5', 'ПВД 15144', 'Flymaster live sd 3g',
                   'Jpi Induction Air & Compressor Temperature Probes')
    w.current(0)
    w.grid(column=0, row=1)
    w.bind("<<ComboboxSelected>>", callbackFunc2)  # Привязка функции обратного вызова
    w.bind("<<ComboboxSelected>>", airplane, '+')
    w.bind("<<ComboboxSelected>>", link1, '+')
    w.pack()

    btn4 = Button(window3, text='Очистить', command=delete_win3)
    btn4.place(relx=0.1, y=400, anchor='center')

    btn6 = Button(window3, text='Добавить датчик', command=add_sens)
    btn6.place(relx=0.1, y=300, anchor='center')

    btn8 = Button(window3, text='Удалить датчик', command=del_sensor)
    btn8.place(relx=0.1, y=350, anchor='center')

    window3.mainloop()


def DB():  # Функция начала работы с БД
    def delete_win1():
        console2 = Text(window1, width=60, height=20)
        console2.place(relx=0.5, y=200, anchor='center')

    window1 = Tk()
    window1.title('Измерительные преобразователи')
    window1.geometry('800x500')
    x1 = (window1.winfo_screenwidth() - window1.winfo_reqwidth()) / 3.5
    y1 = (window1.winfo_screenheight() - window1.winfo_reqheight()) / 3.5
    window1.wm_geometry("+%d+%d" % (x1, y1))

    lbl3 = Label(window1, text="База данных по измерительным преобразователям", font=("Arial Bold", 12))
    lbl3.place(relx=0.5, y=15, anchor='center')

    btn1 = Button(window1, text='Самолеты', command=na)
    btn1.place(relx=0.1, y=200, anchor='center')

    btn2 = Button(window1, text='Приборы', command=devices)
    btn2.place(relx=0.1, y=250, anchor='center')

    btn3 = Button(window1, text='Очистить', command=delete_win1)
    btn3.place(relx=0.1, y=350, anchor='center')

    btn4 = Button(window1, text='Датчики', command=sensors)
    btn4.place(relx=0.1, y=300, anchor='center')

    window1.mainloop()


window.mainloop()
