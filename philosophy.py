'''
philosophy.py
Frederik Roenn Stensaeth

Python program to play the game 'all Wikipedia articles lead to philosophy'.
'''

# RULES TO IMPLEMENT:
# 1. Clicking on the first non-parenthesized

# NOTES:
# parenthesis:
# 	(ousia) --> ousia is link.
# 	(and also Locke) --> Locke is link.
# 	(such as Baruch Spinoza, Gottfried Leibniz, and Christian Wolff) --> names are links.


import sys
import requests
from bs4 import BeautifulSoup as BS

def getFirstLink(soup, article):
	"""
	getFirstLink() finds the first link (a-tag) for a given Wikipedia article.
	The url title of the link is returned. Prints an error message and quits
	if no link was found in the article.

	I moved these loops to a separate function to make the algorithm slightly
	faster by returning when we find a link. Including break statements seemed
	like an ugly solution to the problem.

	@params: soup and current article title.
	@return: url title of first link in the article.
	"""
	# the text body is within p-tags, so get those first.
	for p in soup.find_all('p'):
		# further we want the links, right? so we get those as well.
		for a in p.find_all('a'):
			link = a['href']
			# now we make sure that we follow the various rules of the game.
			# 1. Link to Wikipedia.
			# 2. First link.
			# 3. No italics.
			# 4. No red link. We appear to be doing this by making sure the link
			# 	 is /wiki/.
			if link[:6] == '/wiki/':
				new_article = link[6:]
				if new_article != article:
					if a.parent.name != 'i':
						return new_article
	print 'There appears to not be any links on the\'' + article + '\' site...'
	sys.exit()

def philosophy(article_start, article_end):
	"""
	philosophy() finds the path of Wikipedia articles that you need to visit in order
	to get from the start article to the end article.

	@params: page title to start at and page title to end at.
	@return: n/a.
	"""
	seen = {}
	seen[article_start] = True
	print article_start

	while article_start != article_end:
		# load that Wikipedia page.
		r = requests.get('http://en.wikipedia.org/w/index.php?title=' + article_start)
		soup = BS(r.content)
		article_start = getFirstLink(soup, article_start)
		print article_start
		if article_start in seen:
			print 'Cycle detected! We have seen \'' + article_start + '\' before...'
			sys.exit()
		else:
			seen[article_start] = True

def main():
	if len(sys.argv) != 3:
		print 'Sorry, looks like you provided an incorrect number of arguments...'
		print 'Usage: $ python philosophy.py <starting title> <ending title>'
		sys.exit()
	philosophy(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
	main()