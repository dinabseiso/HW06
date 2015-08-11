#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write function(s) to assist you
#   - number of abecedarian words: 595
##############################################################################
# Imports

# Body

def is_abecedarian():
	fin = open("words.txt", "r")
	word = fin.readline()
	count = 0
	for word in fin : 
		word = word.strip()
		wordlength = len(word)
		indexLength = wordlength-1
		comparisonLength = indexLength - 1
		index = 0
		for index in range(indexLength) :
			if ord(word[index]) <= ord(word[index + 1]) :
				if index == comparisonLength : 
					print word
					count += 1
					#return True
			else : 
				break
	print count


##############################################################################
def main():
	is_abecedarian()

if __name__ == '__main__':
    main()
