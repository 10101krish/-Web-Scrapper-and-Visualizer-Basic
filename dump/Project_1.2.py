# Libraries Importing
import requests
import pandas as pd
import numpy as np
import matplotlib as plt
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

# Initial Page
root = Tk()
frame1 = LabelFrame(root, text="Starting Inputs")
frame2 = LabelFrame(root, text="Countries Selection and Filtration")
frame3 = LabelFrame(root)
frame1.pack()
frame2.pack()
frame3.pack()

# Root Details
root.title("Scrapping Project for Software Engineering")
root.iconbitmap("43_iPv_icon.ico")


# Exit Button Commands
def exit_pro():
    response = messagebox.askokcancel("Warning Prompt", "Do you really want to Quit ?")
    if response == 1:
        root.quit()
    else:
        return


# Selection from Top
def fromtp():
    clen = len(datafile.columns)
    label = Label(frame3, text="Enter how many countries you want to Select from top : ")
    label.grid(row=0, column=0)
    e = Entry(frame3)
    e.grid(row=0, column=1)
    global n

    def clicked():
        n = int(e.get())
        popdict = {}
        for i in range(clen):
            c = datafile.columns[i]
            x = datafile[c][0:n]
            popdict[c] = x
        df = pd.DataFrame(popdict)
        df.to_csv("Modified_pop.csv", index=False)
        return

    button = Button(frame3, text="Confirm", command=clicked).grid(row=0, column=2)

    return


# Selection from Bottom
def frombtm():
    clen = len(datafile.columns)
    rlen = len(datafile['Name'])
    label = Label(frame3, text="Enter how many countries you want to Select from top : ")
    label.grid(row=0, column=0)
    e = Entry(frame3)
    e.grid(row=0, column=1)

    def clicked():
        n = int(e.get())
        popdict = {}
        for i in range(clen):
            c = datafile.columns[i]
            x = datafile[c].iloc[(rlen - n - 1):]
            popdict[c] = x
        df = pd.DataFrame(popdict)
        df.to_csv("Modified_pop.csv", index=False)
        return

    button = Button(frame3, text="Confirm", command=clicked).grid(row=0, column=2)
    return


# Custom Selection :
def selective():
    clen = len(datafile.columns)
    rlen = len(datafile['Name'])
    global xyz
    xyz = []
    label = Label(frame3, text="How Many countries do you Want to Compare : ")
    label.grid(row=0, column=0)
    e = Entry(frame3)
    e.grid(row=0, column=1)
    global x

    def clicked():
        x = int(e.get())
        for i in range(x):
            labelo = Label(frame3, text="Provide Country Name (First Letter to be Capital) : ")
            labelo.grid(row=i + 1, column=0)
            ef = Entry(frame3)
            ef.grid(row=i + 1, column=1)

            def clickedo():
                cont = ef.get()
                y = (datafile.loc[datafile['Name'] == cont])
                if y.empty == False:
                    print(y)
                    df = pd.concat(xyz.append(y))
                    df.to_csv("Modified_pop.csv", index=False)
                else:
                    print("Wrong Country Input, Entry Rejected !")
                return

            buttono = Button(frame3, text="Confirm", command=clickedo).grid(row=i + 1, column=2)


        return

    button = Button(frame3, text="Confirm", command=clicked).grid(row=0, column=2)
    return


# Radio Button Submission
def clicking(value):
    if value == 1:
        fromtp()

    elif value == 2:
        frombtm()

    elif value == 3:
        selective()

    else:
        Label(frame2, text="Please enter valid choice").grid(row=4, column=1)


def data_filteration_start():
    # Radio Buttons
    r = IntVar()
    r.set("0")
    Radiobutton(frame2, text="Choose Countries From Top ", variable=r, value=1).grid(row=0, column=0)
    Radiobutton(frame2, text="Choose Countries From Bottom ", variable=r, value=2).grid(row=1, column=0)
    Radiobutton(frame2, text="Custom Selection of Countries ", variable=r, value=3).grid(row=2, column=0)
    button = Button(frame2, text="Finalize selection", command=lambda: clicking(r.get()))
    button.grid(row=3, column=0, columnspan=2)
    label = Label(frame2, text="Selection Status : ").grid(row=4, column=0)
    return


# Scrapping of Page
def initial_srapper():
    page_url = 'https://www.worldometers.info/world-population/population-by-country/'
    response = requests.get(page_url)
    page_data = BeautifulSoup(response.text, 'html.parser')

    # Scrapping of Data pt 1
    name_selection = 'font-weight: bold; font-size:15px; text-align:left'
    pop_selection = 'font-weight: bold;'
    scope = 'row'
    countries_data = page_data.find_all('tbody')
    country_data = countries_data[0].find_all('tr')

    # Scrapping of Data pt 2
    country_names = []
    country_population = []
    population_change = []
    net_change = []
    country_density = []
    land_area = []
    world_share = []
    for tag in country_data:
        country_bio = tag.find_all('td')
        country_names.append(country_bio[1].text)
        country_population.append(int((country_bio[2].text).replace(",", "")))
        population_change.append(float((country_bio[3].text).replace(" %", "")))
        net_change.append(int((country_bio[4].text).replace(",", "")))
        country_density.append((country_bio[5].text).replace(",", ""))
        land_area.append(int((country_bio[6].text).replace(",", "")))
        world_share.append(float((country_bio[11].text).replace(" %", "")))

    # dict and save cvs
    country_dict = {'Name': country_names, 'Population (2020)': country_population,
                    'Yearly Change (%)': population_change, 'Net Change': net_change,
                    'Country Density (P/Km2)': country_density, 'Land Area (Km2)': land_area,
                    'World Share (%)': world_share}
    country_df = pd.DataFrame(country_dict)
    country_df.to_csv('Conutries_Population_Sheet.csv', index_label="#", index=False)
    data_filteration_start()
    return


# Filtering Data
datafile = pd.read_csv('Conutries_Population_Sheet.csv')

# Start and exit Buttons
start_button = Button(frame1, text="Click Me to Initiate the Project !", command=initial_srapper)
start_button.grid()
exit_button = Button(root, text="Exit the Program!", command=exit_pro)
exit_button.pack()

# Page ending
root.mainloop()
