###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!BEFORE RUNNING THIS SCRIPT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###
###!!Download a copy of your https://www.youtube.com/feed/subscriptions into this directory as subs.html!!###
###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###

import os
import sys
from datetime import date
from bs4 import BeautifulSoup

if not (os.path.isfile('subs.html')):
    print('Press CTRL+S on your https://www.youtube.com/feed/subscriptions page and save the html contents into this directory as subs.html before running.')
    sys.exit()

HTMLFileToBeOpened = open("subs.html", "r")
contents = HTMLFileToBeOpened.read()
soup = BeautifulSoup(contents, 'html.parser')
  
subs = set()

for sub in soup.findAll('ytd-guide-entry-renderer', {'class': 'style-scope ytd-guide-section-renderer'}):
    if sub.find('yt-formatted-string').get_text():
        subs.add(sub.text.strip())

for sub in soup.findAll('ytd-guide-entry-renderer', {'class': 'style-scope ytd-guide-collapsible-entry-renderer'}):
    if sub.find('yt-formatted-string').get_text():
        subs.add(sub.text.strip())

subList = list(subs)
subList.sort(key=str.lower)

subList.remove('Show 676 more')
subList.remove('Show less')
subList.remove('Show more')
subList.remove('Movies & Shows')
subList.remove('Gaming')
subList.remove('Live')
subList.remove('Fashion & Beauty')
subList.remove('Learning')
subList.remove('Sports')
subList.remove('Creator Studio')
subList.remove('YouTube Music')
subList.remove('YouTube Kids')
subList.remove('YouTube TV')
subList.remove('Settings')
subList.remove('Report history')
subList.remove('Help')
subList.remove('Send feedback')

fileName = 'subscriptions ' + str(date.today()) + '.txt'
with open(fileName, 'w') as f:
    for sub in subList:
        f.write(sub+"\n")

print('Outputed subscriptions to ' + fileName + '.txt')
