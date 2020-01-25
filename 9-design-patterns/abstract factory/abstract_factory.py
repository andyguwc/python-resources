##################################################
#  Abstract Factory Pattern
##################################################

'''
structure
'''
# The abstract factory pattern is normally used when we have multiple possible
# implementations of a system that depend on some configuration or platform issue.
# The calling code requests an object from the abstract factory, not knowing exactly
# what class of object will be returned. The underlying implementation returned may
# depend on a variety of factors, such as current locale, operating system, or local
# configuration

# Common examples of the abstract factory pattern include code for
# operating-system independent toolkits, database backends, and country-specific
# formatters or calculators. An operating-system-independent GUI toolkit might use an
# abstract factory pattern that returns a set of WinForm widgets under Windows, Cocoa
# widgets under Mac, GTK widgets under Gnome, and QT widgets under KDE.

# Compared to factory pattern, the Abstract Factory Pattern creates familities of classes and enforces dependencies between classes 
# while the Factory Pattern only create one product. Also known as the Kit Pattern 

# abstract factory interface which needs all three models to be implemented
class AbsFactory(metaclass=ABCMeta):
    @abstractstaticmethod 
    def create_economy():
        pass 

    @abstractstaticmethod 
    def create_sport():
        pass 
    
    @abstractstaticmethod 
    def create_luxury():
        pass 

class FordFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()
    
    @staticmethod 
    def create_sport():
        return FordMustang()

    @staticmethod 
    def create_luxury():
        return LincolnMKS()


# autos base class 
class AbsAuto(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass 
    
    @abstractmethod
    def stop(self):
        pass 

class FordMustang(AbsAuto):
    def start(self):
        print('Ford Mustang ready to go')
    
    def stop(self):
        print('Ford Mustang shutting down')



'''
example - formatter factories 
'''
class FranceDateFormatter:
    def format_date():
        pass  

class USADateFormatter:
    def format_date():
        pass 

class FranceCurrencyFormatter:
    def format_currency():
        pass 

class USACurrencyFormatter:
    def format_currency():
        pass 

# formatter factories 
class USAFormatterFactory:
    def create_date_formatter(self):
        return USADateFormatter()
    def create_currency_formatter(self):
        return USACurrencyFormatter()

class FranceFormatterFactory:
    def create_date_formatter(self):
        return FranceDateFormatter()
    def create_currency_formatter(self):
        return FranceCurrencyFormatter()

factory_map = {
    "US": USAFormatterFactory,
    "FR": FranceFormatterFactory,
}

formatter_factory = factory_map.get(country_code)()


'''
example - collection of car factories 
'''

# each factory makes one brand but multiple models 

