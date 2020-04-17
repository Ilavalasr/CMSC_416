# Suraj Ilavala
# March 31st, 2020
# CMSC 416: PA4-WSD
# scorer.py
# 
# This program uses a wsd algorithim to predict context sense. After training given senses, in this case the training will recording the
# type of wording used in that specific sense and assigning it to the sense. After the training it the conext of the practice text will 
# be compared to the created inventory. Depending on which sense the context relates to more accurately, that senseid will be assigned to 
# the context. 
# Example input command is as follows, this is also how to run the program: 
#       python3 scorer.py my-line-answers.txt line-key.txt
#   The my-line-answers.txt is the results from the wsd.py. Th answers text will be compared to the line-key.txt to measure the efficiency 
#   of the wsd.py program. 
# Example output is as follows:
#       Efficiency: 90.55118110236221%
#       Total Correct Predictions: 115
#       Total Incorrect Predictions: 12
#       Total Number of Predictions: 127
#   The output will display the efficiency, the total number fo correct and incorrect predictions and total number of predictions.
# The algorithim used to find the probability is fairly simple. First I created two arrays one that contains my answers and the key.
# I compared the my answers and the key and checked if they matched, if they do match I added one to the counter. After going through all
# the predictions I divided the the number of correct predictions with the total predictions like this: 
# (num of correct prediction/num of total prediction)*100. I multiplied a 100 to get the percentage. 
# These were the results:
#       Efficiency: 90.55118110236221%
#       Total Correct Predictions: 115
#       Total Incorrect Predictions: 12
#       Total Number of Predictions: 127
# #

# import statements
import sys
import re
# opens appropriate files
answerf = open(sys.argv[1], "r")
keyf = open(sys.argv[2], "r")
# reads each file and stores in a string variable
answertxt = answerf.read()
keytxt = keyf.read()
# splits the string into an array
answerarr = re.split('\n', answertxt)
keyarr = re.split('\n', keytxt)

# instance variables to keep count of correct predictions and swift through the array
i = 0
count = 0
while i < len(answerarr):
    # checks if my answer is correct, if it is it adds a counter
    if answerarr[i] in keyarr[i]:
        count = count + 1
    i = i + 1
# prints the efficiency percentage, correct and incorrect predictions, and total number of predictions
print ("Efficiency: " + str(100 * float(count)/float(len(answerarr))) + "%")
print ("Total Correct Predictions: " + str(count))
print ("Total Incorrect Predictions: " + str(i - count))
print ("Total Number of Predictions: " + str(i))

