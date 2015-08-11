#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################
# Imports
def getWord():
	fin = open("words.txt", "r")
	line = fin.readline()
	word = line.split()
	return word 

def uses_all(necessaryLetters):
	fin = open("words.txt", "r")
	line = fin.readline()
	word = line.split()
	count = 0
	necessaryLetters = list(necessaryLetters)
	for word in fin:
		j = len(necessaryLetters)
		while j > 0 :
			for i in necessaryLetters:
				if i in word:
					j -= 1
					if j == 0:
						count += 1
						#print word
						#return True
				else : 
					j = 0
					continue
	fin.close()
	return count


# Body


##############################################################################
def main():
	print uses_all("aeiou")
	print uses_all("aeiouy")

if __name__ == '__main__':
    main()
