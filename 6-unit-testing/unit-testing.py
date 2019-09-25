################################################
# Best Practices
################################################
# https://docs.python-guide.org/writing/tests/

# A testing unit should focus on one tiny bit of functionality and prove it correct
# Each test unit must be fully independent
# Make tests run fast 
# Use long and descriptive test names

# Arrange Act Assert
# http://wiki.c2.com/?ArrangeActAssert

# Arrange all necessary preconditions and input
# Act on the object or method under test
# Assert that the expected results have occurred

################################################
# Test Case Design
################################################

# Reasons for Unit Testing
# Understand what to build
# Document the units
# Design the units - idependently testable
# Regression Protection

# A unit test checks the behavior of an element of code
# A method or function
# A module or class

# An automated test
# runs without intervention 

# Test Case
# Each should be for a specific behavior
# Shouldn't have side effects (like creating data other test cases use)

# $ python3 -m unittest


# Basic Unittest

import unittest
def func(x):
    return x+1

class Mytest(unittes.TestCase):
    def test(self):
        self.assertEqual(func(3),4)


# in test_phonebook.py
import unittest

from phonebook import Phonebook

class TestPhonebook(unittest.TestCase):
    def test_create_phonebook(self):
        phonebook = Phonebook()

# in phonebook.py
class Phonebook:
    pass

# run a specific test 
# $ python3 -m unittest -q test_phonebook.TestPhonebook.test_lookup_entry_by_name

# skip a test
@unittest.skip("WIP")

def tearDown(self):
    pass

# setUp()
# before each test case is run, the test case can access the object defined in setUp
def setUp(self):
    self.phonebook = Phonebook()

# to do cleanup 
def tearDown(self):
    pass


# Test Case Name
#  - Arrange setup the object to be tested & collaborators
#  - Act exercise functionality on the object
#  - Assert make claims about the object & its collaborators
#  - Cleanup



# Test last (Design code -> design tests -> debug & rework)
# Risk: discover testability problems and bugs late in the process

# Test first (Design code -> design tests -> write code )
# Risk: rework (needs to refactor tests and code)

# Test first (Design code -> design tests -> write code )
# Risk: rework (needs to refactor tests and code)

# Test driven (design and build up test case together)
# write a test -> write a little code -> refactor 


# Continuous integration
# version control -> continous integration server 

################################################
# Pytest
################################################

# pip install -U pytest

# run tests
# python3 -m pytest

from phonebook import Phonebook

def test_add_and_lookup_entry():
    phonebook = Phonebook()
    phonebook.add("Bob","123")
    assert "123" == phonebook.lookup("Bob")
    assert "123" == None


# text fixture https://docs.pytest.org/en/latest/fixture.html#fixtures
# to share data between test cases
# offers a baseline upon which tests can execute

# test case request a resource
@pytest.fixture
def resource():
    return Resource()


# adding a test fixture and clearning out
@pytest.fixture
def phonebook(request):
    phonebook = Phonebook()
    def cleanup_phonebook():
        phonebook.clear()
    request.addfinalizer(cleanup_phonebook)
    return phonebook


import pytest_example
@pytest.fixture
def smtp_connection():
    import smtplib
    return smtplib.SMTP("smtp.gmail.com",587,timeout=5)

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0 





# assertions about expected exceptions

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0 

################################################
# doctest
################################################
# make documentation comments more truthful
# searches for pieces of text that look like interactive python sessions in docstrings and then executes those sessions
def square(x):
    """Return the square of x.
    >>> square(2)
    4
    >>> square(-2)
    4
    """
    return x*x 

if __name__ == '__main__':
    import doctest
    doctest.testmod()


# checking examples in docstrings
# regression testing 

# $ python3 -m doctest -v xx.py

# docstring runs each test while pytest treats the entire block as one test 

# tracebacks


################################################
# Test Doubles
################################################
# class under test doesn't know it isn't talking to real one 

# test stub 
# stub has the same interface as the original 
# no logic or advanced behavior
# not the same as Mock 


class Alarm(object):
    # pass in an optional argument which can be subbed for testing
    def __init__(self, sensor =None):
        self._low_pressure_threshold = 15
        self._high_pressure_threshold = 21
        self._sensor = sensor or Sensor()
        self._is_alarm_on = False
    

class AlarmTest(unittest.TestCase):
    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm._is_alarm_on)
    
    def check_too_low_pressure_sounds_alarm(self):
        # pass in test sensor
        alarm = Alarm(sensor=TestSensor())
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

class TestSensor:
    def sample_pressure(self):
        return 15


# use the mock library 
def test_check_with_pressure_ok_with_mock_fw(self):
    # using mock to pass in test sensor 
    test_sensor = Mock(Sensor)
    test_sensor.sample_pressure.return_value = 18
    alarm = Alarm(test_sensor)
    alarm.check()
    self.assertFalse(alarm.is_alarm_on)



