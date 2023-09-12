from tkinter import *
from tkinter import messagebox
import mysql.connector

def login():

    # Login Page
    root = Tk()
    frame1 = LabelFrame(root, text="Login")
    frame1.pack()

    # Root Details
    root.title("Welcome to our Login Page")
    root.iconbitmap("43_iPv_icon.ico")

    # Data Base SQL Initialization
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="20202krish",
        database="users",
        auth_plugin="mysql_native_password"
    )
    cursor = mydb.cursor()

    # New User Initialization
    def new_user_process():
        new_top_page = Toplevel()
        new_top_page.title("New Users Page")
        new_top_page.iconbitmap("43_iPv_icon.ico")
        loginframe = LabelFrame(new_top_page, text="New Login")
        loginframe.pack()
        name_label = Label(loginframe, text="Enter User Name : ")
        name_input = Entry(loginframe)
        name_label.grid(row=0, column=0)
        name_input.grid(row=0, column=1)
        password_label = Label(loginframe, text="Enter Password : ")
        password_input = Entry(loginframe)
        password_label.grid(row=1, column=0)
        password_input.grid(row=1, column=1)

        def new_user_entery():
            sql = "INSERT INTO users (name, password) VALUES (%s, %s)"
            val = (name_input.get(), password_input.get())
            cursor.execute(sql, val)
            mydb.commit()

        confirm_button = Button(
            loginframe, text="Click to Confirm and access the program ", command=lambda: [new_user_entery(), new_top_page.destroy()])
        confirm_button.grid(row=2, column=0)
        exit_button_new = Button(
            new_top_page, text="Exit the Program!", command=exit_pro)
        exit_button_new.pack()

    # Existing Users Login

    def existing_user_process():
        new_top_page = Toplevel()
        new_top_page.title("Existing Users Page")
        new_top_page.iconbitmap("43_iPv_icon.ico")
        loginframe = LabelFrame(
            new_top_page, text="Please Enter Correct Details")
        loginframe.pack()
        name_label = Label(loginframe, text="Enter User Name : ")
        name_input = Entry(loginframe)
        name_label.grid(row=0, column=0)
        name_input.grid(row=0, column=1)
        password_label = Label(loginframe, text="Enter Password : ")
        password_input = Entry(loginframe)
        password_label.grid(row=1, column=0)
        password_input.grid(row=1, column=1)

        def existing_user_entery():
            userid = name_input.get()
            password = password_input.get()
            sql = "SELECT * FROM users WHERE name ='" + userid + "'"
            cursor.execute(sql)
            myresult = cursor.fetchall()
            if len(myresult) == 0:
                messagebox.showinfo(
                    "Alert 1", "Entered Credentials are Invalid")
                error_label = Label(
                    loginframe, text="Do you want to create a new Account Instead ?")
                error_button = Button(loginframe, text="Click here for New Account Creation", command=lambda: [
                    new_user_process(), new_top_page.destroy()])
                error_label.grid(row=2, column=0)
                error_button.grid(row=2, column=1)
            else:
                sql = "SELECT * FROM users WHERE name ='" + \
                    userid + "' AND password = '" + password + "'"
                cursor.execute(sql)
                myresult = cursor.fetchall()
                if (len(myresult) == 0):
                    messagebox.showinfo(
                        "Alert 2", "Entered Credentials are Invalid")
                    error_label = Label(
                        loginframe, text="Do you want to create a new Account Instead ?")
                    error_button = Button(loginframe, text="Click here for New Account Creation", command=lambda: [
                        new_user_process(), new_top_page.destroy()])
                    error_label.grid(row=2, column=0)
                    error_button.grid(row=2, column=1)
                elif (len(myresult) == 1):
                    print(myresult[0][1])
                    messagebox.showinfo(
                        "Confirmation", "Welcome to the Software")

        confirm_button = Button(
            loginframe, text="Click to Confirm and access the program ", command=existing_user_entery)
        confirm_button.grid(row=3, column=0)
        exit_button_new = Button(
            new_top_page, text="Exit the Program!", command=exit_pro)
        exit_button_new.pack()

    # Login Process 1
    existing_user_button = Button(




        frame1, text="Login Now", command=existing_user_process)
    new_user_button = Button(
        frame1, text="New User Account", command=new_user_process)
    temp_user_button = Button(frame1, text="Temperorary User Access")
    existing_user_button.pack()
    new_user_button.pack()
    temp_user_button.pack()

    # Exit Button Commands

    def exit_pro():
        response = messagebox.askokcancel(
            "Warning Prompt", "Do you really want to Quit ?")
        if response == 1:
            root.quit()
        else:
            return

    # Root End
    exit_button = Button(root, text="Exit the Program!", command=exit_pro)
    exit_button.pack()
    root.mainloop()


login()
