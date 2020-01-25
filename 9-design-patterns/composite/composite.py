##################################################
#  Composite Pattern
##################################################

'''
structure
'''
# The composite pattern allows complex tree-like structures to be built from simple
# components. These components, called composite objects, are able to behave sort
# of like a container and sort of like a variable depending on whether they have child
# components. Composite objects are container objects, where the content may actually
# be another composite object.

# clients can handle individual objects and collections of objects 


'''
example - represent folders and files 
'''
# example use composite object to represent folders and leaf nodes to represent normal firles
# abstract away the similar operations in File and Folder 

class Component:
    def __init__(self, name):
        self.name = name 
    
    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self 
        self.parent = new_folder
    
    def delete(self):
        del self.parent.children[self.name]
    
class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}
    
    def add_child(self, child):
        child.parent = self 
        self.children[child.name]

    def copy(self, new_path):
        pass

class File(Component):
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents
    def copy(self, new_path):
        pass

root = Folder('')
def get_path(path):
    names = path.split('/')[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node 

# >>> folder1 = Folder('folder1')
# >>> folder2 = Folder('folder2')
# >>> root.add_child(folder1)
# >>> root.add_child(folder2)
# >>> folder11 = Folder('folder11')
# >>> folder1.add_child(folder11)

# AddComponent()
# GetChild()
# Operation()
# RemoveComponent()


'''
example
'''
class AbsComposite(metaclass=ABCMeta):
    @abstracmethod 
    def get_oldest(self):
        pass 


class Person(AbsComposite):

    def __init__(self, name, birthdate):
        self.name = name 
        self.birthdate = birthdate 
    
    def get_oldest(self):
        return self 

class Tree(Iterable, AbsComposite):

    def __init__(self, members):
        self.members = members 

    def __iter__(self):
        return iter(self.members)
    
    def get_oldest(self):
        # compare two items and return the one
        def f(t1, t2):
            t1_, t2_ = t1.get_oldest(), t2.get_oldest()
            return t1_ if t1.birthdate < t2._birthdate else t2_ 
        return reduce(f, self, NullPerson())


class NullPerson(AbsComposite):
    name = None 
    birthdate = date.max 
    def get_oldest(self):
        return self


