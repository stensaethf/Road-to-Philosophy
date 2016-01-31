'''
philosophy.py
Frederik Roenn Stensaeth

Python program to play the game 'all Wikipedia articles lead to philosophy'.
'''

import sys
import requests
from bs4 import BeautifulSoup as BS

def philosophy(page):
	seen = {}
	seen[page] = True
	print page

	while page != 'Philosophy':
		# load that Wikipedia page.
		r = requests.get('http://en.wikipedia.org/w/index.php?title=' + page)
		soup = BS(r.content)
		# grab first link on that page and set page equal to that.
		first = True
		for p in soup.find_all('p'):
			for a in p.find_all('a'):
				link = a['href']
				if link[:6] == '/wiki/':
					if first == True:
						page = link[6:]
						first = False
		if first == True:
			print 'There appears to not be any links on the\'' + page + '\' site...'
			sys.exit()
		print page
		if page in seen:
			print 'Cycle detected! We have seen \'' + page + '\' before...'
			sys.exit()
		else:
			seen[page] = True

def main():
	if len(sys.argv) != 2:
		print 'Sorry, looks like you provided an incorrect number of arguments...'
		print 'Usage: $ python philosophy.py <starting title>'
		sys.exit()
	philosophy(sys.argv[1])


if __name__ == '__main__':
	main()