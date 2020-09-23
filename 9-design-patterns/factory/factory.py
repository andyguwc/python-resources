################################################
# Factory Pattern
################################################
# https://realpython.com/factory-method-python/


'''
structure
'''

# Factory Method is a design pattern that creates objects with a common interface.
# let subclasses decide which object to create in runtime

# abstract model class 
#  - with concrete models 
# factory class 
#  - this returns the concrete product 


'''
example - song serializer 
'''
# The ._get_serializer() method is the creator component. 
# The creator decides which concrete implementation to use.

class SongSerializer:
    def serialize(self, song, format):
        serializer = get_serializer(format)
        return serializer(song)


def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError(format)


def _serialize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)


def _serialize_to_xml(song):
    song_element = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_element, 'title')
    title.text = song.title
    artist = et.SubElement(song_element, 'artist')
    artist.text = song.artist
    return et.tostring(song_element, encoding='unicode')

'''
example - car manufacturer classic factory pattern
'''

# abstract auto model 
class AbsAuto(metaclass=ABCMeta):

    @property
    def name(self):
        return self._name 
    
    @property.setter 
    def name(self, name):
        self._name = name

    @abstractmethod
    def start(self):
        pass 
    
    @abstractmethod
    def stop(self):
        pass 

# concrete auto model 
class ChevyVolt(AbsAuto):
    def start(self):
        print('%s runnning with power' % self.name)

    def stop(self):
        print('%s shutting down' % self.name) 

# abstract factory baseclass
# just needs to implement create_auto method
class AbsFactory(metaclass=ABCMeta):

    @abstractmethod 
    def create_auto(self):
        pass 

# concrete create_auto method 
class ChevyFactory(AbsFactory):
    def create_auto(self):
        self.chevy = ChevyVolt()
        self.chevy.name = 'ChevyVolt'
        return self.chevy


'''
example - simple car manufacturer (just one factory)
'''
# autos.py
# abstract model
class AbsAuto(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass 
    
    @abstractmethod
    def stop(self):
        pass 

# concrete model
class ChevyVolt(AbsAuto):
    def start(self):
        print("This is chevy")

    def stop(self):
        print("Stops chevy")

# concrete model
class Ford(AbsAuto):
    def start(self):
        print("This is ford")

    def stop(self):
        print("Stops ford")

# null concrete model 
class NullCar(AbsAuto):
    def __init__(self, carname):
        self._carname = carname 
    
    def start(self):
        print("unknown car name %s" % self._carname)

    def stop(self):
        pass 


# simple factory function
# the factory has a name to object mapping 
# and a create instance method to create appropriate instances based on the carname passed in 

from inspect import getmembers, isclass, isabstract
import autos

# create an instance of desired class
class AutoFactory(object):
    autos = {} # a dictionary of car model name mapping to the class of car

    def __init__(self):
        self.load_autos()
    
    def load_autos(self):
        # get concrete classes imported in the package 
        classes = getmembers(autos, lambda m: isclass(m) and not isabstract(m))

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, autos.AbsAuto):
                self.autos.update(dict(name, _type))
        
    def create_instance(self, carname):
        if carname in self.autos:
            return self.autos[carname]()
        else:
            return autos.Nullcar(carname)

# main program 
factory = AutoFactory()

for carname in ['Chevy', 'Ford']:
    car = factory.create_instance(carname)
    car.start()
    car.stop()

