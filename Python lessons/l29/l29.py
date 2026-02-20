# from tkinter import *
#
# def clicked():
#     lbl.configure(text="I did ask you...")
#
# window = Tk()
# window.title("Добро пожаловать в приложение PythonRu")
# window.geometry("600x300")
# lbl = Label(window, text="Hi everyone", font=("Helvetica", 50, "bold"))
# lbl.pack()
# lbl.grid(row=0, column=0)
# btn = Button(window, text="Don't push!", command=clicked)
# btn.grid(row=0, column=1)
# window.mainloop()



# from tkinter import *
#
# window = Tk()
# window.title("Подсчет строк")
# window.geometry("500x300")
#
# btn_select = Button(window, text="Выбрать папку")
# btn_count = Button(window, text="Отобразить количество строк")
#
# label_result = Label(window, text="Количество строк = 0", fg="black", font=("Helvetica", 30, "bold"))
#
# btn_select.grid(row=0, column=0)
# btn_count.grid(row=0, column=1)
# label_result.grid(row=1, column=0, columnspan=2, pady=40)
#
# window.mainloop()



# import tkinter as tk
#
#
# class Main(tk.Frame):
#     def __init__(self, root):
#         super().__init__(root)
#         self.init_main()
#
#     def init_main(self):
#         toolbar = tk.Frame(self, bg="#d7d8e0", bd=2)
#         toolbar.pack(side=tk.TOP, fill=tk.X)
#
#         btn_open_dialog = tk.Button(
#             toolbar,
#             text="Добавить позицию",
#             command=self.open_dialog,
#             bg="#d7d8e0",
#             bd=2
#         )
#         btn_open_dialog.pack(side=tk.LEFT)
#
#     def open_dialog(self):
#         # ПЕРЕДАЁМ родительское окно явно
#         Child(self.master)
#
#
# class Child(tk.Toplevel):
#     def __init__(self, parent):
#         # parent — это root
#         super().__init__(parent)
#
#         self.title("Добавить доходы/расходы")
#         self.geometry("400x220+400+300")
#         self.resizable(False, False)
#
#         self.transient(parent)
#         # Дочернее окно всегда поверх родителя
#
#         self.grab_set()
#         # Блокируем взаимодействие с главным окном,
#         # пока открыто это
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#
#     app = Main(root)
#     app.pack()
#
#     root.title("Домашние финансы")
#     root.geometry("650x450+300+200")
#     root.resizable(False, False)
#
#     root.mainloop()



# from PyQt6.QtWidgets import QApplication, QPushButton
#
# import sys
#
# app = QApplication(sys.argv)
#
# window = QPushButton("Push me")
# window.show()
#
# app.exec()