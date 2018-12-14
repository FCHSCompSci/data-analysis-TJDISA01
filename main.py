import matplotlib.pyplot as plt
import csv
# import requests
# from bs4 import BeautifulSoup

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://commons.wikimedia.org/wiki/File:Element-haeufigkeit.svg

with open("data.txt") as data_file:
    data_reader = csv.reader(data_file, delimiter=',')
    line_count = 0
    for row in data_reader:
        if line_count == 0:
            print(f"Column names are:\n{', '.join(row)}")
            line_count += 1
        else:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")
            line_count += 1
    print(f'Processed {line_count} lines.')