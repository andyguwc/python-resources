##################################################
#  Command Pattern
##################################################

# The goal of Command is to decouple an object that invokes an operation (the Invoker)
# from the provider object that implements it (the Receiver). In the example from Design
# Patterns, each invoker is a menu item in a graphical application, and the receivers are
# the document being edited or the application itself.

# Example: Each command may have a different receiver: the object that
# implements the action. For PasteCommand, the receiver is the Document. For Open‐
# Command, the receiver is the application.

# The Invoker is configured with a concrete command and calls its execute method to operate it.

# Building a list from the commands arguments ensures that it is iterable and keeps
# a local copy of the command references in each MacroCommand instance.
# When an instance of MacroCommand is invoked, each command in self.commands is called in sequence.

# Instead of giving the Invoker a Command instance, we can simply give it a function.
# Instead of calling command.execute(), the Invoker can just call command(). The Macro
# Command can be implemented with a class implementing __call__. Instances of Macro
# Command would be callables, each holding a list of functions for future invocation

'''
structure
'''
# encapsulate a request as an object 
# # - separate command logic from the client
# parameterize objects 
# also known as action pattern or transaction pattern 


class MacroCommand:
    """A command that executes a list of commands"""
    def __init__(self, commands):
        self.commands = list(commands)
    
    def __call__(self):
        for command in self.commands:
            command()

'''
Example the windows GUI
'''

# example of invoker objects: keyboard, button click
# actions which occur (Exit, Save, etc.) are implementations of CommandInterface

# implement a simple command pattern that provides commands for Save and Exit actions 

# first a receiver class 
import sys 

class Window: 
    def exit(self):
        sys.exit(0)
    
class Document: 
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"
    
    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)

# invoker class 
# model toolbar, menu, etc. 

class ToolbarButton:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname 
    
    def click(self):
        # calling command
        # command attribute to be set afterwards
        self.command.execute()

class MenuItem:
    def __init__(self, menu_name, menuitem_name):
        self.menu = menu_name
        self.item = menuitem_name
    
    def click(self):
        # calling command
        self.command.execute()

class SaveCommand:
    def __init__(self, document):
        self.document = document
    
    def execute(self):
        self.document.save()

window = Window()
document = Document("a_document.txt")
save = SaveCommand(document)
exit = ExitCommand(window)

save_button = ToolbarButton('save', 'save.png')
save_button.command = save
save_keystroke = KeyboardShortcut("s", "ctrl")
save_keystroke.command = save
exit_menu = MenuItem("File", "Exit")
exit_menu.command = exit


# a more python way of command pattern 
import sys
class Window: 
    def exit(self):
        sys.exit(0)
    
class MenuItem:
    def click(self):
        self.command()

window = Window()
menu_item = MenuItem()
menu_item.command = window.exit 


'''
example command line order processing system
'''
# Also known as the action pattern or transaction pattern

# three operation: CreateOrder, UpdateQuantity, ShipOrder

# abstract command

class AbsCommand(metaclass=ABCMeta):
    @abstractproperty
    def execute(self):
        pass

class AbsOrderCommand(metaclass=ABCMeta):
    @abstractproperty
    def name(self):
        pass 

    @abstractproperty
    def description(self):
        pass 

class NoCommand(AbsCommand):
    def __init__(self, args):
        self._command = args[0]
        pass

    def execute(self):
        print('No command named %s' % self._command)

# concrete command
class UpdateOrder(AbsCommand, AbsOrderCommand):
    # abstract base class properties
    name = 'UpdateQuantity'
    description = 'UpdateQuantity number'
    
    def __init__(self, args):
        self.newqty = args[1]

    def execute(self):
        oldqty=5
        print('Update database')
        print('Logging: update quantity from %s to %s' % (oldqty, self.newqty))

# main program
# mapping the name to the class 
def get_commands():
    commands = (CreateOrder, UpdateOrder, ShipOrder)
    return dict([(cls.name, cls) for cls in commands])

def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)

# find and execute the command
commands = get_commands()
command = parse_command(commands, sys.argv[1:])
command.execute()




















