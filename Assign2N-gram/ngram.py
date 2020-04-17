# Suraj Ilavala
# CMSC 416
# Programming Assignment 2
# Due: 13 February 2020
# 
# The purpose of this program to create sentences using an n-gram. The n-gram is basically a 
# certain number words grouped together and use them to create new sentences with the same words 
# but randomily put together. The instructions would be making sure all the text files that you 
# are using to process through the n-gram is in the same location as the ngram.py.
# The command line should be input like this:
#       ngram.py n m input-file/s
#       Example:
#       ngram.py 3 10 pg1497.txt pg2500.txt
# this example will process a trigram from the 3, n is the n-gram. The m is the number of sentences, 
# in the example case its 10 sentences. The algorithim used is a basic runs through the text removes 
# and symbols from the text file before storing it. I also subbed "?" and "!" with a ".". This so I can 
# use only one element as a exit element. After I kept adding the words that has been processed through 
# the n-gram, it stops adding when a "." is found then it prints the whole sentence up to the period. 
# sources used where python docs and learning python. 

import sys
import re
import random
#This gets the number of arguments given when the python program is run
filenum = len(sys.argv) - 1
#gets the n-gram and the number of sentences from the arguments
#if no arguments are given an error is thrown 
ngramNum = int(sys.argv[1])
numOfSentences = int(sys.argv[2])
lfile = 3
bookTxt = ""
#this will make sure all files that are given in the command line are taken in and registered.
while (lfile<=filenum):
    with open(sys.argv[lfile], 'r') as temp:
        bookTxt += temp.read()
    lfile = lfile + 1
bookTxt = bookTxt.lower()
#replaces all ? and ! with "." so that we can use a "." as a exit element
bookTxt = re.sub("[\?|!]", ".", bookTxt)
bookTxt = re.sub(r'[^A-Za-z0-9., ]', '', bookTxt)

words = bookTxt.split(" ")
#combines words depending on the n-gram initially inputed
ngramwords = [" ".join(words[i: i + ngramNum]) for i in range(0, len(words), ngramNum)]
sentence = ""
#this is where the sentences are formed and printed.
for i in range(numOfSentences):
    sentence = sentence + " " + ngramwords[random.randrange(len(ngramwords))]
    #Keeps adding words that have been filtered using the n-gram length
    #it exits when "." is shown
    while "." not in sentence:
        sentence = sentence + " " + ngramwords[random.randrange(len(ngramwords))]
    else:
        #finds the location of "." and prints out everything up until the "."
        endOfSent = sentence.find(".")
        print(str(i+1) + ") " + sentence[0:endOfSent+1])
    #resets the sentence
    sentence = ""
