#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body
# def has_no_e():
# 	noE = []
# 	allWords = []
# 	check = True
# 	while check == True: 
# 		word = raw_input("Please enter a word. We will check to see if it has an 'e'. Type 'done' when done.: \n") 
# 		allWords.append(word)
# 		if ("e" not in word): 
# 			noE.append(word)
# 			check = True
# 			print("That word did not have an 'e' in it!")
# 			has_no_e()
# 			#return True 
# 		elif word == "done":
# 			check = False
# 		else : 
# 			check = True 
# 			print("That word had an 'e' in it!")
# 			has_no_e()
# 			#return False
# 	percentageOfNoE = ( len(noE) / len(allWords) ) * 100
# 	print percentageOfNoE

def has_no_e(word):
	if ("e" not in word):
		return True
	else : 
		return False

def sort_noE():
	fin = open("words.txt", "r")
	allWords = []
	noE = []
	word = fin.readline()
	for word in fin: 
		allWords.append(word)
		has_no_e(word)
		if has_no_e(word) == True:
			print word
			noE.append(word)
		else : 
			continue
	percentageOfNoE = (len(noE) / float(len(allWords))) * 100
	print percentageOfNoE
	fin.close()




##############################################################################
def main():
	sort_noE()

if __name__ == '__main__':
    main()
