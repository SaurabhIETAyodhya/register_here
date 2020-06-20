from tkinter import *
import os

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def logout():
    screen7.destroy()

def saved():
    screen10 = Toplevel(screen)
    screen10.title("saved")
    screen10.geometry("100x100")
    Label(screen10, text="Saved").pack()


def save():
    filename = raw_filename.get()
    notes = raw_notes.get()

    data = open(filename, "w")
    data.write(notes)
    data.close()

    saved()

def create_notes():
    global raw_filename
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()

    screen9 = Toplevel(screen)
    screen9.title("info")
    screen9.geometry("300x250")
    Label(screen9, text = "please Enter a filename for the note below : ").pack()
    Entry(screen9, textvariable = raw_filename).pack()
    Label(screen9, text="please Enter a notes for the note below : ").pack()
    Entry(screen9, textvariable=raw_notes).pack()
    Button(screen9, text = "save", command = save).pack()

def view_notes1():
    filename1 = raw_filename1.get()
    data = open(filename1, "r")
    data1 =data.read()
    screen12 = Toplevel(screen)
    screen12.title("Notes")
    screen12.geometry("400x400")
    Label(screen12, text= data1).pack()
    data.close()


def view_notes():
    screen11 = Toplevel(screen)
    screen11.title("info")
    screen11.geometry("250x250")
    all_files = os.listdir()
    Label(screen11, text = "please use one of the filename below").pack()
    Label(screen11, text = all_files).pack()
    global raw_filename1
    raw_filename1  = StringVar()
    Entry(screen11, textvariable = raw_filename1).pack()
    Button(screen11, text = "Ok", command = view_notes1).pack()

def delete_notes1():
    filename3 = raw_filename2.get()
    screen14 = Toplevel(screen)
    screen14.title("Notes")
    screen14.geometry("400x400")
    Label(screen14, text= filename3+" removed ").pack()

def delete_note():
    screen13 = Toplevel(screen)
    screen13.title("info")
    screen13.geometry("250x250")
    all_files = os.listdir()
    Label(screen13, text="please use one of the filename below").pack()
    Label(screen13, text=all_files).pack()
    global raw_filename2
    raw_filename2 = StringVar()
    Entry(screen13, textvariable=raw_filename2).pack()
    Button(screen13, text="Ok", command=delete_notes1).pack()




def session():
    screen8 = Toplevel(screen)
    screen8.title("dashboard")
    screen8.geometry("400x400")
    Label(screen8, text = "Welcome to the dashboard").pack()
    Button(screen8, text = "Create Note", command = create_notes).pack()
    Button(screen8, text = "View Note", command = view_notes).pack()
    Button(screen8, text = "Delete Note", command = delete_note).pack()



def login_sucess():
    session()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="Ok", command=delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found !").pack()
    Button(screen5, text="Ok", command=delete4).pack()


def register_user():

    username_info = username.get()
    password_info = password.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration successful", fg  = "green", font = ("calibri", 11)).pack()

def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry


    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please Enter detalils below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text="password *").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please Enter detalils below to Login").pack()
    Label(screen2, text="").pack()
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="username *").pack()
    username_entry1 = Entry(screen2, textvariable =username_verify)
    username_entry1.pack()
    Label(screen2, text=" ").pack()
    Label(screen2, text="password *").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text=" ").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()

def main_screen():
    global  screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg = "grey",width = "100", height = "2",font = ("calibri" ,13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text="").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()

    screen.mainloop()

main_screen()
