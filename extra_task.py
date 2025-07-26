from tkinter import *
from tkinter import messagebox


def print_entry():
    name = entry1.get()
    email = entry2.get()
    phone = entry3.get()
    login = entry4.get()
    password = entry5.get()

    if name == "":
        messagebox.showerror("Field is Empty!(", "Full name is empty(( try again")
        return
    if email == "":
        messagebox.showerror("Field is Empty!(", "E-mail is empty(( try again")
        return
    if phone == "":
        messagebox.showerror("Field is Empty!(", "Phone is empty(( try again")
        return
    if login == "":
        messagebox.showerror("Field is Empty!(", "Login is empty(( try again")
        return
    if password == "":
        messagebox.showerror("Field is Empty!(", "Password is empty(( try again")
        return

    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

    print(f"Full name: {name}."
          f" E-mail: {email},"
          f" Phone: {phone},"
          f" Login: {login},"
          f" Password: {password}")

    messagebox.showinfo("мяу", "данные отправлены!ура")


root = Tk()
root.geometry("800x400")
root.title("Task1")
root.resizable(False, False)


label1 = Label(root, text = "Full name")
entry1 = Entry(root, width=41)

label1.pack()
entry1.pack()


frame_center = Frame(root)

label2 = Label(frame_center, text = "E-mail")
entry2 = Entry(frame_center)

label2.grid(row = 1, column = 1)
entry2.grid(row = 2, column = 1)

label3 = Label(frame_center, text = "Phone")
entry3 = Entry(frame_center)

label3.grid(row = 1, column = 2)
entry3.grid(row = 2, column = 2)

label4 = Label(frame_center, text = "Login")
entry4 = Entry(frame_center)

label4.grid(row = 3, column = 1)
entry4.grid(row = 4, column = 1)

label5 = Label(frame_center, text = "Password")
entry5 = Entry(frame_center)

label5.grid(row = 3, column = 2)
entry5.grid(row = 4, column = 2)

button_submit = Button(frame_center, text = "Submit", command=print_entry, bg="#FFA500", width = 17)
button_submit.grid(row = 5, column = 1)

frame_center.pack()


root.mainloop()