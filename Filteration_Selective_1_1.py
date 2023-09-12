from tkinter import *
from tkinter import messagebox
import pandas as pd
import numpy as np
from PIL import ImageTk, Image
import Filteration_Selective_2_1
import Filteration_Main


def selective():
    w = Tk()
    w.geometry('600x500')
    w.title('FILTERATION PROCESS')
    w.resizable(0, 0)

    # Importing Data File
    datafile = pd.read_csv('Conutries_Population_Sheet.csv')

    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222+r)

        Frame(w, width=10, height=500, bg="#"+c).place(x=j, y=0)
        j = j+10
        r = r+1

    Frame(w, width=500, height=400, bg='white').place(x=50, y=50)

    # l1 label for Selective Number
    l1 = Label(
        w, text='Number of Countries for Filteration', bg='white')
    l = ('Consolas', 13)
    l1.config(font=l)
    l1.place(x=80, y=200)

    # e1 label for Selective Number entry
    e1 = Entry(w, width=3, border=0)
    l = ('Consolas', 13)
    e1.config(font=l)
    e1.place(x=470, y=200)

    # lineframe on entry

    Frame(w, width=50, height=2, bg='#141414').place(x=450, y=222)
    Frame(w, width=300, height=2, bg='#994422').place(x=80, y=252)

    imagea = Image.open("Scrapper.png")
    resized_image = imagea.resize((180, 120), Image.ANTIALIAS)
    imageb = ImageTk.PhotoImage(resized_image)
    #imageb = ImageTk.PhotoImage(imagea)

    label1 = Label(image=imageb,
                   border=0,

                   justify=CENTER)

    label1.place(x=90, y=55)

    # Command

    def cmd():
        if (len(e1.get()) == 0):
            messagebox.showwarning(
                "FILTERATION PROCESS", "PLEASE ENTER A VALUE FOR THE PROCESS TO START!")
        else:
            n = int(e1.get())
            if n <= 0:
                messagebox.showwarning(
                    "FILTERATION PROCESS", "PLEASE ENTER A VALUE GREATER THAN ZERO!")
            elif n > 235:
                messagebox.showwarning(
                    "FILTERATION PROCESS", "PLEASE ENTER A VALUE LESS THAN 236!")
            else:
                w.destroy()
                Filteration_Selective_2_1.selective_part_2(n)

                # Button_with hover effect

    def confirmbttn(x, y, text, ecolor, lcolor):
        def on_entera(e):
            myButton1['background'] = ecolor  # ffcc66
            myButton1['foreground'] = lcolor  # 000d33

        def on_leavea(e):
            myButton1['background'] = lcolor
            myButton1['foreground'] = ecolor

        myButton1 = Button(w, text=text,
                           width=20,
                           height=2,
                           fg=ecolor,
                           border=0,
                           bg=lcolor,
                           activeforeground=lcolor,
                           activebackground=ecolor,
                           command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    def quitbttn(x, y, text, ecolor, lcolor):
        def on_entera(e):
            myButton1['background'] = ecolor  # ffcc66
            myButton1['foreground'] = lcolor  # 000d33

        def on_leavea(e):
            myButton1['background'] = lcolor
            myButton1['foreground'] = ecolor

        myButton1 = Button(w, text=text,
                           width=20,
                           height=2,
                           fg=ecolor,
                           border=0,
                           bg=lcolor,
                           activeforeground=lcolor,
                           activebackground=ecolor,
                           command=lambda: [w.destroy(), Filteration_Main.filter()])

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    confirmbttn(100, 295, 'Confirm and Proceed', 'white', '#994422')
    quitbttn(300, 295, 'Return to Choices', 'white', '#994422')

    w.mainloop()
