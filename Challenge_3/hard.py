#/r/DailyProgrammer Challenge #3 [Hard]
#Unscrambling words and finding matches

import urllib as url
import itertools

def get_word_list():
	word_file = url.urlretrieve('http://pastebin.com/raw/jSD873gL', 'words.txt')
	word_list = open('words.txt').read().splitlines()
	return word_list

word_list = get_word_list()
scrambled_words = ['mkeart', 'sleewa', 'edcudls', 'iragoge', 'usrlsle', 'nalraoci',
					'nsdeuto', 'amrhat', 'inknsy', 'iferkna']
found_words = []

for i in range(0, len(scrambled_words)):
	permutations = itertools.permutations(scrambled_words[i])
	perm_list = [''.join(x) for x in permutations]
	
	for j in range(0, len(perm_list)):
		if perm_list[j] in word_list:
			found_words.append(perm_list[j])

found_words = list(set(found_words))

for i in range(0, len(found_words)):
	print "Found:", found_words[i]