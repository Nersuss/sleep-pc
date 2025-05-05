import os
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage


def shutdown_pc(minutes):
    os.system("shutdown /s /t " + str(60 * minutes))
    success_msg.pack()
    cancel_msg.pack_forget()

def shutdown_cancel():
    os.system("shutdown /a")
    cancel_msg.pack()
    success_msg.pack_forget()

def show_black_screen():
    # root.attributes("-fullscreen", True)
    # root.geometry(str(root.winfo_screenheight()) + "x" + str(root.winfo_screenwidth()))
    root.configure(background="black")

root = Tk()

root.eval('tk::PlaceWindow . center')
root.title("Выключатель компа")
root.geometry("300x400")
root.configure(background="#003d6e")
root.iconphoto(True, PhotoImage(file="favicon-32x32.png"))

label_welcome = Label(text="Таймер выключения", font=("Arial Bold", 14), fg="white", bg="#003d6e")
label_welcome.pack()

btn_cancel = Button(text="Отменить выключение", command=shutdown_cancel, fg="white", bg="#003d6e")
btn_cancel.pack()

label_time = Label(text="Введите время в минутах", font=("Arial", 12), fg="white", bg="#003d6e")
label_time.pack()

input_time = ttk.Combobox(values=["1", "15", "30", "45", "60", "75", "90"], width=10, foreground="#003d6e", background="green")
input_time.set("45")
input_time.pack()

success_msg = Label(text="Выключение запланировано", font=("Arial", 12), fg="lightgreen", bg="#003d6e")
cancel_msg = Label(text="Выключение отменено", font=("Arial", 12), fg="red", bg="#003d6e")

btn_plan_shutdown = Button(text="Запланировать выключение", fg="white", bg="#003d6e")
btn_plan_shutdown.bind("<Button-1>", lambda event: shutdown_pc(int(input_time.get())))
btn_plan_shutdown.pack()

btn_show_black_screen = Button(text="Черный экран", command=show_black_screen, fg="white", bg="#003d6e")
btn_show_black_screen.pack()

root.mainloop()

# pyinstaller --onedir main.py --noconsole --icon favicon.ico
