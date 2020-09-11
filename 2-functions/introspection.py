##################################################
# Introspection
##################################################

'''
type
'''
# object types 

# repr(int) returning class type integers
# type is a subclass of object and object's type is type 
# better to use isinstance(i, int) rather than directly call the type


'''
dir
'''
# dir(i) returns list of attribute names and method names for the instance
# getattr(i, 'denominator') returns the same value as i.denominator
# hasattr(i, 'bit_length) i has attribute bit_length


'''
scopes
'''
# introspecting scopes
# globals() represents the global namespace 
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
# can modify globals() too
globals()['a'] = 'val'

# locals() returns similar dictionary as globals() 


'''
inspect module
'''
# import inspect
# import sorted_set
# inspect.getmembers(sorted_set.SortedSet, inspect.isfunction)

# sorted_set.py
from itertools import chain

# another.py
from sorted_set import chain


