import pandas as pd 
import matplotlib.pyplot as plt
import csv
import General_classes as gc 
import numpy as np 



# Organisering av eget listesystem for datasettet ([kolonne][rad])
data = pd.read_csv('data.csv', sep=';', encoding='latin-1')
data_universal_list = []
keys = data.keys()

b=0 
for i in keys:
    data_universal_list.append([])
    for j in data[str(i)]:
        data_universal_list[b].append(j)
    b+=1

# Organisering av eget listesystem for datasettet ([rad][kolonne])
data_universal_list_2 = []

with open('data.csv', encoding='latin-1') as fil:
    filinnhold = csv.reader(fil, delimiter=';')

    headers = next(filinnhold) #Overskriftene blir lagt inn i headers og vil ikke bli med i listesystemet

    c=0
    for rad in filinnhold:
        data_universal_list_2.append([])
        for j in range(0, len(rad)):
            data_universal_list_2[c].append(rad[j])
        c+=1
