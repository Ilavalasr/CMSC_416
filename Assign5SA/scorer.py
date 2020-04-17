# Suraj Ilavala
# April 14, 2020
# CMSC 416: PA5-Sentiment Analysis
# scorer.py
# 
# This program uses a wsd algorithim to predict context sentiment. After training given sentiments, in this case the training will recording the
# type of wording used in that specific sentiment and assigning it to the sentiment. After the training it the conext of the practice text will 
# be compared to the created inventory. Depending on which sentiment the context relates to more accurately, that sentiment will be assigned to 
# the context. 
# Example input command is as follows, this is also how to run the program: 
#       python3 scorer.py my-sentiment-answers.txt sentiment-test-key.txt
#   The my-sentiment-answers.txt is the results from the wsd.py. Th answers text will be compared to the sentiment-key.txt to measure the efficiency 
#   of the wsd.py program. 
# Example output is as follows:
#       Efficiency: 69.95708154506438%
#       Total Correct Predictions: 163
#       Total Incorrect Predictions: 70
#       Total Number of Predictions: 233
#       Confusion Matrix: 
#       Negatives mistaken for positive: 33
#       Positives mistaken for negative: 37
#   The output will display the efficiency, the total number fo correct and incorrect predictions and total number of predictions.
# The algorithim used to find the probability is fairly simple. First I created two arrays one that contains my answers and the key.
# I compared the my answers and the key and checked if they matched, if they do match I added one to the counter. After going through all
# the predictions I divided the the number of correct predictions with the total predictions like this: 
# (num of correct prediction/num of total prediction)*100. I multiplied a 100 to get the percentage. For the confusion matrix I simply kept
# track of which output were supposed to be negative but gave positive and vice versa. 
# These were the results:
#   Efficiency: 69.95708154506438%
#   Total Correct Predictions: 164
#   Total Incorrect Predictions: 69
#   Total Number of Predictions: 233
#   Confusion Matrix: 
#   Negatives mistaken for positive: 31
#   Positives mistaken for negative: 38
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
pton = 0
while i < len(answerarr):
    # checks if my answer is correct, if it is it adds a counter counts for the confusion matrix
    if answerarr[i] in keyarr[i]:
        count = count + 1
    elif "positive" in answerarr[i]:
        pton = pton + 1
    i = i + 1
# prints the efficiency percentage, correct and incorrect predictions, and total number of predictions
print ("Efficiency: " + str(100 * float(count)/float(len(answerarr))) + "%")
print ("Total Correct Predictions: " + str(count))
print ("Total Incorrect Predictions: " + str(i - count))
print ("Total Number of Predictions: " + str(i))
# displays the count of one confusion and subtracts the count from the incorrect predictions for the other confusion
print ("Confusion Matrix: ")
print ("Negatives mistaken for positive: " + str(pton))
print ("Positives mistaken for negative: " + str(i-count-pton))
