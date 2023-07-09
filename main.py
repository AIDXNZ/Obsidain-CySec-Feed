import requests
from transformers import pipeline
import feedparser
import os
# List of RSS feed URLs
rss_feeds = [
    "https://www.nist.gov/blogs/cybersecurity-insights/rss.xml"
    # Add more feed URLs as needed
]

import xml.etree.ElementTree as ET

# Change to Obsidian Vault Path
# Can use user input here
os.chdir("../../ObsidianSync")
open("cysecnews.md")



# Fetch and combine RSS feed data
summaries = []

count = 0
for rss_feed in rss_feeds:
    feed = feedparser.parse(rss_feed)
    for i in range(10):
        if count <= 10:
            #Create summarization pipeline
            count += 1
            #summarizer = pipeline("summarization", model='sshleifer/distilbart-cnn-12-6')
            #summary = summarizer(feed.entries[i].description, max_length=50, min_length=10, do_sample=False)
            #print(summary[0]['summary_text'])
            summaries.insert(count, "## "+feed.entries[i].title + "\n"+ feed.entries[i].description + "\n "+feed.entries[i].link + "\n\n")

f = open("../../Documents/ObsidianSync/cysecnews.md", "w")
for summary in summaries:
    f.write(str(summary))
f.close()
