# Remove articles that come from useless aggregator websites or other irrelevant sites that show up in the feed

import pandas as pd
import datetime

# Set current date/time of script run
currentDT = datetime.datetime.now()
cleanDate = currentDT.strftime("%Y-%m-%d %H:%M:%S")


#Create a Python list of the blacklisted websites to filter out:

blacklist = [
	'somewebsite.com',
	'someotherwebsite.com'
	]

# Open the .csv
# Data Frame with *all* articles/links:
df = pd.read_csv('feed-articles.csv')

# fdf is the Filtered Data Frame
fdf = df[~df['post.link'].str.contains('|'.join(blacklist))]

# Write the filtered Data Frame back to CSV
fdf.to_csv('feed-articles.csv', index=False)

# Log the script running
log = open('feedlog.txt', 'a')
log.write(cleanDate + " The feed-articles.csv file has been filtered.\n")
log.close()
