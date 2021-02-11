#!/usr/bin/env python
# coding: utf-8
import pandas as pd
df = pd.read_csv('001.txt')
for n in range(2,6):
    tu='data'+str(n)+''
    pu='00'+str(n)+'.txt'
    df[tu]= pd.read_csv(pu,' ')
df.to_csv(r'alldata.csv') #,index=False) activate to erase index

