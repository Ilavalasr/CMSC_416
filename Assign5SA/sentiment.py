# Suraj Ilavala
# April 14, 2020
# CMSC 416: PA5-Sentiment Analysis
# sentiment.py
#
# This program uses a sentiment algorithim to predict sentiment. After training a given sentiment, in this case the training will record the
# type of wording used in that specific sentiment and assigns it to the sentiment. After the training it, the conext of the practice text will 
# be compared to the created inventory. Depending on which sentiment the context relates to more accurately, that sentiment will be assigned to 
# the context. 
# Example input command is as follows, this is also how to run the program: 
#       python3 sentiment.py sentiment-train.txt sentiment-test.txt my-model.txt > my-sentiment-answers.txt
#   the sentiment-train.txt is the txt used to create the sentiment inventory and sentiment-test.txt is where the practice context is located to assign
#   the sentiment after comparing the context to the sentiment inventory. The my-model.txt is a document that shows the sentiment inventory
#   created. Any stdout will be printed to my-sentiment-answers.txt which will then be used in the scorer.py. Make sure all these files are
#   in the same location/folder
# Actual training input from a text will look like this:
#           <instance id="620821002390339585">
#           <answer instance="620821002390339585" sentiment="negative"/>
#           <context>
#               Does @macleansmag still believe that Ms. Angela Merkel is the "real leader of the free world"?  http://t.co/isQfoIcod0 (Greeks may disagree
#           </context>
#           </instance>
# Actual test input from a text will look like this:
#           <instance id="620979391984566272">
#           <context>
#               On another note, it seems Greek PM Tsipras married Angela Merkel to Francois Hollande on Sunday #happilyeverafter http://t.co/gTKDxivf79
#           </context>
#           </instance>
#   Please take note of the key difference between test and train text. The train text contains a "answer instance" while test does not.
# Here is a example of output:
#           <answer instance="620979391984566272" sentiment="negative"/>
#   This will will be compared to the key to test the efficiency of the program
# The model used to solve this uses Naive bayes. For this algorithim, I first created sentiment inventories with the train text to identify what 
# was common in one particular sentiment. After the sentiment invetories were made I took the individual words of the context in test and tested to 
# see if that word is consistent with that sentiment. If it was a counter was added. After checking the words in both sentiment inventories I would 
# choose the sentiment which the context is more consistent with. For example, lets say for sentiment "negative" the conext consistency is 40 and 
# for sentiment "positive" the context consistency is 43, I would choose the sentiment "positive" becuase it was more consistent than the sentiment "negative".
# If positive consistency equals negative consistency then a float percentage is taken and compared, then sentiment id is assigned accordingly.
# This was done to every context and each context was given a sentiment accordindingly. One key point please make sure your test data is also 
# in the same format as ones we were given. This will allow the program to run without any errors or bugs.
# Using this methodology I obtained the following results
# Efficiency: 69.95708154506438%
# Total Correct Predictions: 164
# Total Incorrect Predictions: 69
# Total Number of Predictions: 233
# Confusion Matrix: 
# Negatives mistaken for positive: 31
# Positives mistaken for negative: 38

# import statements
import sys
import re

# opens file with necessary read and write command
trainf = open(sys.argv[1], "r")
testf = open(sys.argv[2], "r")
modelf = open(sys.argv[3], "w")
# reads the file to a string variable
traintxt = trainf.read()
testtxt = testf.read()
# creates positive and negative sentiment inventories
positive = ""
negative = ""
# removes unnecossaries from the training text file
traintxt = re.sub(r'[.,!?\\:-]', "", traintxt)
# creates an array with just context and other data.
trainarr = re.split(r'context>', traintxt)

# starts going through the array adds context to the individual sentiment inventory
i = 0
while i+1 < len(trainarr):
    # checks which sentiment the context is associated with and adds it to that sentiments particulary inventory
    if "positive" in trainarr[i]:
        temp = re.split('\s+', trainarr[i+1])
        for z in temp:
            if z in positive:
                continue
            else:
                positive = positive + z + " "
    elif "negative" in trainarr[i]:
        temp = re.split('\s+', trainarr[i+1])
        for j in temp:
            if j in negative:
                continue
            else:
                negative = negative + j + " "

    i = i + 2
# cleans up each sentiment inventory for better comparison
positive = re.sub(r'[.,!?\\:-]', "", positive)
negative = re.sub(r'[.,!?\\:-]', "", negative)
# adds the sentiment inventory to model text for future reference if needed
modelf.write("negative sentiment Inventory:\n" + negative)
modelf.write("\n\npositive sentiment Inventory:\n" + positive)
# counter for each sentiment for later comparison
countpos = 0
countneg = 0
# cleans up test text
testtxt = re.sub(r':', "", testtxt)
# now test is ready and is split between context and other data
testarr = re.split(r'context>', testtxt)

# swifts through test array to give each context a sentiment id
i = 0
c = 1
while i+1 < len(testarr):
    testarr[i+1] = re.sub(r'[.,!?\\-]', "", testarr[i+1])
    temp = re.split('\s+', testarr[i+1])
    for n in temp:
        if n in negative:
            countneg = countneg + 1
        if n in positive:
            countpos = countpos + 1
    tempinstance = re.split('\n', testarr[i])
    for m in tempinstance:
        if "id" in m:
            m = m[13:-1]
            # writes to the model text with individual consistencies
            modelf.write("\nContext " + str(c) + ": ")
            modelf.write("\nPositive sentiment Count: " + str(countpos))
            modelf.write("\nNegatice sentiment Count: " + str(countneg))
            # writes the appropriate sentiment for the according context after comparing count of each sentiment consistency
            if(countpos == countneg):
                pcountpos = float(countpos)/float(len(positive))
                pcountneg = float(countneg)/float(len(negative))
                if pcountpos > pcountneg:
                    modelf.write("\nThis sentiment ID is positive")
                    print("<answer instance=" + m + " sentiment=\"positive\"/>")
                else:
                    modelf.write("\nThis sentiment ID is negative")
                    print("<answer instance=" + m + " sentiment=\"negative\"/>")
            elif(countpos > countneg):
                modelf.write("\nThis sentiment ID is positive")
                print("<answer instance=" + m + " sentiment=\"positive\"/>")
            else:
                modelf.write("\nThis sentiment ID is negative")
                print("<answer instance=" + m + " sentiment=\"negative\"/>")
    # resets counters and increments to move to the next position in the array
    countpos = 0
    countneg = 0
    i = i + 2
    c = c + 1

modelf.close()
