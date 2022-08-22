###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!BEFORE RUNNING THIS SCRIPT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###
###!!Download a copy of your https://www.youtube.com/feed/subscriptions into this directory as subs.html!!###
###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###

import os
import sys
from datetime import date
from bs4 import BeautifulSoup

#check whether the user has saved their subscriptions page before running the script
if not (os.path.isfile('subs.html')):
    print('Press CTRL+S on your https://www.youtube.com/feed/subscriptions page and save the html contents into this directory as subs.html before running.')
    sys.exit()

HTMLFileToBeOpened = open("subs.html", "r")
contents = HTMLFileToBeOpened.read()

#create new soup object based on html
soup = BeautifulSoup(contents, 'html.parser')

#create dictionary for subcriptions and their links
subs = dict()

#loop through all sidepanel items to find subscriptions along with their hrefs
for a in soup.find_all('a', href=True, class_="yt-simple-endpoint style-scope ytd-guide-entry-renderer"):
    subs[a['title']] = str(a.get_attribute_list('href')[0])

#remove unnecessary sidepanel items
subs.pop('Home')
subs.pop('Explore')
subs.pop('Subscriptions')
subs.pop('Originals')
subs.pop('Library')
subs.pop('History')
subs.pop('Your videos')
subs.pop('Watch later')
subs.pop('Downloads')
subs.pop('Liked videos')
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

#sort subcriptions alphabetically based on channel name
sorted_subNames = sorted(subs, key=str.lower)
sorted_subs = dict()

for sub in sorted_subNames:
  sorted_subs[sub] = subs[sub]

#write subcriptions to file
fileName = 'subscriptions ' + str(date.today()) + '.csv'
with open(fileName, 'w') as f:
    for name, link in sorted_subs.items():
        f.write(name + ',' + link + "\n")

print('Done! Wrote subscriptions to ' + fileName + '.csv')
