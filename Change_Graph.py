import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


def change():

    def autolabel(rectangle_group):
        for rect in rectangle_group:
            height = rect.get_height()

            plt.annotate(str(height),
                         xy=(rect.get_x() + rect.get_width() / 2, height),
                         ha='center',
                         xytext=(0, 3), textcoords='offset points',
                         color='black')

    def autolabel2(rectangle_group):
        for rect in rectangle_group:
            height = rect.get_height()

            plt.annotate(str(height)+"%",
                         xy=(rect.get_x() + rect.get_width() / 2, height),
                         ha='center',
                         xytext=(0, 3), textcoords='offset points',
                         color='black')

    datafile = pd.read_csv("Modified_pop.csv")
    plt.figure(figsize=(11, 6), dpi=100)
    plt.subplot(1, 2, 1)
    rect = plt.bar(datafile["Name"], datafile["Net Change"], ec="Black")
    autolabel(rect)
    plt.xlabel("Countries")
    plt.ylabel("Change (10e7)")
    plt.title("Net Change 2019-2020")
    labels = plt.gca().get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')

    plt.subplot(1, 2, 2)
    rect = plt.bar(datafile["Name"], datafile["Yearly Change (%)"], ec="Black")
    autolabel2(rect)
    plt.xlabel("Countries")
    plt.ylabel("Change (%)")
    plt.title(" Yearly Change 2019-2020 (%)")
    labels = plt.gca().get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')

    plt.show()
