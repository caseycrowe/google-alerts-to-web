# This file uploads the feed_articles.csv to the FTP server

from ftplib import FTP
import datetime

# Set current date/time of script run
currentDT = datetime.datetime.now()
cleanDate = currentDT.strftime("%Y-%m-%d %H:%M:%S")

# Store login credentials
ftp = FTP('yourdomain.org')
ftp.login('username@yourdomain.org', 'somepass')

# Change to News folder
ftp.cwd('news')

# Check for yesterday's backup of the articles, and delete it,
# then rename today's to .old to create a backup
oldCsv = 'feed-articles.old'
newCsv = 'feed-articles.csv'
if oldCsv in ftp.nlst('feed-articles.old'):
	ftp.delete('feed-articles.old')
	ftp.rename('feed-articles.csv', 'feed-articles.old')

# Copy the new file to the ftp server
with open('feed-articles.csv', 'rb') as f:
    ftp.storlines('STOR %s' % 'feed-articles.csv', f)

# Verify the both files exist on the server and log the results
if oldCsv and newCsv in ftp.nlst():
	log = open('feedlog.txt', 'a')
	log.write(cleanDate + " feed-articles.csv has been uploaded\n")
	log.close()
ftp.quit()
