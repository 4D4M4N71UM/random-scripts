#!/bin/sh

### Copyright 2017 Adam Maynard
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

## Build for PAN-OS 7.1 External Dynamic Lists
## Mofidy phishing feed(s) to on-prem storage, for use in Palo EDL (URL Filtering)
## Tested on CentOS 7

# create cron job to keep list updated
# get your app key here: http://www.phishtank.com/developer_info.php

wget -O - http://data.phishtank.com/data/{your_app_key}/online-valid.csv | grep -oP '[0-9]{6,8},\K.*(?=,http:\/\/www\.phishtank\.com)' > /var/www/{your_folder}/public_html/phishtank-verified.txt 
sed -i -e 's/^"//' -e 's/"$//' /var/www/{your_folder}/public_html/phishtank-verified.txt
# Only keep the last 1000, due to EDL size restriction
head -n 1000 /var/www/{your_folder}/public_html/phishtank-verified.txt > /var/www/{your_folder}/public_html/phishtank-verified-1k.txt
rm -f /var/www/{your_folder}/public_html/phishtank-verified.txt
sed -ie 's/http:\/\///g' /var/www/{your_folder}/public_html/phishtank-verified-1k.txt
sed -ie 's/https:\/\///g' /var/www/{your_folder}/public_html/phishtank-verified-1k.txt
grep 'www.' /var/www/{your_folder}/public_html/phishtank-verified-1k.txt | sed -e 's/www\.//g' >> /var/www/{your_folder}/public_html/phishtank-verified-1k.txt
