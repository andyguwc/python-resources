


##################################################
#  Patterns
##################################################
# Creational 
# - object creation
# Structural
# - object relationships
# Behavioral
# - object interation and responsibility 

# SOLID Principle 
# - Single responsibility
# - Open-closed: open for extension but closed for modification 
# - Substituion: sub classes can stand in for parents without breaking it 
# - Inteface segregation
# - Dependency inversion: abstrations not implementations



##################################################
#  Flyweight Pattern
##################################################

# The flyweight pattern basically ensures that objects that share a state can use the
# same memory for that shared state. It is often implemented only after a program
# has demonstrated memory problems. It may make sense to design an optimal
# configuration from the beginning in some situations, but bear in mind that
# premature optimization is the most effective way to create a program that is too
# complicated to maintain.

# Each Flyweight has no specific state; any time it needs to perform an operation on
# SpecificState, that state needs to be passed into the Flyweight by the calling code.
# Traditionally, the factory that returns a flyweight is a separate object; its purpose
# is to return a flyweight for a given key identifying that flyweight.

# example car model factory

import weakref 

class CarModel:
    _models = weakref.WeakValueDictionary()

    # whenver we construct a new flyweight with a given name, 
    # first look at the name in the weak referenced dictionary 
    # (if exists, return the model, if not create a new one)

    def __new__(cls, model_name, *args, **kwargs):
        model = cls._models.get(model_name)
        if not model: 
            model = super().__new__(cls)
            cls._models[model_name] = model 
        return model 
    
    def __init__(self, model_name, air=False, tilt=False,
        cruise_control=False, power_locks=False,
        alloy_wheels=False, usb_charger=False):
        # only intialized object the first time it is called 
        if not hasattr(self, "initted"):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.power_locks = power_locks
            self.alloy_wheels = alloy_wheels
            self.usb_charger = usb_charger
            self.initted=True
        

