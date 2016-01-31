'''
philosophy.py
Frederik Roenn Stensaeth

Python program to play the game 'all Wikipedia articles lead to philosophy'.
'''

import sys

def philosophy(page):
	# load given page.
	seen = {}
	seen[page] = True
	print page
	while page != 'Philosophy':
	# 	load that Wikipedia page.
	# 	grab first link on that page and set page equal to that.
		print page
		if page in seen:
			print 'Cycle detected! We have seen \'' + page + '\' before...'
			sys.exit()

def main():
	if len(sys.argv) != 2:
		print 'Sorry, looks like you provided an incorrect number of arguments...'
		print 'Usage: $ python philosophy.py <starting title>'
		sys.exit()
	philosophy(sys.argv[1])


if __name__ == '__main__':
	main()