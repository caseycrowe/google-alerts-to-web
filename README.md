# google-alerts-to-web
This project pulls Google's Atom feeds to a .CSV, and FTPs them to a web server, where they're displayed with PHP.

I wanted to keep abreast of news articles related to a very specific subject, and share that with a few other people that were interested. I began by trying to display Google Alert's raw XML page on my site, but it posed two problems. First, they prohibit cross-site loading. So you can view their page directly without issue, but can't load it from another site. Second, the articles only stay live on the alert for about a day. After that they are removed. So I wanted them to persist, which meant saving them somewhere. A database seemed too heavy-handed, so I settled on .CSV since I'm not changing my query. 

So this has a few different steps, and each step is its own file. I should note here that I run this all from a Raspberry Pi on my home network, and upload the feed-articles.csv to the webserver. Though if you had access to Python and the required modules and cron, you could do all this locally and skip the FTP.

1. read-feeds.py pulls the feeds down to feed-articles.csv
2. filter-feeds.py loads feed-articles.csv, and removes any entries containing blacklisted sites
3. dedupe-feeds.py loads feed-articles.csv, and removes any articles that appear twice. Since I have numerous alerts, this prevents dupes.
4. ftp-articles.py connects to an FTP server, deletes the backup copy of the feed-articles.csv (feed-articles.old), renames feed-articles.csv to feed-articles.old, and uploads a fresh copy of feed-articles.csv. 
5. Each of the above files logs the time, date, and some informational data to feedlog.txt for easy status checking.


