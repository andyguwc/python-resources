##################################################
# Context Manager
##################################################
# an object designed to be used in a with statement
# a context-manager ensures the resources are properly and automatically managed

with context-manager:
    # enter and exit are always called no matter how the body block terminates
    enter() # prepares the context manager
    body 
    exit() # clean up 

# a context manager ensures that resources are properly and automatically managed
with open('important_data.txt', 'w') as f:
    f.write('The secret password is 12345')

# files are context managers
# file's exit() code closes the file 


'''
context manager protocol
'''
__enter__(self)
# if __enter__ throws an exception, then never execute the following
# expression.__enter__() is bound to the as variable
# common for __enter__ to return itself
# for example, file.__enter__() returns the file object itself 

# __exit__ can do different things depending on how the with block terminates
# called when with-statement block exits
# exception type, exception object, exception traceback
__exit__(self, exc_type, exc_val, exc_tb)
# __exit__() called when with statement body exits
# __exit__() can check type for None to see if an exception was thrown 

# by default, __exit__() propagates exceptions thrown from the with-block
# if __exit__() returns False, the exception is propagated (with statement asks if need to swallow the exception, if false, reraises the exception)

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


with LoggingContextManager() as x:
    print(x)


class ManagedFile:
    def __init__(self, name):
        self.name = name 

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file 

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file: 
            self.file.close()

with ManagedFile('hello.txt') as f: 
    f.write('Hello world')


##################################################
# contextlib
##################################################

'''
contextlib.contextmanager
'''
# https://pymotw.com/3/contextlib/index.html

# A context manager is enabled by the with statement, and the API involves two methods. The __enter__() method is run when execution flow enters the code block inside the with. It returns an object to be used within the context. When execution flow leaves the with block, the __exit__() method of the context manager is called to clean up any resources being used.


# enforce the call of an object's close() method 
from contextlib import closing 
with closing(open("outfile.txt", "w")) as output:
    output.write("abc")

# because __enter__() and __exit__() are defined for the object that handles file I/O we can use the with directly
with open("outfile.txt", "w") as output: 
    pass 

# from generator to context manager
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
    finally:
        # final cleanup code to execute
with my_context_manager() as x:
    pass
# exception propagated from inner context mansgers will be seen by outer context managers

# passing multiple context managers
with nest_test('a'), nest_test('b'):
    pass

# example
@contextmanager
def session_scope(commit=True):
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        if commit:
            session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    resource = acquire_resource(*args, **kwds)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)

with managed_resource(timeout=3600) as resource:
# Resource is released at the end of this block,
# even if code in the block raises an exception

# In this case, managed_file() is a generator that first acquires the
# resource. After that, it temporarily suspends its own execution and
# yields the resource so it can be used by the caller. When the caller
# leaves the with context, the generator continues to execute so that any
# remaining clean-up steps can occur and the resource can get released
# back to the system.


@contextlib.contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f 
    finally:
        f.close()

with managed_file('hello.txt') as f:
    f.write('hello world')

'''
contextlib.ContextDecorator
'''
# context manager using ContextDecorator
The class ContextDecorator adds support to regular context manager classes to let them be used as function decorators as well as context managers.

contextlib_decorator.py
import contextlib


class Context(contextlib.ContextDecorator):

    def __init__(self, how_used):
        self.how_used = how_used
        print('__init__({})'.format(how_used))

    def __enter__(self):
        print('__enter__({})'.format(self.how_used))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__({})'.format(self.how_used))


@Context('as decorator')
def func(message):
    print(message)


print()
with Context('as context manager'):
    print('Doing work in the context')

print()
func('Doing work in the wrapped function')

'''
context manager (global state change)
'''

# We'll often use context managers to make global state changes. This might be a change to the database transaction status or a change to the locking status of a resource, something that we want to do and then undo when the transaction is complete.
# For this example, we'll make a global change to the random number generator. We'll create a context in which the random number generator uses a fixed and known seed, providing a fixed sequence of values.

import random
from typing import Optional, Type
from types import TracebackType

class KnownSequence:
    def __init__(self, seed):
        self.seed = 0
    
    def __enter__(self):
        self.was = random.getstate()
        random.seed(self.seed, version=1)
        return self
    
    def __exit__(self):
        random.setstate(self.was)
        return False


# Context manager as a factory
# produce deterministic deck
# here context manager ensures we are changing global random generator temporarily
class Deterministic_Deck:
    def __init__(self, *args, **kw):
        self.args = args
        self.kw = kw
    
    def __enter__(self):
        self.was = random.getstate()
        random.seed(0, version=1)
        return Deck(*self.args, **self.kw)

    def __exit__(self):
        random.setstate(self.was)
        return False

with Deterministic_Deck(size=6) as deck:
    h = Hand(deck.pop())


# Context manager to clean up 
# have original file renamed if the context works normally
# abort and rename old file back if the context raises error

with Updating(some_path):
    with some_path.open('w') as target_file:
        process(target_file)

from pathlib import Path
from typing import Optional

class Updating:
    def __init__(self, target):
        self.target = target
        self.previous = None

    def __enter__(self):
        try:
            self.previous = (
                self.target.parent / (self.target.stem + "backup")
            ).with_suffix(self.target.suffix)
        except FileNotFoundError:
            self.previous = None
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            try:
                self.failure = (
                    self.target.parent / (self.target.stem + "error")
                ).with_suffix(self.target.suffix)
                self.target.rename(self.failure)
            except FileNotFoundError:
                pass
            if self.previos:
                self.previous.rename(self.target)
        return False
        
                

