#! python3
# quickShopper.py - Opens  several  product pages

import requests, sys, webbrowser, bs4

print('Searching..') # display text while downloading the Amazon page
res = requests.get('http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords= ' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.

linkElems = soup.select('.a-spacing-small a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))
	