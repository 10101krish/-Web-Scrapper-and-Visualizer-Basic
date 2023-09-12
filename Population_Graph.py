import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


def population():

    def autolabel(rectangle_group):
        for rect in rectangle_group:
            height = rect.get_height()

            plt.annotate(str(height),
                         xy=(rect.get_x() + rect.get_width() / 2, height),
                         ha='center',
                         xytext=(0, 3), textcoords='offset points',
                         color='black')

    datafile = pd.read_csv("Modified_pop.csv")
    plt.figure(figsize=(11, 6), dpi=100)
    plt.subplot(1, 2, 1)
    labels = datafile["Name"]
    popl = datafile["Population (2020)"]
    rect = plt.bar(labels, popl, ec="Black", label=labels)
    autolabel(rect)
    plt.xlabel("Countries")
    plt.ylabel("Population (10e9)")
    plt.title("Population as of 2020")
    labels = plt.gca().get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')

    pie = plt.subplot(1, 2, 2)
    labels = datafile['Name']
    sizes = datafile['World Share (%)']
    wedges = plt.pie(sizes, autopct="%.2f %%", shadow=False, labels=labels,
                     wedgeprops={'linewidth': 1, 'edgecolor': 'black'}, 
                     textprops={'size': 15, "color": "black"}, labeldistance=1.1, rotatelabels=True)
    plt.title("World Share (%) Across given Countries")
    #plt.legend(labels, title="Countries", loc="lower center")

    plt.show()

