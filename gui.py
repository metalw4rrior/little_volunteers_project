import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox
from db import get_volunteer_data_by_role

class VolunteerApp:
    def __init__(self, window, namelist):
        self.window = window
        self.window.title('Волонтеры')
        self.window.geometry('900x900')
        self.window.configure(bg='#FFFFF0')

        self.setup_frames()
        self.setup_header()
        self.setup_table(namelist)
        self.setup_combobox()

    def setup_frames(self):
        self.f2 = tk.Frame(self.window, width=900, height=400, bg='#FFFFF0')
        self.f2.pack()
        self.f3 = tk.Frame(self.window, width=900, height=400, bg='#FFFFF0')
        self.f3.pack()
        self.f1 = tk.Frame(self.window, width=600, height=400, bg='#FFFFF0')
        self.f1.pack()

    def setup_header(self):
        head_label = ttk.Label(self.f2, text="Волонтеры для помощи вашей организации", font="Courier 28 italic ", background="#008B8B")
        head_label.pack()

    def setup_table(self, namelist):
        columns = ("fam", "name", "othestvo")
        self.table = ttk.Treeview(self.f1, columns=columns, show="headings")
        self.table.heading("fam", text="Фамилия")
        self.table.heading("name", text="Имя")
        self.table.heading("othestvo", text="Отчество")
        self.table.pack(fill="both", expand=1)
        self.table.column("#1", width=200)
        self.table.column("#2", width=200)
        self.table.column("#3", width=200)
        for person in namelist:
            self.table.insert("", "end", values=person)
        self.table.pack(fill="both", expand=1)

    def setup_combobox(self):
        text_f3 = tk.Label(self.f3, text="Выберите нужного вам волонтера", font=("Courier", 14, "italic"), background="#B2DFDB", foreground="#000000")
        text_f3.pack()

        self.combo = Combobox(self.f3, background='#696969', foreground='#008B8B', font=("Courier", 14, "italic"), height=15)
        self.combo['values'] = ('Сотрудник штаба', 'Переводчик', 'Население', 'Аташе Россия', 'Аташе заграница', 'Регистрация', 'Логистика', 'Сотрудник столовой', 'Ответственные по направлениям', 'Награждение', 'СМИ')
        self.combo.current(0)
        self.combo.pack()
        self.combo.bind("<<ComboboxSelected>>", self.on_role_selected)

        text1_f3 = tk.Label(self.f3, text="В таблице представлены все наши волонтеры", font=("Courier", 14, "italic"), background="#B2DFDB", foreground="#000000")
        text1_f3.pack()

    def on_role_selected(self, event):
        role = self.combo.get()
        records = get_volunteer_data_by_role(role)
        self.show_volunteer_data(records)

    def show_volunteer_data(self, records):
        msg = ''
        for row in records:
            msg += f"ФИО: {row[0]}\nИНН: {row[1]}\nПаспорт: {row[2]}\nСнилс: {row[3]}\nДата рождения: {row[4]}\n\n"
        messagebox.showinfo("Запрошенные данные", msg)
