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
# lst[i:j];lst[i:];lst[:j]
#
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
# sorted(lst) => returns a newly sorted list
# min(lst)
# max(lst)
# sum(lst)
# lst.index(data)
# str.split('x')    => retuns a new list after splitting str at each occurrence of x
# 'x'.join(lst)     => retuns a new str after joining all elements of lst using x
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

def listsmain():

    print("lists")

    mystring2list()
    print()

    print("lists end")

listsmain()

##Help on class list in module builtins:
##
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