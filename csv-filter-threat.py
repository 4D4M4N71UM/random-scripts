#!/usr/bin/env python3
## Export Palo Alto threat log as csv, then use this to filter the junk
import pandas as pd
#Rename your csv file and remove ".csv" if you want to append later
infile = input("Enter the CSV file location (C:/Users/someuser/somefile.csv): ")
f=pd.read_csv(infile)
#Choose the headers you want to keep
keep_col = ['Receive Time','Source address','Destination address','Application','Repeat Count','Source Port','Destination Port','IP Protocol','URL','Threat/Content Name','Source Country','Destination Country']
new_f = f[keep_col]
#save and append the filtered csv file
new_f.to_csv(infile + "-log.csv", index=False)