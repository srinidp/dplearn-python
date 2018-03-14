#-------------------------------------------------------------------------------
# Name:        regex module1
# Purpose:
#
# Author:      srini_000
#
#   r'xxx'  => r ignores the default esc seq
#   \d      => numbers
#   ()      => create groups within pattern
#   \       => create esc seq in pattern
#   |       => match any of the mutiple patterns
#   ?       => match 0 or 1 occurence patterns
#   *       => match 0 or many occurence patterns
#   +       => match 1 or many occurence patterns
#   {x,y}   => match min x and max y occurence patterns...greedy match(goes for max)
#   {x,y}?  => match min x and max y occurence patterns...non-greedy match(goes for min)
#   {0,y}   => match max y occurence patterns... no min
#   {x,0}   => match min x occurence patterns... no max
#
# Created:     14/03/2018
# Copyright:   (c) srini_000 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re
import os

def mysub1():
    print("sub1")
    myregex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

    for lines in range (len(inputdata)):
        #print(inputdata[lines])
        ## search & group finds first occurance for each input
        match = myregex1.search(str(inputdata[lines]))
        if match != None:
            print("match first", match.group())

        ## searchall finds all occurances for each input
        matchall = myregex1.findall(str(inputdata[lines]))
        for items in range(len(matchall)):
            print("match all", matchall[items])

def mysub2():
    print("sub2")
    myregex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

    for lines in range (len(inputdata)):
        print("input:", inputdata[lines])

        ## finds sub-groups using search
        match = myregex1.search(str(inputdata[lines]))

        ## finds sub-groups using search
        matchall = myregex1.findall(str(inputdata[lines]))

        if match != None:
            print("s.group", match.group())
            print("area code", match.group(1))
            print("phone", match.group(2))

        if matchall != None and len(matchall) != 0:
            print("all:", matchall)

def mysub3():
    print("sub3")
    myregexqu = re.compile(r'0(123)?4')
    myregexas = re.compile(r'0(123)*4')
    myregexpl = re.compile(r'0(123)+4')
    myregexco = re.compile(r'123{1,2}')

    for lines in range (len(inputdata)):
        print("input",inputdata[lines])
        ## finds various pattern matching seq
        match = None
        match = myregexqu.search(str(inputdata[lines]))
        if match != None:
            print("? =>", match.group())
        else:
            print("? =>", None)

        match = None
        match = myregexas.search(str(inputdata[lines]))
        if match != None:
            print("* =>", match.group())
        else:
            print("* =>", None)

        match = None
        match = myregexpl.search(str(inputdata[lines]))
        if match != None:
            print("+ =>", match.group())
        else:
            print("+ =>", None)

        match = None
        match = myregexco.search(str(inputdata[lines]))
        if match != None:
            print("{} =>", match.group())
        else:
            print("{} =>", None)

def regexmain():

    print("regex")
    cwdpath = os.getcwd()
    inputfileloc =  os.path.join(cwdpath,"myregex_input1.txt")

    global inputfile
    inputfile = open(inputfileloc,'r')

    global inputdata
    inputdata = inputfile.readlines()

    mysub1()
    print()
    mysub2()
    print()
    mysub3()
    print()

    inputfile.close()

    print("regex end")


regexmain()

# re object methods
## 'findall',
## 'finditer',
## 'flags',
## 'fullmatch',
## 'groupindex',
## 'groups',
## 'match',
## 'pattern',
## 'scanner',
## 'search',
## 'split',
## 'sub',
## 'subn'