# fake object 
# replace a whole component or subsystem
# fake has functionality, logic or implementation that works on some level 
# for example, create a fake file wrapper that wraps around a file 

# replace with something more lights: usually for file, database, webserver 
class FakeFileWrapper:
    def __init__(self, text):
        self.text= text
    
    def open(self):
        return io.StringIO(self.text)


# mock object 
# make assertions 
# mock can cause a test to fail 

# assertions
# check the return value or an exception
# check a state change (use a public API)
# check a method call (use a mock or spy)

# interaction testing 

def test_invalid_token_with_mock(self):
    token = SSOToken()
    registry = MockSingleSignOnRegistry(expected_token=token, token_is_valid=False)
    my_service = MyService(registry)

    response = my_service.handle_request("do_stuff", token=token)
    self.assertTrue(registry.is_valid_was_called)

# test spy 


# monkeypatching
# changing code at runtime 



################################################
# Parameterized Testing & Test Coverage
################################################
# parametrerized tests with unittest and pytest 

# use custom assert to reduce repitition of test cases

def assert_tennis_score(self, expected_score, player1_points, player2_points):
    self.assertEqual(expected_score, tennis_score(player1_points,player2_points))

# measuring coverage of tests 


# defining parameterized tests 
# using meta programming 
# first template the tests
# pass in bunch of examples as one data 

def tennis_test_template(*args):
    def foo(self):
        self.assert_tennis_score(*args)
    return foo 

    class TennisTest(unittest.TestCase):
        def assert_tennis_score(self, expected_score, player1_points, player2_points):
            self.assertEqual(expected_score, tennis_score(player1_points, player2_points))


# using pytest
from tennis import tesnnis_store
import pytest 

examples = ( ("expected_score","player1_points", "player2_points"),
            [("Love-All", 0, 0),
                ("Fifteen-All",1, 1),
                ("Thirty-All",2,2)
            ])
@pytest.mark.parametrize(*examples)                        
def test_early_game_scores_equal(expected_score, player1_points, player2_points):
    assert expected_score == tennis_score(player1_points, player2_points)


# test coverage 

# pip-3.3 install coverage
# pip-3.3 install pytest-cov

# can mark something as uninteresting #pragma: no cover 


# create config file for coverage tool 

# find missing test cases
# get legacy code under test
# continuous integration - constant management 



##################################################
# Exceptions
##################################################


# Try Statement
# We can use try statements to handle exceptions. 

# try: This is the only mandatory clause in a try statement. The code in this block is the first thing that Python runs in a try statement.
# except: If Python runs into an exception while running the try block, it will jump to the except block that handles that exception.
# else: If Python runs into no exceptions while running the try block, it will run the code in this block after running the try block.
# finally: Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. 


while True:
    try:
        x = int(input('Enter a number'))
        break
    except ValueError:
        print('That\'s not a valid number')
    finally:
        print('\nAttempted Input\n')

# accessing error mesages
try:
    # some code
except Exception as e:
    # some code
    print("Exception occured: {}".format(e))



# raising and catching errors
try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception:
    print("got an error")

print("continuing")


# continue 
# always specify an exception type
while True:
    try:
        #
    except ValueError: 
        continue # this just ignores the error and continues

# standard exception hierarchy
# IndexError
# KeyError
# IndexError and KeyError are subclasses of LookupError


# Exception payloads
# contains diagonalist information
try:
    #
except ValueError as e:
    print("Payload:", e.args)
    print(str(e))

# defining new exceptions
class TriangleError(Exception):
    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)
    
    @property
    def sides(self):
        return self._sides
    
    def __str__(self):
        return "'{}' for sides {}".format(self.args[0], self._sides)
    
    def __repr__(self):
        return "TriangleError({!r},{!r}".format(self.args[0], self._sides)


def triangle_area(a,b,c):
    sides = sorted((a,b,c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal Triangle", sides)
    p = (a+b+c)/2
    a = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return a 

# chaining exceptions
# implicit chaining - during handling of one exception, another one occurred. Implented using the __context__
# explicit chaining 

# tracebacks
# records of the function stacks 
__traceback__ 
def main():
    try:
        inclination(0,5)
    except InclinationError as e:
        print(e.__traceback__)
        traceback.print(e.__traceback__)
        s = traceback.format_tb(e.__traceback__)
        print(s)

# assertions for monitoring program invariants (should always be true)
assert condition , message # optional error string to print if condition is False

def func():
    if:
        # 
    elif:
        #
    else:
        assert False, "This should never happen"

# class invariants

# assertions are for checking function implementations
# shouldn't use it for validating client inputs, instead should just raise errors
# use assertions for checking preconditions and postconditions
assert(all(len(line)<=line_length for line in result.splitlines())

