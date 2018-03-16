#-------------------------------------------------------------------------------
# Name:        regex module1
# Purpose:
#
# Author:      srini_000
#
# quantifier: ?*+.{}
# ?     - 0 or 1 character
# *     - 0 or many characters
# +     - 1 or many characters
# .     - any character except newline (\n)
# {x}   - exact number of x occurrences
# {x,y} - range of occurrences with x as min and y as max
#
# character set: []
# [] - one or more character(s) or literals
#    - either or logic (no need of | symbol)
#    - no escape sequence (no need of \ symbol)
# [^]- negates []
# () - group one or more character(s) or literals
# |  - either or logic
#
# anchors: ^$\b\B
# ^  - starts with character(s) at the beginning of line
# $  - ends with character(s) at the end of line
# \b - word boundary
# \B - not a word boundary
#
# patterns: \d\D\w\W\s\S
# \d - digit character (0-9)
# \D - not a digit character
# \w - word character (a-z, A-Z, 0-9, _)
# \W - not a word character
# \s - whitespace character (space, tab, newline)
# \S - not a whitespace character
# \  - escape sequence character
#
# meta characters to be escaped:
# ?*+.^$|{}()\
#
# methods:
#   'findall'   - returns all matches in list/tuple
#   'finditer'  - returns all match objects
#   'search'    - returns first match object
#
# Created:     14/03/2018
# Copyright:   (c) srini_000 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re
import os

def mysubfinditer():
    print("***finditer-all match objects***")
    print("input:", inputdata)

    myregex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    matchobj = myregex1.finditer(str(inputdata))

    for items in matchobj:
        print(items)
        print(items.group())

def mysubsearch():
    print("***search-first match object***")
    print("input:", inputdata)

    myregex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    matchobj = myregex1.search(str(inputdata))

    print(matchobj)
    print(matchobj.group())

def mysubfindall():
    print("***findall-all matches as list/tuple***")
    print("input:", inputdata)

    myregex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    matchlist = myregex1.findall(str(inputdata))

    for items in range(len(matchlist)):
        print(matchlist[items])

def mysubgroup():
    print("input:", inputdata)
    myregex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

    print("***finditer-group***")
    matchobj = myregex1.finditer(str(inputdata))

    for items in matchobj:
        print("area code:", items.group(1))
        print("phone  no:", items.group(2))

    print("***search-group***")
    matchobj = myregex1.search(str(inputdata))

    print("area code:", matchobj.group(1))
    print("phone  no:", matchobj.group(2))

    print("***findall-group***")
    matchlist = myregex1.findall(str(inputdata))

    for items in range(len(matchlist)):
        print(matchlist[items])
        print("area code:", matchlist[items][0])
        print("phone  no:", matchlist[items][1])

def mysubregex():
    print("***mysubregex***")
    myregexqu = re.compile(r'0(123)?4')
    myregexas = re.compile(r'0(123)*4')
    myregexpl = re.compile(r'0(123)+4')
    myregexco = re.compile(r'123{1,2}')

    for lines in range (len(inputdata)):
        print()
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
    inputdata = inputfile.readlines(1)

    mysubfinditer()
    mysubsearch()
    mysubfindall()
    print()
    mysubgroup()
    print()
    inputdata.clear()

    inputdata = inputfile.readlines()
    mysubregex()
    print()
    inputdata.clear()

    inputfile.close()

    print("regex end")


regexmain()

##class SRE_Pattern(builtins.object)
## |  Compiled regular expression objects
## |
## |  Methods defined here:
## |
## |  __copy__(...)
## |
## |  __deepcopy__(...)
## |
## |  __repr__(self, /)
## |      Return repr(self).
## |
## |  findall(...)
## |      findall(string[, pos[, endpos]]) -> list.
## |      Return a list of all non-overlapping matches of pattern in string.
## |
## |  finditer(...)
## |      finditer(string[, pos[, endpos]]) -> iterator.
## |      Return an iterator over all non-overlapping matches for the
## |      RE pattern in string. For each match, the iterator returns a
## |      match object.
## |
## |  fullmatch(...)
## |      fullmatch(string[, pos[, endpos]]) -> match object or None.
## |      Matches against all of the string
## |
## |  match(...)
## |      match(string[, pos[, endpos]]) -> match object or None.
## |      Matches zero or more characters at the beginning of the string
## |
## |  scanner(...)
## |
## |  search(...)
## |      search(string[, pos[, endpos]]) -> match object or None.
## |      Scan through string looking for a match, and return a corresponding
## |      match object instance. Return None if no position in the string matches.
## |
## |  split(...)
## |      split(string[, maxsplit = 0])  -> list.
## |      Split string by the occurrences of pattern.
## |
## |  sub(...)
## |      sub(repl, string[, count = 0]) -> newstring.
## |      Return the string obtained by replacing the leftmost non-overlapping
## |      occurrences of pattern in string by the replacement repl.
## |
## |  subn(...)
## |      subn(repl, string[, count = 0]) -> (newstring, number of subs)
## |      Return the tuple (new_string, number_of_subs_made) found by replacing
## |      the leftmost non-overlapping occurrences of pattern with the
## |      replacement repl.
## |
## |  ----------------------------------------------------------------------
## |  Data descriptors defined here:
## |
## |  flags
## |
## |  groupindex
## |
## |  groups
## |
## |  pattern
