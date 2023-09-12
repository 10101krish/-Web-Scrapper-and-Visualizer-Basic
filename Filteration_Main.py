import os.path
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Filteration_FromTp
import Filteration_FromBtm
import Filteration_Selective_1_1
import Visualization_Main


def filter():
    w = Tk()
    w.geometry('450x625')
    w.title('DATA FILTERATION')
    w.resizable(0, 0)

    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222+r)
        Frame(w, width=10, height=625, bg="#"+c).place(x=j, y=0)
        j = j+10
        r = r+1

    Frame(w, width=350, height=525, bg='white').place(x=50, y=50)

    # Radio Buttons for Choice Selection
    r = IntVar()
    r.set("0")

    # Radio Button 1
    l = ('Consolas', 13)
    r1 = Radiobutton(w, text="Choose Countries From Top ", variable=r,
                     value=1, activeforeground="red", bg='white')
    r1.config(font=l)
    r1.place(x=80, y=200)

    # Radio Button 2
    r2 = Radiobutton(w, text="Choose Countries From Bottom ", variable=r,
                     value=2, activeforeground="red", bg='white')
    r2.config(font=l)
    r2.place(x=80, y=260)

    # Radio Button 3
    r3 = Radiobutton(w, text="Custom Selection of Countries ",
                     variable=r, value=3, activeforeground="red", bg='white')
    r3.config(font=l)
    r3.place(x=80, y=320)

    # lineframe on entry

    Frame(w, width=280, height=2, bg='#141414').place(x=80, y=245)
    Frame(w, width=280, height=2, bg='#141414').place(x=80, y=305)

    imagea = Image.open("Scrapper.png")
    resized_image = imagea.resize((180, 120), Image.ANTIALIAS)
    imageb = ImageTk.PhotoImage(resized_image)
    #imageb = ImageTk.PhotoImage(imagea)

    label1 = Label(image=imageb,
                   border=0,

                   justify=CENTER)

    label1.place(x=145, y=57)

    # Necceccesary Precaution for Radio Buttons
    r1.deselect()
    r2.deselect()
    r3.deselect()

    # Command for Radio Buttons

    def clicking(value):
        if value == 1:
            w.destroy()
            Filteration_FromTp.fromtp()

        elif value == 2:
            w.destroy()
            Filteration_FromBtm.frombtm()

        elif value == 3:
            w.destroy()
            Filteration_Selective_1_1.selective()

    # Command for Visualization

    def visualize_cmd():
        if (os.path.exists("Modified_pop.csv") == True):
            w.destroy()
            Visualization_Main.visualize()
        else:
            messagebox.showwarning(
                "WARNING!", "PLEASE PERFORM BASIC FILTRATION FIRST!")

    # Filteration Button_with hover effect

    def Filteration_Selection(x, y, text, ecolor, lcolor):
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
                           command=lambda: clicking(r.get()))

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    # Visualisation Button_with hover effect

    def Viusalisation_Button(x, y, text, ecolor, lcolor):
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
                           command=visualize_cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    # Quit Button_with hover effect

    def Back_Button(x, y, text, ecolor, lcolor):
        def on_entera(e):
            myButton1['background'] = ecolor  # ffcc66
            myButton1['foreground'] = lcolor  # 000d33

        def on_leavea(e):
            myButton1['background'] = lcolor
            myButton1['foreground'] = ecolor

        import Home_Page
        myButton1 = Button(w, text=text,
                           width=20,
                           height=2,
                           fg=ecolor,
                           border=0,
                           bg=lcolor,
                           activeforeground=lcolor,
                           activebackground=ecolor,
                           command=lambda: [w.destroy(), Home_Page.home()])

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    Filteration_Selection(
        150, 375, 'Starting Filtering Process', 'white', '#994422')
    Viusalisation_Button(
        150, 440, 'Skip to Data Visualization', 'white', '#994422')
    Back_Button(
        150, 505, 'Back to Home Page', 'white', '#994422')

    w.mainloop()
