##################################################
# Context Manager
##################################################
# an object designed to be used in a with statement
with context-manager:
    context-manager.begin()
    body
    context-manager.end()

# a context manager ensures that resources are properly and automatically managed

with open('important_data.txt', 'w') as f:
    f.write('The secret password is 12345')

# files are context managers
# file's exit() code closes the file 

# context manager protocol
__enter__(self)

__exit__(self,
        exc_type,
        exc_val,
        exc_tb)

with expression as x: # expression must support __enter__ and __exit__
    body 

# naive implementation of a context manager 
class LoggingContextManager:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return 

# common for __enter__ to return itself
# for example, file.__enter__() returns the file object itself 

# __exit__() called when with statement body exits
__exit__(self, exc_type, exc_val, exc_tb) # exception type, exception object, exception traceback
# propagates exceptions thrown from the with-block

# contextlib
# standard library module for working with context managers
# contextlib.contextmanager is a decorator you can use to create new context managers
# Essentially the contextlib.contextmanager decorator wraps the function in a class that implements the __enter__ and __exit__ methods

# find the yield keyword: everything before it deals with setting up the context, which entails creating
# a backup file, then opening and yielding references to the readable and writable file
# handles that will be returned by the __enter__ call. The __exit__ processing after the
# yield closes the file handles and restores the file from the backup if something went wrong.

@contextlib.contextmanager
def my_context_manager():
    # Enter
    try:
        yield [value] # like __enter__()'s return statement
        # normal exit
    except:
        # exceptional exit from with block
        raise
with my_context_manager() as x:

# exception propagated from inner context mansgers will be seen by outer context managers

# passing multiple context managers
with nest_test('a'), nest_test('b'):
    pass

# example
@contextlib.contextmanager
def start_transaction(connection):
    tx=Transaction(connection)
    
    try:
        yield tx
    except:
        tx.rollback()
        raise
    
    tx.commit()


##################################################
# Introspection
##################################################

# object types 

# repr(int) returning class type integers
# type is a subclass of object and object's type is type 

# instropsecting objects
# dir(i) returns list of attribute names 
# getattr(i, 'denominator')
# hasattr(i, 'bit_length) i has attribute bit_length

# introspecting scopes
# globals() 
# locals() returns same dictionary as globals() 

# inspect module
# import inspect
# import sorted_set
# inspect.getmembers(sorted_set.SortedSet, inspect.isfunction)

