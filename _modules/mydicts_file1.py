#-------------------------------------------------------------------------------
# Name:        dict1
# Purpose:
#
# Author:      srini_000
#
# here...
# dict are varaibles of dictionary datatype...{}
#   => dictionary holds key and value pairs
#   => key is any literal data but unique for a dictionary
#   => value can be any data type including list
#
# emptydict = {} or emptylst = dict()
#
# dict[key] => retuns value for the key
# len(dict)
#
# for keys in dict:
#   => keys loops thro' each key in dict
#
# for values in dict.values():
#   => values loops thro' each value in dict
#
# for keys,values in dict.items():
#   => keys loops thro' each key in dict
#   => values loops thro' each value in dict
#
# methods:
# dict.get(key) => returns the value for key (recommended method to get value)
# dict.update(key,value)  => update/add one or more key-value pairs
# dict.del(key)
# dict.pop(key) => removes and returns value for key
# dict.keys()
# dict.values()
# dict.items()  => returns key-value pairs
#
# sorted(dict);sorted(dict,reverse=True)  => returns a newly sorted dict as per keys
#
# dict comprehension => use {}
#
# Created:     16/03/2018
# Copyright:   (c) srini_000 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def mydictcomprehension():
    print("***mydictcomprehension***")

    names = ['bruce','peter', 'logan']
    heros = ['batman','spiderman', 'wolverine']

    # i want a dict{name, hero} for each name,hero in zip(name,heros)
    # zip(x,y) creates a list of tuple (as pairs) for elements in x and y
    mydict = {name:hero for name,hero in zip(names,heros)}
    print("my dict:", mydict)

    # i want a dict{name, hero} for each name,hero in zip(name,heros)
    # except for peter
    mydict = {name:hero for name,hero in zip(names,heros) if name != 'peter'}
    print("my dict:", mydict)

def dictsmain():

    print("dicts")

    print()
    mydictcomprehension()
    print()

    print("dicts end")

dictsmain()

##class dict(object)
## |  dict() -> new empty dictionary
## |  dict(mapping) -> new dictionary initialized from a mapping object's
## |      (key, value) pairs
## |  dict(iterable) -> new dictionary initialized as if via:
## |      d = {}
## |      for k, v in iterable:
## |          d[k] = v
## |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
## |      in the keyword argument list.  For example:  dict(one=1, two=2)
## |
## |  Methods defined here:
## |
## |  __contains__(self, key, /)
## |      True if D has a key k, else False.
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
## |  __ne__(self, value, /)
## |      Return self!=value.
## |
## |  __new__(*args, **kwargs) from builtins.type
## |      Create and return a new object.  See help(type) for accurate signature.
## |
## |  __repr__(self, /)
## |      Return repr(self).
## |
## |  __setitem__(self, key, value, /)
## |      Set self[key] to value.
## |
## |  __sizeof__(...)
## |      D.__sizeof__() -> size of D in memory, in bytes
## |
## |  clear(...)
## |      D.clear() -> None.  Remove all items from D.
## |
## |  copy(...)
## |      D.copy() -> a shallow copy of D
## |
## |  fromkeys(iterable, value=None, /) from builtins.type
## |      Returns a new dict with keys from iterable and values equal to value.
## |
## |  get(...)
## |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
## |
## |  items(...)
## |      D.items() -> a set-like object providing a view on D's items
## |
## |  keys(...)
## |      D.keys() -> a set-like object providing a view on D's keys
## |
## |  pop(...)
## |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
## |      If key is not found, d is returned if given, otherwise KeyError is raised
## |
## |  popitem(...)
## |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
## |      2-tuple; but raise KeyError if D is empty.
## |
## |  setdefault(...)
## |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
## |
## |  update(...)
## |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
## |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
## |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
## |      In either case, this is followed by: for k in F:  D[k] = F[k]
## |
## |  values(...)
## |      D.values() -> an object providing a view on D's values
## |
## |  ----------------------------------------------------------------------
## |  Data and other attributes defined here:
## |
## |  __hash__ = None