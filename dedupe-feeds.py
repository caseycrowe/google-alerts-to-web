# This script deduplicates news items in the feed_articles.csv file

import pandas as pd
import datetime

# Set current date/time of script run
currentDT = datetime.datetime.now()
cleanDate = currentDT.strftime("%Y-%m-%d %H:%M:%S")
 
# Dedupe the feed_articles.csv file in place with Pandas
df = pd.read_csv('feed-articles.csv',encoding = "ISO-8859-1")
df.drop_duplicates(subset="date",inplace=True)
df.to_csv('feed-articles.csv', index=False)

# Log the script running
log = open('feedlog.txt', 'a')
log.write(cleanDate + " The feed-articles.csv file has been deduped.\n")
log.close()
