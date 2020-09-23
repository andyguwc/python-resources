
##################################################
#  Adapter Pattern
##################################################

'''
structure
'''
# adapters allow two pre-existing objects to work together even if interfaces are not compatible
# The adapter object's sole purpose is to perform this translation job. 

# Adapting may entail a variety of tasks, such as converting arguments to a different format, rearranging the order of arguments, calling a differently named method, or supplying default arguments.

# Map between two interfaces to let classes work together 
#  - Object adapaters: Composition (better approach with flatter class structure)
#  - Class adapaters: Inheritance


'''
example - date format adapter
'''
# example, we have a preexisting class which takes a string date in the format "YYYY-MM-DD"
class AgeCalculator:
    def __init__(self, birthday):
        self.year, self.month, self.day = (
            int(x) for x in birthday.split('-'))
    
    def calculate_age(self, date):
        year, month, day = (
            int(x) for x in date.split('-'))
        age = year - self.year
        if (month,day) < (self.month,self.day):
            age -= 1
        return age
    
# rewrite the class to accept datetime objects 
# whenever we want to calculate the age on a datetime.date object, we could call
# datetime.date.strftime('%Y-%m-%d') to convert it to the proper format
# write an adapter that allows a normal date to be plugged into a normal AgeCalculator class 

import datetime
class DateAgeAdapter:
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")
    
    def __init__(self, birthday):
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)
    
    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)

calculator = DateAgeAdapter(birthday=datetime.datetime.today())
calculator.get_age(datetime.datetime.today())

'''
example - composition adapter 
'''
# object (composition) adapter delegates to the adaptee 
# customers and have different address properties

class Customer(object):
    def __init__(self, name, address):
        self._name = name 
        self._address = address 

    @property 
    def name(self):
        return self._name 
    
    @property 
    def address(self):
        return self._address 


# concrete vendor adapater 
class VendAdapter(Object):
    def __init__(self, adaptee):
        self.adaptee = adaptee 

    @property 
    def name(self):
        return self.adaptee.name 

    @property 
    def address(self):
        return '{}{}'.format(
            self.adaptee.number, 
            self.adaptee.street 
        )

mock_vendors = (
    VendAdapter(Vendor('Dough factory', 1, '123 road'))
)

for item in mock_vendors:
    print('Name %s; Address %s' % (item.name, item.address))


'''
example - class adapter to modify the address printed out
'''
# the adapter inherits from both the original class and the adapted class 
# class adapter overwrites the adaptee methods 
# adapt the vendor properties into customer property

class VendorAdapter(Vendor, Customer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @property
    def address(self):
        return '{}{}'.format(
            self.number, self.street
        )

mock_vendors = (
    VendorAdapter('Dough factory', 1, '123 road')
)

for item in mock_vendors:
    print('Name %s; Address %s' % (item.name, item.address))



