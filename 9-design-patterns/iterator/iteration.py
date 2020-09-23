##################################################
#  Iteration Patterns
##################################################

'''
structure
'''
# Hide the implementation and exposes method for iteration 
# add new abilities to a collection 
# set, list, dictionary, tree 


'''
examples
'''
from collections improt Iterable, Iterator
# this supports multiple iterators upon initialization
# an iterable has __iter__() which returns an iterator 

class Employees(Iterable):
    _employees = {}
    _headcount = 0 
    _empid = 0 

    def add_employee(self, employee):
        self._headcount +=1 
        self._employees[self._headcount] = employee 
    
    def __iter__(self):
        return EmployeesIterator(self._employees, self._headcount)


# proper implementation which supports multiple iterators
class EmployeesIterator(Iterator):
    def __init__(self, employees, headcount):
        self._employees = employees 
        self._headcount = headcount 
        self._empid = 0 
    
    # returns itself an an iterator so taht Employees is both iterator and iterable
    def __iter__(self):
        self._empid = 0 
        return self 

    def __next__(self):
        if self._empid < self._headcount:
            self._empid +=1 
            return self._employees[self._empid]
        else:
            raise StopIteration 


# alternative - using generator expressions 
class Employees(Iterable):
    _employees = {}
    _headcount = 0 

    def add_employee(self, employee):
        self._headcount +=1 
        self._employees[self._headcount] = employee
    
    def __iter__(self):
        # generator expression which does the iterating
        # the __next__() method is essentially implemented by the generator
        return (e for e in self._employees.values())


# alternative - inherit from the sequence type of iterator 
# implements the __getitem__ method and __len__ method
# sequence iterator 
from collections import Sequence 

class Department(Sequence):
    _departments = []

    def add_department(self, department):
        self._departments.append(department)
    
    def __getitem__(self, item):
        return self._departments[item]
    
    def __len__(self):
        return len(self._departments)

# utilize internal structure
class Members(Iterable):
    members = []

    def __init__(self, members):
        self.members = members
    
    def __iter__(self):
        return iter(self.members)
