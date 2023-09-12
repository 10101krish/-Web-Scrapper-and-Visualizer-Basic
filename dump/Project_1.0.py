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
frame1.pack()


# Exit Button Commands
def exit_pro():
    response = messagebox.askokcancel("Warning Prompt", "Do you really want to Quit ?")
    if response == 1:
        root.quit()
    else:
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
    return


# Start and exit Buttons
start_button = Button(frame1, text="Click Me to Initiate the Project !", command=initial_srapper)
start_button.grid()
exit_button = Button(root, text="Exit the Program!", command=exit_pro)
exit_button.pack()

# Page ending
root.mainloop()
