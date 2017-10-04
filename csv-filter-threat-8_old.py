#!/usr/bin/env python3

### Copyright 2017 Adam Maynard
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# Build for PAN-OS 8

## Export Palo Alto threat log as csv, then use this to filter the junk
import pandas as pd
#Rename your csv file and remove ".csv" if you want to append later
infile = input("Enter the CSV file location (E:/Users/someuser/somefile.csv): ")
#savefile = input("Enter the CSV save file location (E:/Users/someuser/savefile.csv): ")
f=pd.read_csv(infile)
keep_col = ['Receive Time','Source address','Destination address','Application','Repeat Count','Source Port','Destination Port','IP Protocol','URL/Filename','Threat/Content Name','Source Country','Destination Country']
new_f = f[keep_col]
new_f.to_csv(infile + "-log.csv", index=False)
