
##################################################
# SQL Model
##################################################

# database connection
# All database access requires a connection, created with the module function, sqlite3.connect().

# database operations involve cursor 

crsr = database.cursor()
for stmt in sql_ddl.split(";"):
    crsr.execute(stmt)


'''
Access Layer
'''
# designing access layer for SQL 

class Access:
    get_last_id = """
    SLECt last_insert_rowd()
    """
    def open(self, filename):
        self.database = sqlite3.connect(filename)
        self.database.row_factory = sqlite3.Row 
    
    def get_blog(self, id):
        query_blog = """
        SELECT * FROM BLOG WHERE ID = ?
        """
        row = self.database.execute(query_blog, (id,)).fetchone()
        blog = Blog(id=row['ID'], title=row['TITLE'])
        return blog 
    
    def add_blog(self, blog):
        insert_blog = """
        INSERT INTO BLOG(TITLE) VALUES(:title)
        """
        self.database.execute(insert_blog, dict(title=blog.title))
        row = self.database.execute(get_last_id).fetchone()
        blog.id=row[0]
        return blog 

'''
ORM Layer (SQLAlchemy)
'''

# • The class will be a Python class and can be used to create Python objects. The
# method functions are used by these objects.
# • The class will also describe a SQL table and can be used by the ORM to create
# the SQL DDL that builds and maintains the database structure.
# • The class will also define the mappings between the SQL table and Python
# class. It will be the vehicle to turn Python operations into SQL DML and
# build Python objects from SQL queries.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table
from sqlalchemy import BigInteger, Boolean, Date, DateTime, Enum, \
Float, Integer, Interval, LargeBinary, Numeric, PickleType, \
SmallInteger, String, Text, Time, Unicode, UnicodeText ForeignKey
from sqlalchemy.orm import relationship, backref

# SQLAlchemy's metaclass is built byt the declarative_base() function:
Base = declarative_base()

# The Base objec that was created must be the metaclass for any persistent class we're defining 
class Blog(Base):
    __tablename__ = "BLOG"
    # id column is an Integer primary key 
    id = Column(Integer, primary_key=True)
    title = Column(String)
    def as_dict(self):
        return dict(
            title = self.title,
            underline= '='*len(self.title),
            entries= [ e.as_dict() for e in self.entries ]
        )

# ORM Layer create an engine
from sqlalchemy import create_engine
engine = create_engine('sqlite:///./p2_c11_blog2.db', echo=True)
Base.metadata.create_all(engine)


# to manupulate object, get a session cache
# add new objects to the session cache and use the session cache to query objects in the database 
from sqlaclchemy.orm import sessionmaker
# session class bounded to the database engine
Session = sessionmaker(bind=engine)
# use Session class to build a session object
session = Session()

blog = Blog(title = "travel")
session.add(blog)


# add indexes 
class Post(Base):
    __tablename__ = "POST"
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    date = Column(DateTime, index=True)
    blog_id = Column(Integer, ForeignKey('BLOG.id'), index=True)