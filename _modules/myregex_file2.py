#-------------------------------------------------------------------------------
# Name:        regex module2
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

def mysub1():
    print("sub1")
    myregex1 = re.compile(r'(\d+\s+\w+)')
    match = myregex1.findall(str(inputdata[0]))
    print(match)

    myregex1 = re.compile(r'[a-z]')
    match = myregex1.findall(str(inputdata[0]))
    print(match)

    myregex1 = re.compile(r'[a-z,A-Z,\d+]')
    match = myregex1.findall(str(inputdata[0]))
    print(match)

def mysub2():
    print("sub2")
    myregex1 = re.compile(r'(a|e|i|o|u)')
    match = myregex1.findall(str(inputdata[0]))
    print(match)

    myregex1 = re.compile(r'[aeiou]')
    match = myregex1.findall(str(inputdata[0]))
    print(match)

    myregex1 = re.compile(r'(a|e|i|o|u)',re.IGNORECASE)
    match = myregex1.findall(str(inputdata[0]))
    print(match)

    myregex1 = re.compile(r'[^aeiou]',re.IGNORECASE)
    match = myregex1.findall(str(inputdata[0]))
    print(match)

def mysub3():
    print("sub3")
    myregex1 = re.compile(r'^hello')
    match = myregex1.findall(str(inputdata[0]))
    print(match)
    myregex1 = re.compile(r'^hello')
    match = myregex1.findall(str(inputdata[1]))
    print(match)
    myregex1 = re.compile(r'world$')
    match = myregex1.findall(str(inputdata[0]))
    print(match)
    myregex1 = re.compile(r'world$')
    match = myregex1.findall(str(inputdata[1]))
    print(match)
    myregex1 = re.compile(r'^\d+$')
    match = myregex1.findall(str(inputdata[2]))
    print(match)
    myregex1 = re.compile(r'(^\d+$)')
    match = myregex1.findall(str(inputdata[3]))
    print(match)

def mysub4():
    print("sub4")
    myregex1 = re.compile(r'.at')
    match = myregex1.findall(str(inputdata[4]))
    print(match)

    myregex1 = re.compile(r'.+?at') #non-greedy
    match = myregex1.findall(str(inputdata[4]))
    print(match)
    myregex1 = re.compile(r'.+at')  #greedy
    match = myregex1.findall(str(inputdata[4]))
    print(match)

    myregex1 = re.compile(r'.{1,2}at')
    match = myregex1.findall(str(inputdata[4]))
    print(match)
    myregex1 = re.compile(r'(.{1,2})at')
    match = myregex1.findall(str(inputdata[4]))
    print(match)

def mysub5():
    print("sub5")
    myregex1 = re.compile(r'first: (.*) last: (.*)')
    match = myregex1.findall(str(inputdata[5]))
    print(match)

    myregex1 = re.compile(r'<<(.*?)>>') #non-greedy
    match = myregex1.findall(str(inputdata[6]))
    print(match)

    myregex1 = re.compile(r'<<(.*)>>') #greedy
    match = myregex1.findall(str(inputdata[6]))
    print(match)

def regexmain():

    print("regex")
    cwdpath = os.getcwd()
    inputfileloc =  os.path.join(cwdpath,"myregex_input2.txt")

    global inputfile
    inputfile = open(inputfileloc,'r')

    global inputdata
    inputdata = []

    inputdata = inputfile.readlines(1)
    print("input:", inputdata)
    mysub1()
    inputdata.clear()
    print()

    inputdata = inputfile.readlines(1)
    print("input:", inputdata)
    mysub2()
    inputdata.clear()
    print()

    inputdata = inputfile.readlines()
    print("input:", inputdata)
    mysub3()
    print()
    mysub4()
    print()
    mysub5()
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