# Remove articles that come from useless aggregator websites

import requests
import pandas as pd
import datetime

# Set current date/time of script run
currentDT = datetime.datetime.now()
cleanDate = currentDT.strftime("%Y-%m-%d %H:%M:%S")

# Download the newest blacklist from the website

url = "https://somedomain.com/blacklist"
r = requests.get(url, allow_redirects=False)
open('blacklist.txt', 'wb').write(r.content)

# Log blacklist download/update
log = open('feedlog.txt', 'a')
log.write(cleanDate + " The blacklist has been updated.\n")

# Import blacklist.txt (a simpe text file, one domain entry per line)
with open("blacklist.txt") as f:
    blacklist = f.read().splitlines()

# Open the .csv
# Data Frame with *all* articles/links:
df = pd.read_csv('feed-articles.csv')

# fdf is the Filtered Data Frame
fdf = df[~df['post.link'].str.contains('|'.join(blacklist))]

# Write the filtered Data Frame back to CSV
fdf.to_csv('feed-articles.csv', index=False)

# Log the script running
log.write(cleanDate + " The feed-articles.csv file has been filtered.\n")
log.close()
