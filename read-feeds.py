# This script pulls feeds from Google Alerts into the feed-articles.csv file
#
# Google Alerts are stored in Atom format, and not directly readable from a webpage
#
# To add a feed, simply create the RSS feed and add it to the list below

from time import mktime
import feedparser
import datetime
import time
import csv
import re
 
# The Python list of feeds
feed_URLS = [
  'https://www.google.com/alerts/feeds/12345/12345' # Feed name #1
  'https://www.google.com/alerts/feeds/54321/54321', # Feed name #2
  ]
 
# Parse the URLS with Feedparser, and extend/append the list of posts
posts = []
for url in feed_URLS:
  posts.extend(feedparser.parse(url).entries)
 
# Capture some data about the run for the log file
feedCount = str(len(feed_URLS)) # Count the feeds
postCount = str(len(posts)) # Count the posts
runTime = str(time.strftime('%m-%d-%Y %H:%M')) # Capture the date/time to string
# Set current date/time of script run
currentDT = datetime.datetime.now()
cleanDate = currentDT.strftime("%Y-%m-%d %H:%M:%S")
 
# Strip annoying <b>,</b>, and other annoying characters in titles and content
# There is a better way to do this, but I've not dug in and written it yet
for post in posts:
  post.title = re.sub('<b>', '', post.title)
  post.title = re.sub('</b>', '', post.title)
  post.title = re.sub('\u2014', '-', post.title) # emdash
  post.title = re.sub('\u201c', '&quot;', post.title) # left double quote
  post.title = re.sub('\u201d', '&quot;', post.title) # right double quote
  post.content[0].value = re.sub('<b>', '', post.content[0].value)
  post.content[0].value = re.sub('</b>', '', post.content[0].value)
  post.content[0].value = re.sub('\u2014', '-', post.content[0].value) # emdash
  post.content[0].value = re.sub('\u201c', '&quot;', post.content[0].value) # left double quote
  post.content[0].value = re.sub('\u201d', '&quot;', post.content[0].value) # right double quote
 
# Write the data to a CSV 'feed_articles.csv'
with open('feed-articles.csv', mode='a', newline='') as feed_articles:
  article_writer = csv.writer(feed_articles, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  for post in posts:
    # Put the struct time format into epoch time (seconds)
    date = mktime(post.published_parsed)
    article_writer.writerow([date, post.title, post.content[0].value, post.link])
 
# Write the data to the log file parselog.txt
log=open('feedlog.txt', 'a+')
log.write(cleanDate + ' There were ' + postCount + ' articles across ' + feedCount + ' feeds.\n')
log.close()
