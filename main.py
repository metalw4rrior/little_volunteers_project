import tkinter as tk
from tkinter import ttk
from gui import VolunteerApp
from db import setup_database, get_volunteer_names

def main():
    setup_database()
    namelist = get_volunteer_names()

    window = tk.Tk()
    app = VolunteerApp(window, namelist)
    window.mainloop()

if __name__ == "__main__":
    main()
