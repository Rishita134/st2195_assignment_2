#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:34:13 2022

@author: apple
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/Comma-separated_values"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

table = soup.find("table", class_="wikitable")
table

headers = []

for i in table.find_all("th"):
    title = i.text.strip()
    headers.append(title)
    
wiki_table = pd.DataFrame(columns = headers)

for row in table.find_all("tr")[1:]:
    data = row.find_all("td")
    row_data = [td.text.strip() for td in data]
    wiki_table.loc[len(wiki_table)] = row_data
    
print(wiki_table)

wiki_table.to_csv("wiki_table.csv", index = False)
