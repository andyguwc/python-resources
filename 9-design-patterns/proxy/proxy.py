
##################################################
# Proxy Pattern
##################################################

'''
structure
'''
# proxy between client code and the objects to access 
# - remote proxy 
# - virtual proxy 
# - protection proxy 
# - smart reference proxy

# proxy keeps a reference to the subject
# exposes an identical interface


'''
example - get employee record 
'''
# abstract structure
class AbsEmployees(metaclass=ABCMeta):
    @abstractmethod 
    def get_employees_info(self, empids):
        pass 

# concrete subject
class Employees(AbsEmployees):
    def get_employees_info(self, empids):
        return (EMPLOYEES[empid]
                for empid in empids
                if empid in EMPLOYEES)

# proxy itself 
# composition of the concrete subject
class Proxy(AbsEmployees):
    def __init__(self, employees, reqid):
        self._employees = employees
        self._reqid = reqid 
    
    def get_employees_info(self, empids):
        reqid = self._reqid 
        acc = AccessControls.get_access_control()
        for e in self._employees.get_employees_info(empids):
            if e.empid == reqidd or \
                (reqid in acc and acc[reqid].can_see_personal):
                yield Employee(e.empid, e.name, e.birthdate)

# main program

def get_employees_collection(reqid):
    return Proxy(Employees(), reqid)


