##################################################
#  Template Pattern
##################################################

'''
structure 
'''
# It is designed for situations where we have several different tasks to accomplish that have some, but not all, steps in common. The
# common steps are implemented in a base class, and the distinct steps are overridden
# in subclasses to provide custom behavior. In some ways, it's like a generalized
# strategy pattern, except similar sections of the algorithms are shared using a base class.

# define skeleton deferring some steps to concrete algorithms. This ensures all required steps are implemented
#  - Abstract method 
#  - Concrete methods 
#  - Hooks (may be overwritten)
#  - Fixed process order 

'''
example 
'''

# connect to SQLite database get results and format the results.
# The common steps are connecting and outputing which we can put into a template pattern 

class QueryTemplate:
    def connect(self):
        self.conn = sqlite3.connect("sales.db")

    # this method is outside of template and needs subclass to override 
    def construct_query(self):
        raise NotImplementedError()

    def do_query(self):
        results = self.conn.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        output = []
        for row in self.results:
            row =[str(i) for i in row]
            output.append(", ".join(row))
        self.formatted_results = "\n".join(output)
    
    def output_results(self):
        raise NotImplementedError()
    
    # this method calls all steps
    def process_format(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_results()
        self.output_results()


# concete class 
import datetime
class NewVehiclesQuery(QueryTemplate):
    def construct_query(self):
    self.query = "select * from Sales where new='true'"
    def output_results(self):
    print(self.formatted_results)
