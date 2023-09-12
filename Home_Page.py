import os.path
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Scrapping_Main


def home():
    # Login_1_1.t = 0
    w = Tk()
    w.geometry('350x500')
    w.title('HOME PAGE')
    w.resizable(0, 0)

    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222+r)
        Frame(w, width=10, height=500, bg="#"+c).place(x=j, y=0)
        j = j+10
        r = r+1

    Frame(w, width=250, height=400, bg='white').place(x=50, y=50)

    # lineframe on entry

    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=250)
    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=315)

    imagea = Image.open("Scrapper.png")
    resized_image = imagea.resize((180, 120), Image.Resampling.LANCZOS)
    imageb = ImageTk.PhotoImage(resized_image)
    #imageb = ImageTk.PhotoImage(imagea)

    label1 = Label(image=imageb,
                   border=0,

                   justify=CENTER)

    label1.place(x=90, y=55)

    # Command

    def cmd():
        if (os.path.exists('Conutries_Population_Sheet.csv') == True):
            w.destroy()
            import Filteration_Main
            Filteration_Main.filter()
        else:
            messagebox.showwarning(
                "WARNING!", "PLEASE PERFORM SCRAPPING FIRST!")

    # Web Scrapping Button_with hover effect

    def Web_Scrapping_Button(x, y, text, ecolor, lcolor):
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
                           command=Scrapping_Main.initial_srapper)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    # Filter Button_with hover effect

    def Filter_Button(x, y, text, ecolor, lcolor):
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

    # Button_with hover effect

    def log_out_bttn(x, y, text, ecolor, lcolor):
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
                        #    command=lambda: [w.destroy(), Login_1_1.login_main()])
                           command=lambda: [w.destroy()])

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    Web_Scrapping_Button(100, 200, 'Begin Web Scrapping', 'white', '#994422')
    Filter_Button(100, 265, 'Skip To Filteration Process', 'white', '#994422')
    log_out_bttn(100, 330, 'Exit', 'white', '#994422')

    w.mainloop()
