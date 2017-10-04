#!/usr/bin/env python3

### Copyright 2017 Adam Maynard
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# Build for PAN-OS 8

## Export Palo Alto threat log as csv, then use this to filter the junk
import pandas as pd, sys, argparse, os.path

parser = argparse.ArgumentParser(description='-- Removes junk columns from Palo Alto threat log exported as CSV. --- Example: "py csv-filter-threat-8.py -i C:\\threat-log.csv -o ." (\'.\' = cd)')
parser.add_argument("-i", "--input", help='input source csv file (with path)')
parser.add_argument("-o", "--output", help='output path to save the new csv file')
args = parser.parse_args()

winpath = args.input
newpath = args.output
infile = winpath.replace("\\","/")
savepath = newpath.replace("\\","/")
f=pd.read_csv(infile)
keep_col = ['Receive Time','Source address','Destination address','Application','Repeat Count','Source Port','Destination Port','IP Protocol','URL/Filename','Threat/Content Name','Source Country','Destination Country']
new_f = f[keep_col]
new_f.to_csv(savepath + '/' + os.path.basename(infile.rsplit( ".", 1 )[ 0 ]) + "-threat.csv")