##################################################
#  Builder
##################################################

'''
structure
'''
# creational pattern 
# separates construction of an object from its representation 
# encapsulates the object construction 
# allows multistep construction process 

# a Director product with construct() to assemble the parts (BuilderPart())
# the ConcreteBuilder class implements each BuildPart()
# the ConcreteBuilder inherits from the AbsBuilder interface


'''
example - build custom computer
'''

# # in main program
# builder = MyComputerBuilder()
# builder.build_computer()
# computer = builder.get_computer()
# computer.display()


# abstract builder 

class AbsBuilder(metaclass=ABCMeta):
    def get_computer(self):
        return self._computer 
    
    def new_computer(self):
        self._computer = Computer()
    
    @abstractmethod 
    def get_case(self):
        pass 

    @abstractmethod 
    def get_mainboard(self):
        pass 
    
    @abstractmethod
    def get_hard_drive(self):
        pass 
    
    
class MyComputerBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = 'Coolermaster'

    def get_mainboard(self):
        self._computer.mainboard = 'MSI'     
        self._computer.cpu = 'Intel Core'
    
    def get_hard_drive(self):
        self._computer.hard_drive = 'Seagate'

class AnotherComputerBuilder(AbsBuilder):
    pass 

class Director(object):
    def __init__(self, builder):
        self._builder = builder 
    
    def build_computer(self):
        self._builder.new_computer()
        self._builder.get_case()
        self._builder.get_mainboard()
        self._builder.get_hard_drive()
    
    def get_computer(self):
        return self._builder.get_computer()

computer_builder = Director(MyComputerBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

