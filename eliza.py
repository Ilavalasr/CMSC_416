# Suraj Ilavala
# CMSC 416
# Coding Assignment Eliza the psychologist
# DUE: 01/30/2020
#
# The problem we are trying to solve is to create a personal psychologist, 
# called Eliza that interacts and responds to the user depending on input. 
# Examples: User says - I am feeling sad
#           Eliza would respond with: Why are u feeling sad?
#           User says - Because my dog died
#           Eliza would respond with: Why did your dog died?
#
# The program starts with assessing how the user asks the question. 
# Depending on how it starts the response varies from "why did you", "Why are you", etc.
# After this step the program will swift through the words and take out any words that might relates to oneself
# Then it adds the rest of the words to one string and uses them to ask another question
# Once you are done you simply type in bye and it ends the program
#
# How to use in terminal write this command
#   python3 eliza.py

import re

#This gets the name of the user and sets the user's name 
print("Eliza: Hi my name is Eliza, I am a Psychologist, what's your name?")
user = input("User: ")
name = re.split('\s+', user)
user = name[-1]

#Asks what eliza can help with
print("Hi " + user + ", how can I help you today?")

#Gets users response
uresponse = input(user+ ": ")

#Sets the keyword to bye so when the user types in Bye it exits
while uresponse != "bye":
    #creates an array of all the words that were used in the sentence
    urep = re.split('\s+', uresponse)
    #Sets the beginning of the questioning depending on how the users starts their sentence
    # Deals with I and I'm
    if re.search(r'[I|i]', urep[0]) is not None:
        urep[0] = ""
        fresp = "Why are you"
    elif re.search(r'[my|My|mY]', urep[0]) is not None:
        urep[0] = ""
        fresp = "Why did your"
    elif re.search(r'[B|b]ecause', urep[0]) is not None:
        urep[0] = ""
        fresp = "Why do you think"
    else:
        fresp = "Why do you"
    #Goes through all the words and removes an words that references users self
    for parts in urep:
        if re.search(r'\b[I|i]\b', parts) is not None:
            parts = re.sub(r'\b[I|i]\b', "", parts)
        elif re.search(r'\b[m|M][y|Y]\b', parts) is not None:
            parts = re.sub(r'\b[m|M][y|Y]\b', "", parts)
        elif re.search(r'\b[a|A][m|M]\b', parts) is not None:
            parts = re.sub(r'\b[a|A][m|M]\b', "", parts)
        else:
            fresp = fresp + " " + parts
    fresp = fresp + "?"
    #prints the response of eliza, a question and askes for input from the user
    print(fresp)
    uresponse = input(user + ": ")
#the user inputed Bye which caused the loop to end and as a results ends the program with a goodbye
print("Goodbye")

