#---------------------------------------Govnocoded by metaw4rrior and revan------------------------------------------------------------------------------
import sqlite3 as sl
import tkinter as tk
from tkinter import ttk, DISABLED, NORMAL
from tkinter import messagebox as mb
from tkinter.ttk import Combobox
import re

def okno_baza():

    #--------------------------------подключение к базе--------------------------------------
    con = sl.connect('humans2.db')
    #--------------------------------проверка базы и данных в ней--------------------------------------
    with con:
        data = con.execute("select count(*) from sqlite_master where type='table' and name='users'")
        for row in data:
            if row[0] == 0:
                with con:    
                    con.execute("""
                        CREATE TABLE users (
                        name VARCHAR PRIMARY KEY,
                        inn INTEGER,
                        passport VARCHAR,
                        snils VARCHAR,
                        birthday DATE
                        role VARCHAR);""")
    #-----------------------------данные для таблицы с юзерами------------------------------------------
    namelist = []
    with con:
        data = con.execute("SELECT name FROM users")
        for row in data:
            namelist.append(*row)
    #---------------------------запуск родительского окна------------------------------------------------------
    window = tk.Tk()
    window.title('Волонтеры')
    window.geometry('900x900')
    window.configure(bg='#FFFFF0')
    #-----------конфиг фреймов-----------------------------------------------
    f2 = tk.Frame(window,width=900, height=400,bg='#FFFFF0')
    f2.pack()
    f3 = tk.Frame(window,width=900, height=400,bg='#FFFFF0')
    f3.pack()
    f1 = tk.Frame(window,width=600, height=400,bg='#FFFFF0')
    f1.pack()
    #-------------заголовок страницы-------------------------------------------------------
    head_label = ttk.Label(f2,text="Волонтеры для помощи вашей организации", font="Courier 28 italic ",background="#008B8B")
    head_label.pack()


    #-------------таблица с волонтерами--------------------------------------------------
    columns = ("fam","name","othestvo")
    table = ttk.Treeview(f1,columns=columns, show="headings")
    table.heading("fam", text="Фамилия")
    table.heading("name", text="Имя")
    table.heading("othestvo", text="Отчество")
    table.pack(fill="both", expand=1)
    table.column("#1", width=200)
    table.column("#2", width=200)
    table.column("#3", width=200)
    for person in namelist:
        table.insert("","end", values=person)
    table.pack(fill="both", expand=1)
    #----------------комбобокс------------------------------------------------------
    text_f3 = tk.Label(f3, text = "Выберите нужного вам волонтера",font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
    text_f3.pack()

    combo = Combobox(f3,background = '#696969',foreground = '#008B8B',font=("Courier", 14, "italic"),height=15)  
    combo['values'] = ('Сотрудник штаба', 'Переводчик', 'Население', 'Аташе Россия', 'Аташе заграница',
    'Регистрация', 'Логистика', 'Сотрудник столовой', 'Ответственные по направлениям','Награждение','СМИ')  
    combo.current(0)
    combo.pack()
    text1_f3 = tk.Label(f3, text = "В таблице представлены все наши волонтеры",font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
    text1_f3.pack()
    #-------------------------------------функции вызова окон, в каждой функции свое всплывающее окно.--------------------------------------------------------------
    def stab(records):
        sqlite_connection = sl.connect('humans2.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from users where role like 'Штаб'"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего волонтеров:  ", len(records))
        stab_stroka = []
        stab_stroka_bez_personalki=[]
        for row in records:
            stab_stroka.append("ФИО: " + row[0]+ '\n')
            stab_stroka.append('ИНН: '+ str(row[1])+ '\n')
            stab_stroka.append('Паспорт: '+row[2]+ '\n')
            stab_stroka.append('Снилс: '+row[3]+ '\n')
            stab_stroka.append('Дата рождения: '+str(row[4])+ '\n')
        for row in records:
            stab_stroka_bez_personalki.append("Волонтер:  " + row[0]+ '\n')
        msg_stab_bez_personalki=''
        msg_stab_bez_personalki = msg_stab_bez_personalki.join(stab_stroka_bez_personalki)
        msg_stab = ''
        msg_stab = msg_stab.join(stab_stroka)
        stab_window = tk.Tk()
        stab_window.title('Запрошенные данные')
        stab_window.geometry('600x800')
        stab_window.configure(bg='#FFFFF0')
        def clicked_stab():
            text_bez_personalki.configure(text = msg_stab)
        but_stab = tk.Button(stab_window, text="Запросить полные данные",command = clicked_stab, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic"))
        but_stab.grid(column=1,row = 2)
        text_bez_personalki = tk.Label(stab_window,text = msg_stab_bez_personalki,font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
        text_bez_personalki.grid(column = 1, row = 1)
        cursor.close()
        stab_window.mainloop()
    def perevodchik(records):
        sqlite_connection = sl.connect('humans2.db')
        cursor = sqlite_connection.cursor()
        sqlite_select_query = """SELECT * from users where role like 'Переводчик'"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего волонтеров:  ", len(records))
        stab_stroka = []
        stab_stroka_bez_personalki=[]
        for row in records:
            stab_stroka.append("ФИО: " + row[0]+ '\n')
            stab_stroka.append('ИНН: '+ str(row[1])+ '\n')
            stab_stroka.append('Паспорт: '+row[2]+ '\n')
            stab_stroka.append('Снилс: '+row[3]+ '\n')
            stab_stroka.append('Дата рождения: '+str(row[4])+ '\n')
        for row in records:
            stab_stroka_bez_personalki.append("Волонтер:  " + row[0]+ '\n')
        msg_stab_bez_personalki=''
        msg_stab_bez_personalki = msg_stab_bez_personalki.join(stab_stroka_bez_personalki)
        msg_stab = ''
        msg_stab = msg_stab.join(stab_stroka)
        stab_window = tk.Tk()
        stab_window.title('Запрошенные данные')
        stab_window.geometry('600x800')
        stab_window.configure(bg='#FFFFF0')
        def clicked_stab():
            text_bez_personalki.configure(text = msg_stab)
        but_stab = tk.Button(stab_window, text="Запросить полные данные",command = clicked_stab, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic"))
        but_stab.grid(column=1,row = 2)
        text_bez_personalki = tk.Label(stab_window,text = msg_stab_bez_personalki,font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
        text_bez_personalki.grid(column = 1, row = 1)
        cursor.close()
        stab_window.mainloop()
    def nacelen(records):
        sqlite_connection = sl.connect('humans2.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from users where role like 'Население'"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего волонтеров:  ", len(records))
        stab_stroka = []
        stab_stroka_bez_personalki=[]
        for row in records:
            stab_stroka.append("ФИО: " + row[0]+ '\n')
            stab_stroka.append('ИНН: '+ str(row[1])+ '\n')
            stab_stroka.append('Паспорт: '+row[2]+ '\n')
            stab_stroka.append('Снилс: '+row[3]+ '\n')
            stab_stroka.append('Дата рождения: '+str(row[4])+ '\n')
        for row in records:
            stab_stroka_bez_personalki.append("Волонтер:  " + row[0]+ '\n')
        msg_stab_bez_personalki=''
        msg_stab_bez_personalki = msg_stab_bez_personalki.join(stab_stroka_bez_personalki)
        msg_stab = ''
        msg_stab = msg_stab.join(stab_stroka)
        stab_window = tk.Tk()
        stab_window.title('Запрошенные данные')
        stab_window.geometry('600x800')
        stab_window.configure(bg='#FFFFF0')
        def clicked_stab():
            text_bez_personalki.configure(text = msg_stab)
        but_stab = tk.Button(stab_window, text="Запросить полные данные",command = clicked_stab, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic"))
        but_stab.grid(column=1,row = 2)
        text_bez_personalki = tk.Label(stab_window,text = msg_stab_bez_personalki,font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
        text_bez_personalki.grid(column = 1, row = 1)
        cursor.close()
        stab_window.mainloop()
    def atache_rus(records):
        sqlite_connection = sl.connect('humans2.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from users where role like 'Аташе'"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего волонтеров:  ", len(records))
        stab_stroka = []
        stab_stroka_bez_personalki=[]
        for row in records:
            stab_stroka.append("ФИО: " + row[0]+ '\n')
            stab_stroka.append('ИНН: '+ str(row[1])+ '\n')
            stab_stroka.append('Паспорт: '+row[2]+ '\n')
            stab_stroka.append('Снилс: '+row[3]+ '\n')
            stab_stroka.append('Дата рождения: '+str(row[4])+ '\n')
        for row in records:
            stab_stroka_bez_personalki.append("Волонтер:  " + row[0]+ '\n')
        msg_stab_bez_personalki=''
        msg_stab_bez_personalki = msg_stab_bez_personalki.join(stab_stroka_bez_personalki)
        msg_stab = ''
        msg_stab = msg_stab.join(stab_stroka)
        stab_window = tk.Tk()
        stab_window.title('Запрошенные данные')
        stab_window.geometry('600x800')
        stab_window.configure(bg='#FFFFF0')
        def clicked_stab():
            text_bez_personalki.configure(text = msg_stab)
        but_stab = tk.Button(stab_window, text="Запросить полные данные",command = clicked_stab, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic"))
        but_stab.grid(column=1,row = 2)
        text_bez_personalki = tk.Label(stab_window,text = msg_stab_bez_personalki,font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
        text_bez_personalki.grid(column = 1, row = 1)
        cursor.close()
        stab_window.mainloop()
    def atache_zagran(records):
        sqlite_connection = sl.connect('humans2.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from users where role like 'Аташе_и'"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего волонтеров:  ", len(records))
        stab_stroka = []
        stab_stroka_bez_personalki=[]
        for row in records:
            stab_stroka.append("ФИО: " + row[0]+ '\n')
            stab_stroka.append('ИНН: '+ str(row[1])+ '\n')
            stab_stroka.append('Паспорт: '+row[2]+ '\n')
            stab_stroka.append('Снилс: '+row[3]+ '\n')
            stab_stroka.append('Дата рождения: '+str(row[4])+ '\n')
        for row in records:
            stab_stroka_bez_personalki.append("Волонтер:  " + row[0]+ '\n')
        msg_stab_bez_personalki=''
        msg_stab_bez_personalki = msg_stab_bez_personalki.join(stab_stroka_bez_personalki)
        msg_stab = ''
        msg_stab = msg_stab.join(stab_stroka)
        stab_window = tk.Tk()
        stab_window.title('Запрошенные данные')
        stab_window.geometry('600x800')
        stab_window.configure(bg='#FFFFF0')
        def clicked_stab():
            text_bez_personalki.configure(text = msg_stab)
        but_stab = tk.Button(stab_window, text="Запросить полные данные",command = clicked_stab, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic"))
        but_stab.grid(column=1,row = 2)
        text_bez_personalki = tk.Label(stab_window,text = msg_stab_bez_personalki,font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
        text_bez_personalki.grid(column = 1, row = 1)
        cursor.close()
        stab_window.mainloop()
    def registration(records):
        sqlite_connection = sl.connect('humans2.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from users where role like 'Регистрация'"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего волонтеров:  ", len(records))
        stab_stroka = []
        stab_stroka_bez_personalki=[]
        for row in records:
            stab_stroka.append("ФИО: " + row[0]+ '\n')
            stab_stroka.append('ИНН: '+ str(row[1])+ '\n')
            stab_stroka.append('Паспорт: '+row[2]+ '\n')
            stab_stroka.append('Снилс: '+row[3]+ '\n')
            stab_stroka.append('Дата рождения: '+str(row[4])+ '\n')
        for row in records:
            stab_stroka_bez_personalki.append("Волонтер:  " + row[0]+ '\n')
        msg_stab_bez_personalki=''
        msg_stab_bez_personalki = msg_stab_bez_personalki.join(stab_stroka_bez_personalki)
        msg_stab = ''
        msg_stab = msg_stab.join(stab_stroka)
        stab_window = tk.Tk()
        stab_window.title('Запрошенные данные')
        stab_window.geometry('600x800')
        stab_window.configure(bg='#FFFFF0')
        def clicked_stab():
            text_bez_personalki.configure(text = msg_stab)
        but_stab = tk.Button(stab_window, text="Запросить полные данные",command = clicked_stab, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic"))
        but_stab.grid(column=1,row = 2)
        text_bez_personalki = tk.Label(stab_window,text = msg_stab_bez_personalki,font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
        text_bez_personalki.grid(column = 1, row = 1)
        cursor.close()
        stab_window.mainloop()
    def logistic(records):
        sqlite_connection = sl.connect('humans2.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from users where role like 'Логистика'"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего волонтеров:  ", len(records))
        stab_stroka = []
        stab_stroka_bez_personalki=[]
        for row in records:
            stab_stroka.append("ФИО: " + row[0]+ '\n')
            stab_stroka.append('ИНН: '+ str(row[1])+ '\n')
            stab_stroka.append('Паспорт: '+row[2]+ '\n')
            stab_stroka.append('Снилс: '+row[3]+ '\n')
            stab_stroka.append('Дата рождения: '+str(row[4])+ '\n')
        for row in records:
            stab_stroka_bez_personalki.append("Волонтер:  " + row[0]+ '\n')
        msg_stab_bez_personalki=''
        msg_stab_bez_personalki = msg_stab_bez_personalki.join(stab_stroka_bez_personalki)
        msg_stab = ''
        msg_stab = msg_stab.join(stab_stroka)
        stab_window = tk.Tk()
        stab_window.title('Запрошенные данные')
        stab_window.geometry('600x800')
        stab_window.configure(bg='#FFFFF0')
        def clicked_stab():
            text_bez_personalki.configure(text = msg_stab)
        but_stab = tk.Button(stab_window, text="Запросить полные данные",command = clicked_stab, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic"))
        but_stab.grid(column=1,row = 2)
        text_bez_personalki = tk.Label(stab_window,text = msg_stab_bez_personalki,font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
        text_bez_personalki.grid(column = 1, row = 1)
        cursor.close()
        stab_window.mainloop()
    def stolovaya(records):
        sqlite_connection = sl.connect('humans2.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from users where role like 'Столовая'"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего волонтеров:  ", len(records))
        stab_stroka = []
        stab_stroka_bez_personalki=[]
        for row in records:
            stab_stroka.append("ФИО: " + row[0]+ '\n')
            stab_stroka.append('ИНН: '+ str(row[1])+ '\n')
            stab_stroka.append('Паспорт: '+row[2]+ '\n')
            stab_stroka.append('Снилс: '+row[3]+ '\n')
            stab_stroka.append('Дата рождения: '+str(row[4])+ '\n')
        for row in records:
            stab_stroka_bez_personalki.append("Волонтер:  " + row[0]+ '\n')
        msg_stab_bez_personalki=''
        msg_stab_bez_personalki = msg_stab_bez_personalki.join(stab_stroka_bez_personalki)
        msg_stab = ''
        msg_stab = msg_stab.join(stab_stroka)
        stab_window = tk.Tk()
        stab_window.title('Запрошенные данные')
        stab_window.geometry('600x800')
        stab_window.configure(bg='#FFFFF0')
        def clicked_stab():
            text_bez_personalki.configure(text = msg_stab)
        but_stab = tk.Button(stab_window, text="Запросить полные данные",command = clicked_stab, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic"))
        but_stab.grid(column=1,row = 2)
        text_bez_personalki = tk.Label(stab_window,text = msg_stab_bez_personalki,font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
        text_bez_personalki.grid(column = 1, row = 1)
        cursor.close()
        stab_window.mainloop()
    def otv_po_napr(records):
        sqlite_connection = sl.connect('humans2.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from users where role like 'Ответственный'"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего волонтеров:  ", len(records))
        stab_stroka = []
        stab_stroka_bez_personalki=[]
        for row in records:
            stab_stroka.append("ФИО: " + row[0]+ '\n')
            stab_stroka.append('ИНН: '+ str(row[1])+ '\n')
            stab_stroka.append('Паспорт: '+row[2]+ '\n')
            stab_stroka.append('Снилс: '+row[3]+ '\n')
            stab_stroka.append('Дата рождения: '+str(row[4])+ '\n')
        for row in records:
            stab_stroka_bez_personalki.append("Волонтер:  " + row[0]+ '\n')
        msg_stab_bez_personalki=''
        msg_stab_bez_personalki = msg_stab_bez_personalki.join(stab_stroka_bez_personalki)
        msg_stab = ''
        msg_stab = msg_stab.join(stab_stroka)
        stab_window = tk.Tk()
        stab_window.title('Запрошенные данные')
        stab_window.geometry('600x800')
        stab_window.configure(bg='#FFFFF0')
        def clicked_stab():
            text_bez_personalki.configure(text = msg_stab)
        but_stab = tk.Button(stab_window, text="Запросить полные данные",command = clicked_stab, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic"))
        but_stab.grid(column=1,row = 2)
        text_bez_personalki = tk.Label(stab_window,text = msg_stab_bez_personalki,font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
        text_bez_personalki.grid(column = 1, row = 1)
        cursor.close()
        stab_window.mainloop()
    def smi(records):
        sqlite_connection = sl.connect('humans2.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from users where role like 'СМИ'"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего волонтеров:  ", len(records))
        stab_stroka = []
        stab_stroka_bez_personalki=[]
        for row in records:
            stab_stroka.append("ФИО: " + row[0]+ '\n')
            stab_stroka.append('ИНН: '+ str(row[1])+ '\n')
            stab_stroka.append('Паспорт: '+row[2]+ '\n')
            stab_stroka.append('Снилс: '+row[3]+ '\n')
            stab_stroka.append('Дата рождения: '+str(row[4])+ '\n')
        for row in records:
            stab_stroka_bez_personalki.append("Волонтер:  " + row[0]+ '\n')
        msg_stab_bez_personalki=''
        msg_stab_bez_personalki = msg_stab_bez_personalki.join(stab_stroka_bez_personalki)
        msg_stab = ''
        msg_stab = msg_stab.join(stab_stroka)
        stab_window = tk.Tk()
        stab_window.title('Запрошенные данные')
        stab_window.geometry('600x800')
        stab_window.configure(bg='#FFFFF0')
        def clicked_stab():
            text_bez_personalki.configure(text = msg_stab)
        but_stab = tk.Button(stab_window, text="Запросить полные данные",command = clicked_stab, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic"))
        but_stab.grid(column=1,row = 2)
        text_bez_personalki = tk.Label(stab_window,text = msg_stab_bez_personalki,font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
        text_bez_personalki.grid(column = 1, row = 1)
        cursor.close()
        stab_window.mainloop()
    def nagrajdenie(records):
        sqlite_connection = sl.connect('humans2.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from users where role like 'Награждение'"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего волонтеров:  ", len(records))
        stab_stroka = []
        stab_stroka_bez_personalki=[]
        for row in records:
            stab_stroka.append("ФИО: " + row[0]+ '\n')
            stab_stroka.append('ИНН: '+ str(row[1])+ '\n')
            stab_stroka.append('Паспорт: '+row[2]+ '\n')
            stab_stroka.append('Снилс: '+row[3]+ '\n')
            stab_stroka.append('Дата рождения: '+str(row[4])+ '\n')
        for row in records:
            stab_stroka_bez_personalki.append("Волонтер:  " + row[0]+ '\n')
        msg_stab_bez_personalki=''
        msg_stab_bez_personalki = msg_stab_bez_personalki.join(stab_stroka_bez_personalki)
        msg_stab = ''
        msg_stab = msg_stab.join(stab_stroka)
        stab_window = tk.Tk()
        stab_window.title('Запрошенные данные')
        stab_window.geometry('600x800')
        stab_window.configure(bg='#FFFFF0')
        def clicked_stab():
            text_bez_personalki.configure(text = msg_stab)
        but_stab = tk.Button(stab_window, text="Запросить полные данные",command = clicked_stab, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic"))
        but_stab.grid(column=1,row = 2)
        text_bez_personalki = tk.Label(stab_window,text = msg_stab_bez_personalki,font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
        text_bez_personalki.grid(column = 1, row = 1)
        cursor.close()
        stab_window.mainloop()
    #-------------------------------функция выборки данных с ввода комбобокса-----------------------------------------------
    def zapros_volontera():
        if combo.get() == "Сотрудник штаба":
            stab(1)
        elif combo.get()=="Переводчик":
            perevodchik(1)
        elif combo.get() == 'Аташе Россия':
            atache_rus(1)
        elif combo.get() == 'Население':
            nacelen(1)
        elif combo.get() == 'Аташе заграница':
            atache_zagran(1)
        elif combo.get() == 'Регистрация':
            registration(1)
        elif combo.get() == 'Логистика':
            logistic(1)
        elif combo.get() == 'Сотрудник столовой':
            stolovaya(1)
        elif combo.get() == 'Ответственные по направлениям':
            otv_po_napr(1)     
        elif combo.get() == 'СМИ':
            smi(1)
        elif combo.get() == 'Награждение':
            nagrajdenie(1)
        else:
            mb.showwarning('Данные введены неверно!','Выберите данные из списка!!!')
    #-------------------------------------------кнопка запроса волонтеров---------------------------------------------------
    button_zapros = tk.Button(f1, text="Запросить волонтера", bg="#B2DFDB", fg="#000000",command = zapros_volontera,font=("Courier", 14, "italic"))
    button_zapros.pack()
    #------------------------------------кнопка вызова окна регистрации-----------------------------------------------------
    # def reg():
    #     registr.reg_file()
    # button_zapros = tk.Button(f1, text="Зарегистрировать волонтера", bg="#B2DFDB", fg="#000000",command = reg, font=("Courier", 14, "italic"))
    # button_zapros.pack()

    window.mainloop()


def reg_file():
    ###################### ДАННЫЕ В БД ############################
    def registration():
        # entry_surname.dele(0, tk.END)
        surname = entry_surname.get()
        name = entry_name.get()
        otchestvo = entry_otchestvo.get()
        date_of_birth = entry_date.get()
        passport = entry_passport.get()
        snils = entry_snils.get()
        inn = entry_inn.get()
        role = role_choise.get()
        fio = surname+" "+name+" "+otchestvo
        data_in_sqlite = [fio,inn,passport,snils,date_of_birth,role]   #### <------ ТУТ ДАННЫЕ В БД ####
        x = proverka(surname, name, otchestvo, date_of_birth, passport, snils, inn)
        if x == 7:
            conn = sl.connect(r"humans2.db")      #### <----- ТУТ ПРОПИСАТЬ ПУТЬ ДО БД
            cur = conn.cursor()
            cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?);", data_in_sqlite)
            conn.commit()
            mb.showinfo("Поздравляем", "Вы успешно прошли регистрацию")



    ###################### ОКНА УВЕДОМЛЕНИЙ ########################

    def soglasie():
        mb.showinfo(title="Согласие на обработу персональных данных", 
    message="""Я даю свое согласие на обработку моих персональных данных, включающих фамилию, имя, отчество, страховой номер индивидуального лицевого счета в Пенсионном фонде России (СНИЛС), ИНН, а также право осуществлять все действия (операции) с моими персональными данными, включая сбор, систематизацию, накопление, хранение, обновление, изменение, использование, обезличивание, блокирование,уничтожение.""",
    detail="""Настоящее согласие на обработку персональных данных может быть отозвано в порядке,установленном Федеральным законом Российской Федерации от 27.07.2006 № 152-ФЗ «О персональных данных».""") #sogl)

    def is_valid_fio(newval):
        result = re.match(r"^[А-Я]{,1}[а-я]{,15}$", newval) is not None
        return result

    def how_to_date():     
        mb.showinfo("Как прописывать дату", "Прописывать в таком виде\n\"1980-12-31\"")

    def how_to_passport():     
        mb.showinfo("Как прописать дынне паспорта", "Прописывать в таком виде\n\"7123 345123\"")

    def how_to_snils():     
        mb.showinfo("Как прописывать снилс", "Прописывать в таком виде\n\"123-456-789 12\"")

    def how_to_fio():     
        mb.showinfo("Error", "Неправильно прописанное ФИО")

    def something_is_wrong():
        mb.showinfo("Error", "Что-то не так")

    ############### САМАЯ ХУДШАЯ ПРОВЕРКА ВСЕХ ВРЕМЕН #################

    def proverka(surname, name, otchestvo, date_of_birth, passport, snils, inn):
        x = 0
        match = re.fullmatch(r'^[А-Я][а-яА-Я]+$', surname)
        if match: x+=1
        else: how_to_fio()
        match = re.fullmatch(r'^[А-Я][а-яА-Я]+$', name)
        if match: x+=1
        else: how_to_fio()
        match = re.fullmatch(r'^[А-Я][а-яА-Я]+$', otchestvo)
        if match: x+=1
        else: how_to_fio()
        match = re.fullmatch(r'(19|20)\d{2}-\d{2}-\d{2}', date_of_birth)
        if match: x+=1
        else: how_to_date()
        match = re.fullmatch(r'^\d{4}\s\d{6}$', passport)
        if match: x+=1
        else: how_to_passport()
        match = re.fullmatch(r'^\d{3}-\d{3}-\d{3}\s\d{2}$', snils)
        if match: x+=1
        else: how_to_snils()
        match = re.fullmatch(r'\d{12}', inn)
        if match: x+=1
        else: something_is_wrong()
        return x

    ################ ГАЛОЧКА ДЛЯ ТЕХ КТО ПРОЧИТАЛ ###################
    def check():
        if galochka_state.get() == 'yes':
            btn_submit.configure(state=NORMAL)
        else:
            btn_submit.configure(state=DISABLED)


    ##################### РЕНДЕР ОКНА ###############################
    root = tk.Tk()
    root.title("Регистрация")
    root.geometry('1000x800')
    root.configure(bg='#FFFFF0')

    ################### НЕВИДИМАЯ ТАБЛИЦА ###########################
    text_glava = tk.Label(root, text = "GOVNOCODE IT.2w",font=("Courier", 24, "italic"),background="#B2DFDB",foreground="#000000").pack()
    text_glava_2 = tk.Label(root, text = "Если вы хотите быть в нашей базе волнтеров, пожалуйста, пройдите регистрацию",font=("Courier", 15, "italic"),background="#B2DFDB",foreground="#000000").pack()
    frm_form = tk.Frame(master=root, relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack()
    ########################### ФИО ################################

    fio_check = (root.register(is_valid_fio), "%P")

    label_surname = tk.Label(master=frm_form, text="Фамилия")
    label_surname.grid(row=0, column=0)
    entry_surname = ttk.Entry(master=frm_form, width=50, validate="key", validatecommand=fio_check)
    entry_surname.grid(row=0, column=1)

    label_name = tk.Label(master=frm_form, text="Имя")
    label_name.grid(row=1, column=0)
    entry_name = ttk.Entry(master=frm_form, width=50, validate="key", validatecommand=fio_check)
    entry_name.grid(row=1, column=1)

    label_otchestvo = tk.Label(master=frm_form, text="Отчество")
    label_otchestvo.grid(row=2, column=0)
    entry_otchestvo = ttk.Entry(master=frm_form, width=50, validate="key", validatecommand=fio_check)
    entry_otchestvo.grid(row=2, column=1)

    ######################## ДАТА РОЖДЕНИЯ #########################

    btn_date = tk.Button(master=frm_form, text="Дата рождения*", relief=tk.FLAT, command=how_to_date)
    btn_date.grid(row=4, column=0)
    entry_date = tk.Entry(master=frm_form, width=50)
    entry_date.grid(row=4, column=1)


    ######################## ПАСПОРТ ################################

    btn_passport = tk.Button(master=frm_form, text="Паспорт*", relief=tk.FLAT, command=how_to_passport)
    btn_passport.grid(row=5, column=0)
    entry_passport = tk.Entry(master=frm_form, width=50)
    entry_passport.grid(row=5, column=1)

    ######################### СНИЛС #################################

    btn_snils = tk.Button(master=frm_form, text="Снилс*", relief=tk.FLAT, command=how_to_snils)
    btn_snils.grid(row=6, column=0)
    entry_snils = tk.Entry(master=frm_form, width=50)
    entry_snils.grid(row=6, column=1)

    ########################## ИНН #################################

    label_inn = tk.Label(master=frm_form, text="ИНН")
    label_inn.grid(row=7, column=0)
    entry_inn = tk.Entry(master=frm_form, width=50)
    entry_inn.grid(row=7, column=1)

    ########################## РОЛЬ ################################

    roles = ["Население", "Переводчик", "Штаб", "Аташе","Аташе_и", "Логистика", "Столовая",  "Награждение", "Регистрация", "СМИ"]
    # role_menu = ttk.Combobox(frm_form, values=roles, width=50)
    # role_menu.grid(row=9,column=1)
    label_role = tk.Label(master=frm_form, text='Направление')
    label_role.grid(row=9, column=0)
    role_choise = tk.StringVar(frm_form)
    role_choise.set(roles[0])
    role_menu = tk.OptionMenu(frm_form, role_choise, *roles)
    role_menu.config(width=45)
    role_menu.grid(row=9,column=1)

    ################## ЕЩЕ НЕВИДИМАЯ ТАБЛИЦА #####################

    frm_buttons = tk.Frame(master=root,bg='#FFFFF0')
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
    btn_registratoin_vibor_2 = tk.Button(root,text = 'Мне нужны волонтеры, я организатор мероприятия', command = okno_baza, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic")).pack()
    #################### КНОПОЧКИ И ГАЛОЧКИ ######################


    btn_soglasie = tk.Button(master=frm_buttons, text="Я прочитал(а) соглашение", fg="blue", relief=tk.FLAT, command=soglasie,font=("Courier", 14, "italic"),background="#B2DFDB",foreground="#000000")
    btn_soglasie.pack(side=tk.LEFT, padx=10)

    galochka_state = tk.StringVar()
    galochka_state.set('no')
    galochka = tk.Checkbutton(master=frm_buttons, command=check, variable=galochka_state, offvalue='no', onvalue='yes')
    galochka.pack(side=tk.LEFT)


    btn_submit = tk.Button(master=frm_buttons, text="Зарегистрироваться", command=registration, state=DISABLED, bg="#B2DFDB", fg="#000000",font=("Courier", 14, "italic"))
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
    check()
    root.mainloop()
reg_file()
