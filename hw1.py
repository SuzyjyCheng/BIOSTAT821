#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_data(file):
    r_file = open(file, "r")
    list_of_lists = []
    for line in r_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        int_list = [int(i) for i in line_list]
        list_of_lists.append(int_list)
        
    return list_of_lists


# In[2]:


get_data("/Users/Suzy/Desktop/BIOSTAT 821/example.txt")


# In[3]:


dat = get_data("/Users/Suzy/Desktop/BIOSTAT 821/example.txt")


# In[43]:


import math
dsum = sum(sum(i) for i in dat)
count = 0
var = 0
for i in range(len(dat)):
    count = count + len(dat[i])
    avg = round(dsum/count, 1)
    var = var + sum([((x - avg) ** 2) for x in dat[i]])
    variance = round((var/count) ** 0.5, 1)

print(avg)
print(variance)


# In[62]:


import math
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


print(avg)
print(sd)
print(cov)
print(corr)
    

