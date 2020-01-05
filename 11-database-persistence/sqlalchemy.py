
##################################################
# SQLAlchemy
##################################################

# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
# https://www.compose.com/articles/using-postgresql-through-sqlalchemy/


'''
ORM-friendly classes
'''
# https://github.com/PacktPublishing/Mastering-Object-Oriented-Python-Second-Edition/blob/8587f534f5af322e3449c92f2bb802ccbbfbf959/Chapter_12/ch12_ex4.py
# The class will be a Python class and can be used to create Python objects. The method functions are used by these objects.
# The class will also describe a SQL table and can be used by the ORM to create the SQL DDL that builds and maintains the database structure.
# The class will also define the mappings between the SQL table and Python class. It will be the vehicle to turn Python operations into SQL DML and build Python objects from SQL queries.


'''
SQLAlchemy Models 
'''
# declaractive base class provides a mataclss for our application's class definitions
# serves as a repository for the metadata that we are defining for our database

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table
from sqlalchemy import BigInteger, Boolean, Date, DateTime, Enum, Float, Integer, Interval, LargeBinary, Numeric, PickleType, SmallInteger, String, Text, Time, Unicode, UnicodeText ForeignKey
from sqlalchemy.orm import relationship, backref

# SQLAlchemy's metaclass is built byt the declarative_base() function:
Base = declarative_base()

# The Base objec that was created must be the metaclass for any persistent class we're defining 
class Blog(Base):
    __tablename__ = "BLOG"
    # id column is an Integer primary key 
    # implicitly this is an auto-increment field 
    id = Column(Integer, primary_key=True)
    title = Column(String)
    def as_dict(self):
        return dict(
            title = self.title,
            underline= '='*len(self.title),
            entries= [ e.as_dict() for e in self.entries ]
        )


# adding index
class Post(Base):
    __tablename__ = "POST"
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    date = Column(DateTime, index=True)
    blog_id = Column(Integer, ForeignKey('BLOG.id'), index=True)


'''
Create Engine
'''
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
session.commit()


'''
Relational
'''
# one to many 
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    addresses = relationship("Address", backref="user")

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

u1 = User()
a1 = Address()
print(u1.addresses)
print(a1.user)

u1.addresses.append(a1)
print(u1.addresses)
print(a1.user)


# many to many 

class Tag(Base):
    __tablename__ = "TAG"
    id = Column(Integer, primary_key=True)
    phrase = Column(String, unique=True)

# a mapping table 
assoc_post_tag = Table(
    "ASSOC_POST_TAG",
    Base.metadata,
    Column("POST_ID", Integer, ForeignKey("POST.id")),
    Column("TAG_ID", Integer, ForeignKey("TAG.id")),
)


# using back_populates

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="addresses")
    
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

# The two complementing relationships Address.user and User.addresses are referred to as a bidirectional relationship, and is a key feature of the SQLAlchemy ORM. 
User.addresses = relationship(
    "Address", order_by=Address.id, back_populates="user")



'''
Query
'''
# https://www.pythonsheets.com/notes/python-sqlalchemy.html
# https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91


# set a DB URL
from sqlalchemy.engine.url import URL

postgres_db = {'drivername': 'postgres',
               'username': 'postgres',
               'password': 'postgres',
               'host': '192.168.99.100',
               'port': 5432}
print(URL(**postgres_db))


# Create a session 
# https://www.pythonsheets.com/notes/python-sqlalchemy.html
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine
engine = create_engine(settings.JDBC_CONN_STRING)
Session = sessionmaker(bind=engine)
session = Session()
# in case of schema
session.execute("SET search_path TO prospector")


# Maniput objects 
blog = Blog(title="abc")
session.add(blog)


# create a Tag if not existing
tags = []
for phrase in ('abc', 'def')
    try:
        tag = session.query(Tag).filter(Tag.phrase == phrase).one()
    except sqlaclchemy.orm.exc.NoResultFound:
        tag = Tag(phrase=phrase)
        session.add(tag)
    tags.append(tag)


# returning lists and scalars
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
partial_results = ResultProxy.fetchmany(50)

# all() 
# first()
# one() fully fetaches all rows and if not exactly one row raises an error
# one_or_none() 

# make it a dataframe
df = pd.DataFrame(ResultSet)
df.columns = ResultSet[0].keys()




'''
Run Raw SQL
'''

# execute SQL with params to prevent sql injection 

db.my_session.execute(
    "UPDATE client SET musicVol = :mv, messageVol = :ml",
    {'mv': music_volume, 'ml': message_volume}
)

# or define a helper function 
# in db.py
def get_results(sql, **params):
    if params is not None:
        resultproxy = session.execute(sql, params)
    else:
        resultproxy = session.execute(sql)
    if not resultproxy:
        return []
    return [{col:val for col, val in rowproxy.items()} for rowproxy in resultproxy]

sql = "SELECT * from organizations where name = :name"
name = '123'
db.get_results(sql, name=name)


