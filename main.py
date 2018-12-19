import matplotlib.pyplot as plt
import csv
# import requests
# from bs4 import BeautifulSoup

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://commons.wikimedia.org/wiki/File:Element-haeufigkeit.svg

name = []
abundance = []

def read_data():
    with open("data.csv") as data_file:
        data_reader = csv.reader(data_file, delimiter=',')
        line_count = 0
        for row in data_reader:
            if line_count == 0:
                print(f"Column names are:\n{', '.join(row)}")
                line_count += 1
            else:
                row_2 = eval(row[2].replace("e", "*10**"))
                print(f"\t{row[0]}\t\t\t{row[1]}\t\t\t{row_2}")
                name.append(row[0])
                abundance.append(row_2)
                line_count += 1
        print(f'Processed {line_count} lines.')
    graph()

def graph():
    plt.bar(name, abundance)
    plt.title("Abundance of Elements In Our Solar System", fontsize=20)
    plt.xlabel("Element", fontsize=18)
    plt.ylabel("Abundance", fontsize=18)
    plt.yscale("log")
    plt.grid(True)
    plt.margins(False)
    plt.tick_params(axis='x', labelsize=8)
    plt.show()

read_data()