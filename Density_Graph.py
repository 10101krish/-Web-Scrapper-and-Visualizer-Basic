import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


def density():

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
    rect = plt.bar(datafile["Name"],
                   datafile["Country Density (P/Km2)"], ec="Black")
    autolabel(rect)
    #plt.plot(datafile["Country Density (P/Km2)"], datafile["Name"], "r--o")
    plt.xlabel("Countries")
    plt.ylabel("Density")
    plt.title("Country Density (P/Km2)")
    labels = plt.gca().get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')

    plt.subplot(1, 2, 2)
    rect = plt.bar(datafile["Name"], datafile["Land Area (Km2)"], ec="Black")
    #plt.plot(datafile["Name"], datafile["Land Area (Km2)"], "r--o")
    autolabel(rect)
    plt.xlabel("Countries")
    plt.ylabel("Area (10e6)")
    plt.title("Land Area in Km2")
    labels = plt.gca().get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')

    plt.show()