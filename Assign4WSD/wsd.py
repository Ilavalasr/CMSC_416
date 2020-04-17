# Suraj Ilavala
# March 31st, 2020
# CMSC 416: PA4-WSD
# wsd.py
# This program uses a wsd algorithim to predict context sense. After training given senses, in this case the training will recording the
# type of wording used in that specific sense and assigning it to the sense. After the training it the conext of the practice text will 
# be compared to the created inventory. Depending on which sense the context relates to more accurately, that senseid will be assigned to 
# the context. 
# Example input command is as follows, this is also how to run the program: 
#       python3 wsd.py line-train.txt line-test.txt my-model.txt > my-line-answers.txt
#   the line-train.txt is the txt used to create the sense inventory and line-test.txt is where the practice context is located to assign
#   the senseid after comparing the context to the sense inventory. The my-model.txt is model is document that shows the sense inventory
#   created. Any stdout will be printed to my-line-answers.txt which will then be used in the scorer.py. Make sure all these files are
#   in the same location/folder
# Actual train input from a text will look like this:
#           <instance id="line-n.w9_10:6830:">
#           <answer instance="line-n.w9_10:6830:" senseid="phone"/>
#           <context>
#               <s> The New York plan froze basic rates, offered no protection to Nynex against an economic downturn that sharply cut demand and didn't offer flexible pricing. 
#               </s> <@> <s> In contrast, the California economy is booming, with 4.5% access <head>line</head> growth in the past year. </s> 
#           </context>
#           </instance>
# Actual test input from a text will look like this:
#           <instance id="line-n.w8_059:8174:">
#           <context>
#               <s> Advanced Micro Devices Inc., Sunnyvale, Calif., and Siemens AG of West Germany said they agreed to jointly develop, manufacture and market microchips for data 
#               communications and telecommunications with an emphasis on the integrated services digital network. </s> <@> </p> <@> <p> <@> <s> The integrated services digital network, 
#               or ISDN, is an international standard used to transmit voice, data, graphics and video images over telephone <head>lines</head> . </s> 
#           </context>
#           </instance>
#   Please take note of the key difference between test and train text. The train text contains a "answer instance" while test does not.
# Here is a example of output:
#           <answer instance="line-n.art7} aphb 29604729:" senseid="phone"/>
#   This will will be compared to the key to test the efficiency of the program
# The model used to solve this uses Naive bayes. For this algorithim, I first created sense inventories with the train text to identify what 
# was common in one particular sense. After the sense invetories were made I took the individual words of the context in test and tested to 
# see if that word is consistent with that sense. If it was a counter was added. After checking the words in both sense inventories I would 
# choose the sense which the context is more consistent with. For example, lets say for sense "product" the conext consistency is 40 and 
# for sense "price" the context consistency is 43, I would choose the sense "price" becuase it was more consistent than the sense "product".
# If price consistency equals product consistency then a float percentage is taken and compared, then sense id is assigned accordingly.
# This was done to every context and each context was given a sense accordindingly. One key point please make sure your test data is also 
# in the same format as ones we were given. This will the program to run without any errors or bugs.
# Using this methodology I obtained a 90.55% efficiency. There were 115 correct predictions out of 127 cases. 
# This means there are 12 incorrect predictions. For more details confusion matric, each individual consistency written to the my-model.txt 
# for further analysis. It will each sense consistency for each context.
# 90.55118110236221% Efficiency
# 115 Correct Predictions
# 12 Incorrect Predictions
# 127 Test Cases#

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
# creates phone and product sense inventories
phone = ""
product = ""
# removes unnecossaries from the training text file
traintxt = re.sub(r'(<|<\/)s>', "", traintxt)
traintxt = re.sub(r'<@>', "", traintxt)
traintxt = re.sub(r'(<|<\/)p>', "", traintxt)
traintxt = re.sub(r'(<|<\/)head>', "", traintxt)
# creates an array with just context and other data.
trainarr = re.split(r'context>', traintxt)

# starts going through the array adds context to the individual sense inventory
i = 0
while i+1 < len(trainarr):
    # checks which sense the context is associated with and adds it to that senses particulary inventory
    if "phone" in trainarr[i]:
        temp = re.split('\s+', trainarr[i+1])
        for z in temp:
            if z in phone:
                continue
            else:
                phone = phone + z + " "
    elif "product" in trainarr[i]:
        temp = re.split('\s+', trainarr[i+1])
        for j in temp:
            if j in product:
                continue
            else:
                product = product + j + " "

    i = i + 2
# cleans up each sense inventory for better comparison
phone = re.sub(r'[.,!?\\-]', "", phone)
product = re.sub(r'[.,!?\\-]', "", product)
# adds the sense inventory to model text for future reference if needed
modelf.write("Product Sense Inventory:\n" + product)
modelf.write("\n\nPhone Sense Inventory:\n" + phone)
# counter for each sense for later comparison
countpho = 0
countpro = 0
# cleans up test text
testtxt = re.sub(r'(<|</)s>', "", testtxt)
testtxt = re.sub(r'<@>', "", testtxt)
testtxt = re.sub(r'(<|</)p>', "", testtxt)
testtxt = re.sub(r'(<|</)head>', "", testtxt)
# now test is ready and is split between context and other data
testarr = re.split(r'context>', testtxt)

# swifts through test array to give each context a sense id
i = 0
c = 1
while i+1 < len(testarr):
    testarr[i+1] = re.sub(r'[.,!?\\-]', "", testarr[i+1])
    temp = re.split('\s+', testarr[i+1])
    for n in temp:
        if n in product:
            countpro = countpro + 1
        if n in phone:
            countpho = countpho + 1
    tempinstance = re.split('\n', testarr[i])
    for m in tempinstance:
        if "id" in m:
            m = m[13:-1]
            # writes to the model text with individual consistencies
            modelf.write("\nContext " + str(c) + ": ")
            modelf.write("\nPhone Sense Count: " + str(countpho))
            modelf.write("\nPhone Sense Count: " + str(countpro))
            # writes the appropriate sense id for the according context after comparing count of each sense consistency
            if(countpho == countpro):
                pcountpho = float(countpho)/float(len(phone))
                pcountpro = float(countpro)/float(len(product))
                if pcountpho > pcountpro:
                    modelf.write("\nThis Sense ID is Phone")
                    print("<answer instance=" + m + " senseid=\"phone\"/>")
                else:
                    modelf.write("\nThis Sense ID is Product")
                    print("<answer instance=" + m + " senseid=\"product\"/>")
            elif(countpho > countpro):
                modelf.write("\nThis Sense ID is Phone")
                print("<answer instance=" + m + " senseid=\"phone\"/>")
            else:
                modelf.write("\nThis Sense ID is Product")
                print("<answer instance=" + m + " senseid=\"product\"/>")
    # resets counters and increments to move to the next position in the array
    countpho = 0
    countpro = 0
    i = i + 2
    c = c + 1

modelf.close()



