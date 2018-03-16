#-------------------------------------------------------------------------------
# Name:        generator expressions 1
# Purpose:
#
# Author:      srini_000
#
# genex comprehension => use ()
#
# Created:     16/03/2018
# Copyright:   (c) srini_000 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def mysquaregen(nums):
    for num in nums:
        yield num*num

def mygenexp():
    print("***mygenexp***")
    data = [1, 2, 3]
    mygen = mysquaregen(data)

    recommended_method = 0

    if recommended_method == 1:
        for items in mygen:
            print(items)
    else:
        try:
            print (next(mygen))
            print (next(mygen))
            print (next(mygen))
            print (next(mygen))
        except:
            print("limit reached")


def mygenexcomprehension():
    print("***mygenexcomprehension***")
    nums = [1, 2, 3, 4, 5]
    # i want to yield n*n for each n in nums
    mygen = (n*n for n in nums)

    recommended_method = 0

    if recommended_method == 1:
        for items in mygen:
            print(items)
    else:
        try:
            print (next(mygen))
            print (next(mygen))
            print (next(mygen))
            print (next(mygen))
            print (next(mygen))
            print (next(mygen))
        except:
            print("limit reached")


def genexpmain():

    print("generator exp")

    print()
    mygenexp()
    print()
    mygenexcomprehension()
    print()

    print("generator exp end")

genexpmain()

##class generator(object)
## |  Methods defined here:
## |
## |  __del__(...)
## |
## |  __getattribute__(self, name, /)
## |      Return getattr(self, name).
## |
## |  __iter__(self, /)
## |      Implement iter(self).
## |
## |  __next__(self, /)
## |      Implement next(self).
## |
## |  __repr__(self, /)
## |      Return repr(self).
## |
## |  close(...)
## |      close() -> raise GeneratorExit inside generator.
## |
## |  send(...)
## |      send(arg) -> send 'arg' into generator,
## |      return next yielded value or raise StopIteration.
## |
## |  throw(...)
## |      throw(typ[,val[,tb]]) -> raise exception in generator,
## |      return next yielded value or raise StopIteration.
## |
## |  ----------------------------------------------------------------------
## |  Data descriptors defined here:
## |
## |  gi_code
## |
## |  gi_frame
## |
## |  gi_running