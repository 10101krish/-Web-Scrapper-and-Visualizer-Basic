from tkinter import *
from tkinter import messagebox
import pandas as pd
import numpy as np
from PIL import ImageTk, Image
import Filteration_Main
import Filteration_Selective_1_1


def selective_part_2(n):
    w = Tk()
    values1 = "600x"+str(180+(n*80))
    w.geometry(values1)
    w.title('FILTERATION PROCESS')
    w.resizable(0, 0)

    # Importing Data File
    datafile = pd.read_csv('Conutries_Population_Sheet.csv')

    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222+r)

        Frame(w, width=10, height=(180+(n*80)), bg="#"+c).place(x=j, y=0)
        j = j+10
        r = r+1

    Frame(w, width=500, height=(80+(n*80)), bg='white').place(x=50, y=50)

    # Labels and Entry Fields for countries
    l = ('Consolas', 13)
    lbl = []
    e = []
    dash = []
    for i in range(n):
        # l for label
        text = "Country " + str(i+1)
        lbl.append(Label(
            w, text=text, bg='white'))
        lbl[i].config(font=l)
        lbl[i].place(x=80, y=(60+(80*i)))
        # e for entry
        e.append(Entry(w, width=30, border=0))
        e[i].config(font=l)
        e[i].place(x=80, y=(90+(80*i)))
        # break dash
        dash.append(Frame(w, width=180, height=2,
                    bg='#141414').place(x=80, y=(112+(80*i))))

    # Command
    def cmd():
        clen = len(datafile.columns)
        rlen = len(datafile['Name'])
        xyz = []
        counter = 0
        for i in range(n):
            cont = e[i].get()
            y = (datafile.loc[datafile['Name'] == cont])
            if y.empty == False:
                xyz.append(y)
                counter = counter+1
        df = pd.concat(xyz)
        df.to_csv("Modified_pop.csv", index=False)
        messagebox.showinfo("FILTERATION PROCESS", str(counter) +
                            " Countries Processed out of "+str(n)+" entered !")
        w.destroy()
        Filteration_Main.filter()

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
                           command=lambda: [w.destroy(), Filteration_Selective_1_1.selective()])

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    confirmbttn(100, (65+(90+(80*(n-1)))),
                'Confirm and Filter', 'white', '#994422')
    quitbttn(300, (65+(90+(80*(n-1)))),
             'Return to Choices', 'white', '#994422')

    w.mainloop()
