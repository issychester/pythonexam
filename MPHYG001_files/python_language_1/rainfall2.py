# -*- coding: utf-8 -*-8
"""
Created on Sun Apr 28 14:15:58 2019

@author: zcemich
"""
import csv
import json
import matplotlib.pyplot as plt
import statistics
from math import sqrt

def loaddata(file):
    years = {}
    with open(file) as f:
        reader = csv.reader(f)
        for n, row in enumerate(reader):
            if not n:
                continue
            year, day, rainfall = row
            if not year in years:
                years[year] = list()
            years[year].append(float(rainfall))
    return years   

def savedictionary(data):
    with open('dictionary2.json', 'w') as f:
        json.dump(data, f)
    return

def graph(file, year, colour = 'b'):
    #load file
    with open(file, 'r') as f:
        filedata = json.load(f)
    
    #selectyeardata
    yeardata = filedata[year]
    
    #plot year data
    plt.plot(range(0, len(yeardata)), yeardata, colour)
    plt.title('Daily rainfall for ' + year)
    plt.xlabel('Date')
    plt.ylabel('rainfall, mm/day')
    
    #save figure
    plt.savefig('take2daily.png')
    return 

def graph_mean(file, year1, year2):
    #load file
    with open(file, 'r') as f:
        filedata = json.load(f)
        
    #get years as integer
    year1 = int(year1)
    year2 = int(year2)

    inclusiveyears = list(range(year1, year2+1))
    
    mean = []
    for year in inclusiveyears:
        yearmean = statistics.mean(filedata[str(year)])
        mean.append(yearmean)
    
    #plot year data
    plt.clf()
    plt.plot(inclusiveyears, mean)
    plt.title('Annual rainfall between ' + str(year1) + ' and ' + str(year2))
    plt.xlabel('Year')
    plt.ylabel('rainfall, mm/year')
    
    #save figure
    plt.savefig('take2annual.png')
    return 

def correction(value):
    correct = value * 1.2 ** sqrt(2.0)
    return correct

def function1(file, year):
    correct = []
    with open(file, 'r') as f:
        filedata = json.load(f)
        
    yeardata = filedata[str(year)]
    
    for day in yeardata:
        newday = correction(day)
        correct.append(newday)
    
    return correct
        
def function2(file, year):
    correct = []
    with open(file, 'r') as f:
        filedata = json.load(f)
        
    yeardata = filedata[str(year)]
    
    '''more compact, quicker to run, but harder to understan'''
    correct = [correction(day) for day in yeardata]
    
    return correct

if __name__ == '__main__':
    data = loaddata('python_language_1_data.csv')
    savedictionary(data)
    graph('dictionary2.json', '1998', 'm')
    graph_mean('dictionary2.json', '1938', '1975')
    function2('dictionary2.json', '1980')