#!/bin/sh

### Copyright 2017 Adam Maynard
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

## Build for PAN-OS 7.1 External Dynamic Lists
## Mofidy threat feeds to on-prem storage, for use in Palo EDL (blocklist)
## Tested on CentOS 7

# create cron job to keep list updated

wget -O - https://www.binarydefense.com/banlist.txt | grep -v '#' | grep -v -e '^$' > /var/www/{your_folder}/public_html/banlist.txt

wget -O - https://blocklist.net.ua/blocklist.csv | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' > /var/www/{your_folder}/public_html/blocklist.net.ua.txt

wget -O - http://www.dartmouth.edu/~blocked/world-list.html | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' > /var/www/{your_folder}/public_html/dartmouth-blocklist.txt

wget -O - http://www.ipspamlist.com/public_feeds.csv | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' > /var/www/{your_folder}/public_html/ipspamlist.txt
