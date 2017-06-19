#!/usr/bin/env python3

### Copyright 2017 Adam Maynard
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# Build for PAN-OS 7.1

import pandas as pd
## Export Palo Alto traffic log as csv, then use this to filter the junk
#Rename your csv file and remove ".csv" if you want to append later
infile = input("Enter the CSV file location (C:/Users/someuser/somefile.csv): ")
f=pd.read_csv(infile)
#Choose the headers you want to keep
keep_col = ['Receive Time','Source address','Destination address','Application','Repeat Count','Source Port','Destination Port','IP Protocol','Source Country','Destination Country']
new_f = f[keep_col]
#save and append the filtered csv file
new_f.to_csv(infile + "-log.csv", index=False)
