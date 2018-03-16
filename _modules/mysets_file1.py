#-------------------------------------------------------------------------------
# Name:        set1
# Purpose:
#
# Author:      srini_000
#
# here...
# set1, set2 are variables of set datatype...{}
#   => set is same as a list except it can hold only unique values
#   => the order of data in a set can vary during each access or read
#   => <un-ordered and no-duplicates>
#
# emptyset = set()
#
# methods:
# set1.union(set2)
# set1.intersection(set2)
# set1.difference(set2)
#
# set comprehension => use {}
#
# Created:     16/03/2018
# Copyright:   (c) srini_000 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def unorderedset():
    print("***unorderedset***")
    myset1 = {"mercury","mars","earth","jupiter"}

    print("order1:",myset1)
    myset1.add("neptune")
    print("order2:",myset1)
    myset1.add("uranus")
    print("order3:",myset1)

def nodupset():
    print("***nodupset***")
    myset1 = {"mercury","mars","earth","jupiter"}

    print("set after add{} is {}".format(0,myset1))

    myset1.add("venus")
    print("set after add{} is {}".format(1,myset1))

    myset1.add("venus")
    print("set after add{} is {}".format(2,myset1))

def mysetfun():
    print("***mysetfunctions***")
    myset1 = {"mercury","mars","earth","jupiter"}
    myset2 = {"earth","moon","sun"}

    print("union:", myset1.union(myset2))
    print("intersection:", myset1.intersection(myset2))
    print("difference:", myset1.difference(myset2))

def mysetcomprehension():
    print("***mysetcomprehension***")

    nums = [1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]

    # i want n for each n in nums but with no dups
    myset = {n for n in nums}
    print("my set:", myset)

def setsmain():

    print("sets")
    unorderedset()
    print()

    nodupset()
    print()

    mysetfun()
    print()

    mysetcomprehension()
    print()

    print("sets end")

setsmain()

##class set(object)
## |  set() -> new empty set object
## |  set(iterable) -> new set object
## |
## |  Build an unordered collection of unique elements.
## |
## |  Methods defined here:
## |
## |  __and__(self, value, /)
## |      Return self&value.
## |
## |  __contains__(...)
## |      x.__contains__(y) <==> y in x.
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
## |  __gt__(self, value, /)
## |      Return self>value.
## |
## |  __iand__(self, value, /)
## |      Return self&=value.
## |
## |  __init__(self, /, *args, **kwargs)
## |      Initialize self.  See help(type(self)) for accurate signature.
## |
## |  __ior__(self, value, /)
## |      Return self|=value.
## |
## |  __isub__(self, value, /)
## |      Return self-=value.
## |
## |  __iter__(self, /)
## |      Implement iter(self).
## |
## |  __ixor__(self, value, /)
## |      Return self^=value.
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
## |  __ne__(self, value, /)
## |      Return self!=value.
## |
## |  __new__(*args, **kwargs) from builtins.type
## |      Create and return a new object.  See help(type) for accurate signature.
## |
## |  __or__(self, value, /)
## |      Return self|value.
## |
## |  __rand__(self, value, /)
## |      Return value&self.
## |
## |  __reduce__(...)
## |      Return state information for pickling.
## |
## |  __repr__(self, /)
## |      Return repr(self).
## |
## |  __ror__(self, value, /)
## |      Return value|self.
## |
## |  __rsub__(self, value, /)
## |      Return value-self.
## |
## |  __rxor__(self, value, /)
## |      Return value^self.
## |
## |  __sizeof__(...)
## |      S.__sizeof__() -> size of S in memory, in bytes
## |
## |  __sub__(self, value, /)
## |      Return self-value.
## |
## |  __xor__(self, value, /)
## |      Return self^value.
## |
## |  add(...)
## |      Add an element to a set.
## |
## |      This has no effect if the element is already present.
## |
## |  clear(...)
## |      Remove all elements from this set.
## |
## |  copy(...)
## |      Return a shallow copy of a set.
## |
## |  difference(...)
## |      Return the difference of two or more sets as a new set.
## |
## |      (i.e. all elements that are in this set but not the others.)
## |
## |  difference_update(...)
## |      Remove all elements of another set from this set.
## |
## |  discard(...)
## |      Remove an element from a set if it is a member.
## |
## |      If the element is not a member, do nothing.
## |
## |  intersection(...)
## |      Return the intersection of two sets as a new set.
## |
## |      (i.e. all elements that are in both sets.)
## |
## |  intersection_update(...)
## |      Update a set with the intersection of itself and another.
## |
## |  isdisjoint(...)
## |      Return True if two sets have a null intersection.
## |
## |  issubset(...)
## |      Report whether another set contains this set.
## |
## |  issuperset(...)
## |      Report whether this set contains another set.
## |
## |  pop(...)
## |      Remove and return an arbitrary set element.
## |      Raises KeyError if the set is empty.
## |
## |  remove(...)
## |      Remove an element from a set; it must be a member.
## |
## |      If the element is not a member, raise a KeyError.
## |
## |  symmetric_difference(...)
## |      Return the symmetric difference of two sets as a new set.
## |
## |      (i.e. all elements that are in exactly one of the sets.)
## |
## |  symmetric_difference_update(...)
## |      Update a set with the symmetric difference of itself and another.
## |
## |  union(...)
## |      Return the union of sets as a new set.
## |
## |      (i.e. all elements that are in either set.)
## |
## |  update(...)
## |      Update a set with the union of itself and others.
## |
## |  ----------------------------------------------------------------------
## |  Data and other attributes defined here:
## |
## |  __hash__ = None