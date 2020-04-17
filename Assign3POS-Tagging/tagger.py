# Suraj Ilavala
# March 3, 2020
# CMSC 416: POS Tagging
# Assignment 3: tagger.py
# 
# The problem solved here is tagging words with penn tree bank pos tagset. Each individual word is stored with 
# the according pos tag. After each tag is stored it is then used to analyze the text in the test document. 
# After running through the test document with the tagger the list of all the words and its tags are printed 
# to a document. 
# Example: to completely measure the efficiency of the tagger you have to print it to a file like so
#           --> python tagger.py pos-train.txt pos-test.txt > pos-test-with-tags.txt
#
#   make sure to have the training file first and the the test file
#   the pos-train.txt is used to train the tagger created so that we can analyze other text, such as pos-test.txt
# This specific algorithim used is a search for specific pos tagger in the training, then stored into the specific
# tagger to be called and used again later to analyze other texts.
# 
# #


import sys
import re
# tag method that asks for train file and test file
def tag(trainf, testf):
    #storage variables that will store the specific word that holds the specified pos tag.
    cc = " "
    cd = " "
    dt = " "
    ex = " "
    fw = " "
    intag = " "
    jj = " "
    jjr = " "
    jjs = " "
    ls = " "
    md = " "
    nn = " "
    nns = " "
    nnp = " "
    nnps = " "
    pdt = " "
    pos = " "
    prp = " "
    ppcash = " "
    rb = " "
    rbr = " "
    rbs = " "
    rp = " "
    sym = " "
    totag = " "
    uh = " "
    vb = " "
    vbd = " "
    vbg = " "
    vbn = " "
    vbp = " "
    vbz = " "
    wdt = " "
    wp = " "
    wpcash = " "
    wrb = " "
    hashtag = " "
    cash = " "
    dot = " "
    comma = " "
    colon = " "
    lp = " "
    rpar = " "
    dquote = " "
    squote = " "
    #reads and stores the file
    trainfile = open(trainf, "r")
    testfile = open(testf, "r")

    traintxt = trainfile.read()
    testtxt = testfile.read()
    #removes brackets and then makes arrays with every word along with its tag
    readytrain = re.sub(r'\[|\]', "", traintxt)
    readytest = re.sub(r'\[|\]', "", testtxt)
    trainarr = re.split('\s+', readytrain)
    testarr = re.split('\s+', readytest)
    #starts storing words into the storage variable
    for i in trainarr:
        if "CC" in i:
            cc = cc + i + " "
        elif "CD" in i:
            cd = cd + i + " "
        elif "DT" in i:
            dt = dt + i + " "
        elif "EX" in i:
            ex = ex + i + " "
        elif "FW" in i:
            fw = fw + i + " "
        elif "IN" in i:
            intag = intag + i + " "
        elif "JJR" in i:
            jjr = jjr + i + " "
        elif "JJS" in i:
            jjs = jjs + i + " "
        elif "JJ" in i:
            jj = jj + i + " "
        elif "LS" in i:
            ls = ls + i + " "
        elif "MD" in i:
            md = md + i + " "
        elif "NNS" in i:
            nns = nns + i + " "
        elif "NNPS" in i:
            nnps = nnps + i + " "
        elif "NNP" in i:
            nnp = nnp + i + " "
        elif "NN" in i:
            nn = nn + i + " "
        elif "PDT" in i:
            pdt = pdt + i + " "
        elif "POS" in i:
            pos = pos + i + " "
        elif "PRP" in i:
            prp = prp + i + " "
        elif "PP$" in i:
            ppcash = ppcash + i + " "
        elif "RBR" in i:
            rbr = rbr + i + " "
        elif "RBS" in i:
            rbs = rbs + i + " "
        elif "RB" in i:
            rb = rb + i + " "
        elif "RP" in i:
            rp = rp + i + " "
        elif "SYM" in i:
            sym = sym + i + " "
        elif "TO" in i:
            totag = totag + i + " "
        elif "UH" in i:
            uh = uh + i + " "
        elif "VBD" in i:
            vbd = vbd + i  + " "
        elif "VBG" in i:
            vbg = vbg + i  + " "
        elif "VBN" in i:
            vbn = vbn + i + " "
        elif "VBP" in i: 
            vbp = vbp + i + " "
        elif "VBZ" in i:
            vbz= vbz + i + " "
        elif "VB" in i:
            vb = vb + i  + " "
        elif "WDT" in i:
            wdt = wdt + i + " "
        elif "WP$" in i:
            wpcash = wpcash + i + " "
        elif "WP" in i:
            wp = wp + i + " "
        elif "WRB" in i:
            wrb = wrb + i + " "
        elif "#" in i:
            hashtag = hashtag + i + " "
        elif "$" in i:
            cash = cash + i + " "
        elif "." in i:
            dot = dot + i + " "
        elif "," in i:
            comma = comma + i + " "
        elif ":" in i:
            colon = colon + i + " "
        elif "(" in i:
            lp = lp + i + " "
        elif ")" in i:
            rpar = rpar + i + " "
        elif "\"" in i:
            dquote = dquote + i + " "
        elif "'" in i:
            squote = squote + i + " "
        else:
            nn = nn + i + " "
    #assigns tags to the test array obtained from the test files
    z = 0
    while z < len(testarr):
        temp = " " + testarr[z] + "/"
        if temp in cc:
            testarr[z] = testarr[z] + "/CC"
            z = z + 1
        elif temp in cd:
            testarr[z] = testarr[z] + "/CD"
            z = z + 1
        elif temp in dt:
            testarr[z] = testarr[z] + "/DT"
            z = z + 1
        elif temp in ex:
            testarr[z] = testarr[z] + "/EX"
            z = z + 1
        elif temp in fw:
            testarr[z] = testarr[z] + "/FW"
            z = z + 1
        elif temp in intag:
            testarr[z] = testarr[z] + "/IN"
            z = z + 1
        elif temp in jj:
            testarr[z] = testarr[z] + "/JJ"
            z = z + 1
        elif temp in jjr:
            testarr[z] = testarr[z] + "/JJR"
            z = z + 1
        elif temp in jjs:
            testarr[z] = testarr[z] + "/JJS"
            z = z + 1
        elif temp in ls:
            testarr[z] = testarr[z] + "/LS"
            z = z + 1
        elif temp in md:
            testarr[z] = testarr[z] + "/MD"
            z = z + 1
        elif temp in nn:
            testarr[z] = testarr[z] + "/NN"
            z = z + 1
        elif temp in nns:
            testarr[z] = testarr[z] + "/NNS"
            z = z + 1
        elif temp in nnp:
            testarr[z] = testarr[z] + "/NNP"
            z = z + 1
        elif temp in nnps:
            testarr[z] = testarr[z] + "/NNPS"
            z = z + 1
        elif temp in pdt:
            testarr[z] = testarr[z] + "/PDT"
            z = z + 1
        elif temp in pos:
            testarr[z] = testarr[z] + "/POS"
            z = z + 1
        elif temp in prp:
            testarr[z] = testarr[z] + "/PRP"
            z = z + 1
        elif temp in ppcash:
            testarr[z] = testarr[z] + "/PP$"
            z = z + 1
        elif temp in rb:
            testarr[z] = testarr[z] + "/RB"
            z = z + 1
        elif temp in rbr:
            testarr[z] = testarr[z] + "/RBR"
            z = z + 1
        elif temp in rbs:
            testarr[z] = testarr[z] + "/RBS"
            z = z + 1
        elif temp in rp:
            testarr[z] = testarr[z] + "/RP"
            z = z + 1
        elif temp in sym:
            testarr[z] = testarr[z] + "/SYM"
            z = z + 1
        elif temp in totag:
            testarr[z] = testarr[z] + "/TO"
            z = z + 1
        elif temp in uh:
            testarr[z] = testarr[z] + "/UH"
            z = z + 1
        elif temp in vb:
            testarr[z] = testarr[z] + "/VB"
            z = z + 1
        elif temp in vbd:
            testarr[z] = testarr[z] + "/VBD"
            z = z + 1
        elif temp in vbg:
            testarr[z] = testarr[z] + "/VBG"
            z = z + 1
        elif temp in vbn:
            testarr[z] = testarr[z] + "/VBN"
            z = z + 1
        elif temp in vbp:
            testarr[z] = testarr[z] + "/VBP"
            z = z + 1
        elif temp in vbz:
            testarr[z] = testarr[z] + "/VBZ"
            z = z + 1
        elif temp in wdt:
            testarr[z] = testarr[z] + "/WDT"
            z = z + 1
        elif temp in wp:
            testarr[z] = testarr[z] + "/WP"
            z = z + 1
        elif temp in wpcash:
            testarr[z] = testarr[z] + "/WP$"
            z = z + 1
        elif temp in wrb:
            testarr[z] = testarr[z] + "/WRB"
            z = z + 1
        elif temp in hashtag:
            testarr[z] = testarr[z] + "/#"
            z = z + 1
        elif temp in cash:
            testarr[z] = testarr[z] + "/$"
            z = z + 1
        elif temp in dot:
            testarr[z] = testarr[z] + "/."
            z = z + 1
        elif temp in comma:
            testarr[z] = testarr[z] + "/,"
            z = z + 1
        elif temp in colon:
            testarr[z] = testarr[z] + "/:"
            z = z + 1
        elif temp in lp:
            testarr[z] = testarr[z] + "/("
            z = z + 1
        elif temp in rpar:
            testarr[z] = testarr[z] + "/)"
            z = z + 1
        elif temp in dquote:
            testarr[z] = testarr[z] + "/\"\""
            z = z + 1
        elif temp in squote:
            testarr[z] = testarr[z] + "/''"
            z = z + 1
        else:
            testarr[z] = testarr[z] + "/NN"
            z = z + 1
    #returns the test array with tags added
    return testarr
#calls the function
taggedtest = tag(sys.argv[1], sys.argv[2])
i = 0
#prints the variables
while i < len(taggedtest):
    print(taggedtest[i] + " ")
    i = i + 1
