##################################################
#  Iteration Patterns
##################################################

'''
structure
'''


# Hide the implementation and exposes method for iteration 
# collection 
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

# using generator expressions 

class Employees(Iterable):
    _employees = {}
    _headcount = 0 

    def add_employee(self, employee):
        self._headcount +=1 
        self._employees[self._headcount] = employee
    
    def __iter__(self):
        return (e for e in self._employees.values())


# alternative - inherit from the sequence type of iterator 
# implements the __getitem__ method and __len__ method
class Department(Sequence):
    _departments = []

    def add_department(self, department):
        self._departments.append(department)
    
    def __getitem__(self, item):
        return self._departments[item]
    
    def __len__(self):
        return len(self._departments)