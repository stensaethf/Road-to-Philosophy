'''
philosophy.py
Frederik Roenn Stensaeth

Python program to play the game 'all Wikipedia articles lead to philosophy'.
'''

# RULES TO IMPLEMENT:
# 1. Clicking on the first non-parenthesized, non-italicized link
# 2. Ignoring red links

# NOTES:
# parenthesis:
# 	(ousia) --> ousia is link.
# 	(and also Locke) --> Locke is link.
# 	(such as Baruch Spinoza, Gottfried Leibniz, and Christian Wolff) --> names are links.
# italics:
# 	i-tag will be parent of the a-tag.
# red links:
# 	from a quick investigation red links appear to start with /w/index.php?title=...
# 		--> this means that we will already be ignoring them, which is good.


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
						new_page = link[6:]
						if new_page != page:
							page = new_page
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