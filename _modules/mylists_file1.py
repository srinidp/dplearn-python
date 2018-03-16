#-------------------------------------------------------------------------------
# Name:        lists1
# Purpose:
#
# Author:      srini_000
#
# here...
# lst,lst1 are varaibles of list datatype...[]
# data is a literal or data
# index,i,j are indexes
# str is a string variable
# 'x' is a string literal
#
# len(lst)
# lst[index]
# lst[-index]   => -1 is last item
# lst[i:j];lst[i:];lst[:j]  => j is excluded
# lst[start:end:step]   => end is excluded
# emptylst = []  or emptylst = list()
#
# data in lst
#   => "in" is an operator
#   => returns True if data is an element of lst
#
# for data in lst
#   => data loops thro' each content of lst elements
#
# for i,data in enumerate (lst)
#   => "in enumerate" is an operator
#   => i loops thro' each index of lst elements
#   => data loops thro' each content of lst elements
#
# methods:
# lst.append(data)
# lst.insert(i,data)
# lst.extend(lst1)  => combines 2 list data
# lst.remove(data)
# lst.pop() => removes and returns last element
# lst.reverse
# lst.sort();lst.sort(reverse=True)
# lst.index(data)
#
# sorted(lst);sorted(lst,reverse=True)  => returns a newly sorted list
# sorted(lst,key=abs)   => returns a newly sorted list as per abs value
# min(lst)
# max(lst)
# sum(lst)
# str.split('x')    => retuns a new list after splitting str at each occurrence of x
# 'x'.join(lst)     => retuns a new str after joining all elements of lst using x
#
# list comprehension => use []
#
# Created:     16/03/2018
# Copyright:   (c) srini_000 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def mystring2list():
    print("***mystring2list***")
    mystr = "Lion,Tiger,Elephant,Rhino"
    mylst = mystr.split(',')
    print(mystr)
    print(mylst)

def mylistslice():
    print("***mylistslice***")

    mylst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #index   0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    #-index-10,-9,-8,-7,-6,-5,-4,-3,-2,-1

    print("     3  -  8:", mylst[3:9])
    print("     3 - end:", mylst[3:])
    print("     odd nos:", mylst[1::2])
    print("     rev nos:", mylst[::-1])
    print(" rev odd nos:", mylst[-1:-10:-2])

def mylistcomprehension():
    print("***mylistcomprehension***")
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # i want n for each n in nums
    mylst = [n for n in nums]
    print("my list:", mylst)

    # i want n*n for each n in nums
    mylst = [n*n for n in nums]
    print("my list:", mylst)

    # i want n for each n in nums if n is even
    mylst = [n for n in nums if n%2==0]
    print("my list:", mylst)

    # i want a (letter,num)pair n for each letter in 'abcd'
    # and each number in '0123' => list of tuples
    letters = ['a','b','c','d']
    nums = [0, 1, 2, 3]
    mylst = [(letter,num) for letter in letters for num in nums]
    print("my list:", mylst)

def listsmain():

    print("lists")

    mystring2list()
    print()
    mylistslice()
    print()
    mylistcomprehension()
    print()

    print("lists end")

listsmain()

##class list(object)
## |  list() -> new empty list
## |  list(iterable) -> new list initialized from iterable's items
## |
## |  Methods defined here:
## |
## |  __add__(self, value, /)
## |      Return self+value.
## |
## |  __contains__(self, key, /)
## |      Return key in self.
## |
## |  __delitem__(self, key, /)
## |      Delete self[key].
## |
## |  __eq__(self, value, /)
## |      Return self==value.
## |
## |  __ge__(self, value, /)
## |      Return self>=value.
## |
## |  __getattribute__(self, name, /)
## |      Return getattr(self, name).
## |
## |  __getitem__(...)
## |      x.__getitem__(y) <==> x[y]
## |
## |  __gt__(self, value, /)
## |      Return self>value.
## |
## |  __iadd__(self, value, /)
## |      Implement self+=value.
## |
## |  __imul__(self, value, /)
## |      Implement self*=value.
## |
## |  __init__(self, /, *args, **kwargs)
## |      Initialize self.  See help(type(self)) for accurate signature.
## |
## |  __iter__(self, /)
## |      Implement iter(self).
## |
## |  __le__(self, value, /)
## |      Return self<=value.
## |
## |  __len__(self, /)
## |      Return len(self).
## |
## |  __lt__(self, value, /)
## |      Return self<value.
## |
## |  __mul__(self, value, /)
## |      Return self*value.n
## |
## |  __ne__(self, value, /)
## |      Return self!=value.
## |
## |  __new__(*args, **kwargs) from builtins.type
## |      Create and return a new object.  See help(type) for accurate signature.
## |
## |  __repr__(self, /)
## |      Return repr(self).
## |
## |  __reversed__(...)
## |      L.__reversed__() -- return a reverse iterator over the list
## |
## |  __rmul__(self, value, /)
## |      Return self*value.
## |
## |  __setitem__(self, key, value, /)
## |      Set self[key] to value.
## |
## |  __sizeof__(...)
## |      L.__sizeof__() -- size of L in memory, in bytes
## |
## |  append(...)
## |      L.append(object) -> None -- append object to end
## |
## |  clear(...)
## |      L.clear() -> None -- remove all items from L
## |
## |  copy(...)
## |      L.copy() -> list -- a shallow copy of L
## |
## |  count(...)
## |      L.count(value) -> integer -- return number of occurrences of value
## |
## |  extend(...)
## |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
## |
## |  index(...)
## |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
## |      Raises ValueError if the value is not present.
## |
## |  insert(...)
## |      L.insert(index, object) -- insert object before index
## |
## |  pop(...)
## |      L.pop([index]) -> item -- remove and return item at index (default last).
## |      Raises IndexError if list is empty or index is out of range.
## |
## |  remove(...)
## |      L.remove(value) -> None -- remove first occurrence of value.
## |      Raises ValueError if the value is not present.
## |
## |  reverse(...)
## |      L.reverse() -- reverse *IN PLACE*
## |
## |  sort(...)
## |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
## |
## |  ----------------------------------------------------------------------
## |  Data and other attributes defined here:
## |
## |  __hash__ = None