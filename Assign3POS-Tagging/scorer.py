# Suraj Ilavala
# March 3, 2020
# CMSC 416: POS Tagging
# Assignment 3: scorer.py
# 
# The problem solved here is tagging words with penn tree bank pos tagset. Each individual word is stored with 
# the according pos tag. After each tag is stored it is then used to analyze the text in the test document. 
# After running through the test document with the tagger the list of all the words and its tags are printed 
# to a document. Then it test the efficiency with the actual key. It compares the actual key with created taged file.
# The Effeciency percentange is 79.1732657586%.
# Example: to completely measure the efficiency of the tagger you have to print it to a file like so
#           --> python scorer.py pos-test-with-tags.txt pos-test-key.txt > pos-tagging-report.txt
#
#   make sure to have the tagged test file first and the the key file next
# Using the key to compare to the tagged to check how efficient the tagger previously created is. To do this I counted 
# the test tags that match the key. After counting, I used that number and divided it with the total words in test file.
# the equation used is this ((matched words)/(total words in test))*100. With this I got 79.1732657586% efficiency. 
# The confusion matrix will consist of total number of tags,  
#
# #
import sys
import re
#reads in the files and stores it
testtagsfile = open(sys.argv[1], "r")
keytagsfile = open(sys.argv[2], "r")
testtagsf = testtagsfile.read()
keytagsf = keytagsfile.read()
#gets rid of the '[]'and creates a array of all the words in the test tag file and and key file
readytesttag = re.sub(r'\[|\]', "", testtagsf)
readykeytag = re.sub(r'\[|\]', "", keytagsf)
testarr = re.split('\s+', readytesttag)
keyarr = re.split('\s+', readykeytag)
#variable used to keep count
count = 0
i = 0
#runs throught the words and counts the matchs
while i < len(keyarr):
    if(testarr[i] in keyarr[i]):
        count = count + 1
    i = i + 1
#gets the total number of words in test tag file
total = len(testarr)
#gets the percentage of the efficiency of the tagger
print("Efficiency: " + str(100 * float(count)/float(total))+"%")
print("\t")
#prints total tagged, correct tags, and incorrect tags
print("Total Tagged: " + str(len(testarr)))
print("Total correct tags: " + str(count))
print("Incorrect Tags: " + str(len(testarr)-count))