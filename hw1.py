#!/usr/bin/env python
# coding: utf-8

# get data function
def get_data(file):
    r_file = open(file, "r")
    list_of_lists = []
    for line in r_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        int_list = [int(i) for i in line_list]
        list_of_lists.append(int_list)
        
    return list_of_lists



#output
get_data("/Users/Suzy/Desktop/BIOSTAT 821/example.txt")


#function to analyze average, standard deviation, covariance and correlation
import math
def analyze_data(dat, option):
    newlist = []
    for i in range(len(dat)):
        newlist = newlist + dat[i]
 
    
    avg = round(sum(newlist)/len(newlist),1)
    var = sum([((x - avg) ** 2) for x in newlist])/len(newlist)
    sd = round(var ** 0.5, 1)

    covariance_temp_sum = 0
    mean_d0 = math.fsum(dat[0]) / len(dat[0])
    mean_d1 = math.fsum(dat[1]) / len(dat[1])
    for x in range(len(dat[0])):
        covariance_temp_sum = covariance_temp_sum + (dat[0][x] - mean_d0) * (dat[1][x] - mean_d1)
    cov = round((covariance_temp_sum / len(dat[0])),2)

    sd0 = (sum([((x - mean_d0) ** 2) for x in dat[0]])/len(dat[0]))**0.5
    sd1 = (sum([((x - mean_d1) ** 2) for x in dat[1]])/len(dat[1]))**0.5
    corr = round(cov/(sd0 * sd1), 3)

    if option == "average":
        return avg
    elif option == "standard deviation":
        return sd
    elif option == "covariance":
        return cov
    elif option == "correlation":
        return corr
   
dat = get_data("/Users/Suzy/Desktop/BIOSTAT 821/example.txt")
Average = analyze_data(dat, "average")
Standard_deviation = analyze_data(dat, "standard deviation") 
Covariance = analyze_data(dat, "covariance")
Correlation = analyze_data(dat, "correlation")

#output
print(Average)
print(Standard_deviation)
print(Covariance)
print(Correlation)


 
