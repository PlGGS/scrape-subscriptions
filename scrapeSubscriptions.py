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
  
subs = dict()

for sub in soup.findAll('ytd-guide-entry-renderer', {'class': 'style-scope ytd-guide-section-renderer'}):
    if sub.find('yt-formatted-string').get_text():
        subs[sub.text.strip()] = ''

for sub in soup.findAll('ytd-guide-entry-renderer', {'class': 'style-scope ytd-guide-collapsible-entry-renderer'}):
    if sub.find('yt-formatted-string').get_text():
        subs[sub.text.strip()] = ''

for a in soup.find_all('a', href=True, class_="yt-simple-endpoint style-scope ytd-guide-entry-renderer"):
    subs[a['title']] = str(a.get_attribute_list('href')[0])

# print(subs)

# subs.sort(key=str.lower)

subs.pop('Home')
subs.pop('Explore')
subs.pop('Shorts')
subs.pop('Subscriptions')
subs.pop('Originals')
subs.pop('Browse channels')
subs.pop('Library')
subs.pop('History')
subs.pop('Your videos')
subs.pop('Watch later')
subs.pop('Downloads')
subs.pop('Liked videos')
subs.pop('Show 676 more')
subs.pop('Show less')
subs.pop('Show more')
subs.pop('Movies & Shows')
subs.pop('Gaming')
subs.pop('Live')
subs.pop('Fashion & Beauty')
subs.pop('Learning')
subs.pop('Sports')
subs.pop('Creator Studio')
subs.pop('YouTube Music')
subs.pop('YouTube Kids')
subs.pop('YouTube TV')
subs.pop('Settings')
subs.pop('Report history')
subs.pop('Help')
subs.pop('Send feedback')

sorted_subNames = sorted(subs, key=str.lower)
sorted_subs = dict()

for sub in sorted_subNames:
  sorted_subs[sub] = subs[sub]

fileName = 'subscriptions ' + str(date.today()) + '.csv'
with open(fileName, 'w') as f:
    for name, link in sorted_subs.items():
        f.write(name + ',' + link + "\n")

print('Outputed subscriptions to ' + fileName + '.csv')
