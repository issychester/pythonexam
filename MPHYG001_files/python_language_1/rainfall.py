import csv
import json
from matplotlib import pyplot as plt
import statistics
from math import sqrt

year = []
date = []
rainfall = [] 

years = {}

with open('python_language_1_data.csv', 'r') as f:
    reader = csv.reader(f)
    #for row in reader:
        #data.append(int(row))
        #with csv.DictReader(f)
        #year.append(int(row['year']))
        #date.append(int(row['day of year']))
        #rainfall.append(float(row['rainfall (mm/day)']))
        
    for n, row in enumerate(reader):
        if not n:
            continue
        year, date, rainfall = row
        if year not in years:
            years[year] = list()
        #years[year].append((date, rainfall))
        years[year].append(float(rainfall))

#print(years)

with open('dictionary.json', 'w') as f:
    json.dump(years, f)
    
def graph(file, year, line = 'b'):
    #file name, year and colour specifier needed as string
    with open(file, 'r') as f:
        data = json.load(f)
    yearData = data.get(year)
    plt.plot(yearData, line)
    plt.title('Rainfall Data for '+ year)
    plt.xlabel('Date')
    plt.ylabel('rainfall, mm/day')
    plt.savefig('graph.png')
    return


#graph('dictionary.json', '1998', 'g')

average = []
def mean(file, year1, year2):
    #file name needed as string and year as integers
    with open(file, 'r') as f:
        data = json.load(f)
    for year in range(year1, year2):
        yearData = data.get(str(year))
        averageYearData = statistics.mean(yearData)
        average.append(averageYearData)
    plt.plot(range(year1, year2+1), average)
    plt.title('Avergae Rainfall Data between '+ str(year1) + ' and '+ str(year2))
    plt.xlabel('Year')
    plt.ylabel('Average Rainfall, mm/day')
    plt.savefig('averageGraph.png')
    return

mean('dictionary.json', 1988, 2000)

def correction(rainfall_value):
    correctedValue = rainfall_value * 1.2 ** sqrt(2.0)
    return correctedValue

def function1(year):
    newYear = []
    for value in year:
        correctedValue = correction(value)
        newYear.append(correctedValue)
    return newYear

def function2(year):
    #Advatnage is it takes less time to compute but is harder to check if answer isn't what is expected 
    newYear = [correction(value) for value in year]
    return newYear

fun1 = function1(years['2012'])
fun2 = function2(years['2012'])

print(fun1 == fun2)
