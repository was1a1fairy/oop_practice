from tkinter import *
from tkinter import messagebox
import customtkinter as ctk


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
button_submit.grid(column = 1)

frame_center.pack()


root.mainloop()




# task2


def reaction_on_click():

    array1 = entry1.get()
    array2 = entry2.get()

    entry1.delete(0, END)
    entry2.delete(0, END)

    if len(array1) != len(array2):
        messagebox.showerror("error!", "input arrays the same length, pls((")
        return

    if len(array1) == 0 or len(array2) == 0:
        messagebox.showerror("error!", "array's length must be > 0")
        return

    if "[" in array1:
        array1 = array1[1::]
    if "[" in array2:
        array2 = array2[1::]
    if "]" in array1:
        array1 = array1[:len(array1)-1:]
    if "]" in array2:
        array2 = array2[:len(array1)-1:]

    if "," in array1:
        array1 = array1.split(",")
    else:
        array1 = array1.split()

    if "," in array2:
        array2 = array2.split(",")
    else:
        array2 = array2.split()

    if not isinstance(array1, list):
        messagebox.showerror("error!", "1st array not list!")
        return
    if not isinstance(array2, list):
        messagebox.showerror("error!", "2nd array not list!")
        return

    result = []
    for i in range(len(array1)):

        if array1[i].isdigit():
            array1[i] = int(array1[i])
        if array2[i].isdigit():
            array2[i] = int(array2[i])

        if not isinstance(array1[i], int|float) or not isinstance(array2[i], int|float):
            messagebox.showerror("error!", "input arrays of numbers((")
            return
        result.append(array2[i]*array1[i])

    label4.configure(text= f"{result}")
    messagebox.showinfo("done!", "arrays were successfully multiplied")


window = ctk.CTk()
window.geometry("800x400")
window.resizable(False, False)
window.title('task2')

main = ctk.CTkFrame(window, fg_color='transparent')
frame1 = ctk.CTkFrame(main, fg_color='transparent')

label1 = ctk.CTkLabel(frame1, text= '1st array:', font= ("Arial", 16))
entry1 = ctk.CTkEntry(frame1)
label1.grid(row= 0, column= 0, pady= 20, padx= 70)
entry1.grid(row= 0, column= 2, pady= 20, padx= 70)
label2 = ctk.CTkLabel(frame1, text= '2nd array:', font= ("Arial", 16))
entry2 = ctk.CTkEntry(frame1)
label2.grid(row= 1, column= 0, pady= 20, padx= 70)
entry2.grid(row= 1, column= 2, pady= 20, padx= 70)

frame1.pack(side= ctk.TOP, fill= ctk.X)

button = ctk.CTkButton(main, 200, 30, text= "calculate", command= reaction_on_click, font= ("Arial", 20))
button.pack(pady=40, padx= 70, fill= X)

frame2 = ctk.CTkFrame(main, fg_color='transparent')

label3 = ctk.CTkLabel(frame2, text= "result:", font= ("Arial", 16))
label4 = ctk.CTkLabel(frame2, text= "soon", font= ("Arial", 16))
label3.pack(side= LEFT, padx= 70, pady= 25)
label4.pack(side= RIGHT, padx= 70, pady= 25)

frame2.pack(side= ctk.BOTTOM, fill= ctk.X)

main.pack(expand= True)
window.mainloop()