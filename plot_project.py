'''
The project requires 2 charts, and to use at least two different data sets. I will mark each part below to increase readability.

Three datasets used: China GDP, India GDP, India politician occupation categories

'''
#importing libraries
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd
import math
import csv

#load in the china dataset
c_path="/Users/rohanmathew/Documents/GitHub/Data-project/chinagdp.json"
c_d_a=[]
with open(c_path, 'r', encoding='utf-8') as c_file:
    c_data = json.load(c_file)
c_gdp = {c_entry["date"]: c_entry["value"] for c_entry in c_data[1]}

#Generated library for China GDP values
c_sort = dict(sorted(c_gdp.items()))
c_lngdp = {year: math.log(value) for year, value in c_sort.items()}

#Sorted and transformed into log GDP

#India GDP should have the exact same structure so will rewrite China data code
i_path="/Users/rohanmathew/Documents/GitHub/Data-project/indiagdp.json"
i_d_a=[]
with open(i_path, 'r', encoding='utf-8') as i_file:
    i_data = json.load(i_file)
i_gdp = {i_entry["date"]: i_entry["value"] for i_entry in i_data[1]}

#Generated India GDP library

i_sort = dict(sorted(i_gdp.items()))
i_lngdp = {year: math.log(value) for year, value in i_sort.items()}
#Sorted and transformed into log GDP


#China graph listings
yearxc = list(c_lngdp.keys())
gdpyc= list(c_lngdp.values())

#India graph listings
yearxi = list(i_lngdp.keys())
gdpyi= list(i_lngdp.values())

GDP_image = "/Users/rohanmathew/Documents/GitHub/Data-project/GDPgraph.png"
#Generated image


plt.figure(figsize=(10, 6))
plt.plot(yearxc, gdpyc, marker='o', linestyle='-', color='r', label='China')
plt.plot(yearxi, gdpyi, marker='o', linestyle='-', color='b', label='India')
#Only showing years in intervals of 8

plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True, nbins=10))

# Add labels and title
plt.xlabel('Year', fontsize=12)
plt.ylabel('log GDP', fontsize=12)
plt.title('India and China log GDP Over Time', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

#Save image
plt.savefig(GDP_image)
plt.close()


"""
Onto the next graph!

Using a CSV file

"""

occupations = {
    'Agriculture': 0,
    'Business': 0,
    'Education': 0,
    'Law': 0,
    'Medical': 0,
    'Other': 0,
    'Politics': 0,
    'Public Service': 0
}
### List of occupations I will be considering
oc_n=0
with open('/Users/rohanmathew/Documents/GitHub/Data-project/lok sabha python.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[11] in occupations:
            occupations[row[11]] += 1
            oc_n+= 1

        elif row[11]=="Civil Servant" or row[11]=="Social worker":
            occupations['Public Service'] +=1
            oc_n+= 1

        else:
            oc_n+= 1
            occupations['Other'] +=1



# Data for the pie chart
labels = occupations.keys()
sizes = occupations.values()

# Plotting the pie chart
plt.figure(figsize=(9,9))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Lok Sabha Occupation Distribution')
plt.axis('equal')

occupation_img = "/Users/rohanmathew/Documents/GitHub/Data-project/occupation_img.png"
plt.savefig(occupation_img)
plt.close()




