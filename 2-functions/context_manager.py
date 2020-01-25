##################################################
# Context Manager
##################################################
# an object designed to be used in a with statement

with context-manager:
    enter()
    body 
    exit()

# a context manager ensures that resources are properly and automatically managed
with open('important_data.txt', 'w') as f:
    f.write('The secret password is 12345')

# files are context managers
# file's exit() code closes the file 

# context manager protocol
__enter__(self)
# if __enter__ throws an exception, then never execute the following
# common for __enter__ to return itself
# for example, file.__enter__() returns the file object itself 

# __exit__ can do different things depending on how the with block terminates
# exception type, exception object, exception traceback
__exit__(self, exc_type, exc_val, exc_tb)
# __exit__() called when with statement body exits
# __exit__() can check type for None to see if an exception was thrown 

# by default, __exit__() propagates exceptions thrown from the with-block
# if __exit__() returns False, the exception is propagated

# naive implementation of a context manager 
class LoggingContextManager:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None: 
            print('normal exit detected')
        else:
            print('exception detected - type={}, value={}, traceback={}').format(
                exc_type, exc_val, exc_tb)) 

'''
contextlib
'''
# standard library module for working with context managers
# provides additional tools that help turn functions into context maangers

# enforce the call of an object's close() method 

from contextlib import closing 
with closing(open("outfile.txt", "w")) as output:
    output.write("abc")

# because __enter__() and __exit__() are defined for the object that handles file I/O we can use the with directly
with open("outfile.txt", "w") as output: 
    pass 


# contextlib.contextmanager is a decorator you can use to create new context managers
# Essentially the contextlib.contextmanager decorator wraps the function in a class that implements the __enter__ and __exit__ methods

# find the yield keyword: everything before it deals with setting up the context, which entails creating
# a backup file, then opening and yielding references to the readable and writable file
# handles that will be returned by the __enter__ call. The __exit__ processing after the
# yield closes the file handles and restores the file from the backup if something went wrong.

@contextlib.contextmanager
def my_context_manager():
    # Enter
    try: # like __enter__()
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
# better to use isinstance(i, int) rather than directly call the type

'''
instropsecting objects
'''
# dir(i) returns list of attribute names and method names
# getattr(i, 'denominator') returns the same value as i.denominator
# hasattr(i, 'bit_length) i has attribute bit_length

# introspecting scopes
# globals() represents the global namespace 
# locals() returns similar dictionary as globals() 


'''
inspect module
'''
# import inspect
# import sorted_set
# inspect.getmembers(sorted_set.SortedSet, inspect.isfunction)

