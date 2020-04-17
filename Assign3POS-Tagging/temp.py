import re

sentence = "Ingrid 	are testing regular expressions."
print(re.split('\s+', sentence))

tokens = re.split('\s+', sentence)
t = "expressions.\b"
if (t) in sentence:
    print ("yay")
