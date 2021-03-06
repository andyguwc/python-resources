
##################################################
# SQLAlchemy
##################################################

# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
# https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
# https://github.com/oreillymedia/essential-sqlalchemy-2e


'''
ORM-friendly classes
'''
# https://github.com/PacktPublishing/Mastering-Object-Oriented-Python-Second-Edition/blob/8587f534f5af322e3449c92f2bb802ccbbfbf959/Chapter_12/ch12_ex4.py
# The class will be a Python class and can be used to create Python objects. The method functions are used by these objects.
# The class will also describe a SQL table and can be used by the ORM to create the SQL DDL that builds and maintains the database structure.
# The class will also define the mappings between the SQL table and Python class. It will be the vehicle to turn Python operations into SQL DML and build Python objects from SQL queries.


##################################################
# SQLAlchemy ORM 
##################################################

# A proper class for use with the ORM must do four things:
# • Inherit from the declarative_base object.
# • Contain __tablename__, which is the table name to be used in the database.
# • Contain one or more attributes that are Column objects.
# • Ensure one or more attributes make up a primary key.
#    - the ORM has to have a way to uniquely identify and associate an instance of the class with a specific record in the underlying database table

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
constraints
'''

class Post(Base):
    __tablename__ = 'somedata'
    __table_args__ = (ForeignKeyConstraint(['id'], ['other_table.id']),
                      CheckConstraint(unit_cost>=0,
                                      name='unit_cost_positive'))


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


##################################################
# Relational
##################################################

'''
one to many 
'''
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# one to many - one user many addresses
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    addresses = relationship("Address", backref="user")
    # this back populates the user attribute on the address object

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


class LineItem(Base):
    __tablename__ = 'line_items'
    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.order_id'))
    cookie_id = Column(Integer(), ForeignKey('cookies.cookie_id'))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12, 2))
    order = relationship("Order", backref=backref('line_items',
    order_by=line_item_id))
    cookie = relationship("Cookie", uselist=False) # this establishes a one-to-one relationship

'''
many to many
'''
# The solution is to add a third table to the database, called an association table. Now
# the many-to-many relationship can be decomposed into two one-to-many relationships
# from each of the two original tables to the association table.

class Tag(Base):
    __tablename__ = "TAG"
    id = Column(Integer, primary_key=True)
    phrase = Column(String, unique=True)

# a mapping table
# it's not a class and not derived from the declarative base 
assoc_post_tag = Table(
    "ASSOC_POST_TAG",
    Base.metadata,
    Column("POST_ID", Integer, ForeignKey("POST.id")),
    Column("TAG_ID", Integer, ForeignKey("TAG.id")),
)


# another example of many to many 

registrations = db.Table('registrations',
    db.Column('student_id', dbInteger, db.ForeignKey('students.id')),
    db.Column('class_id', db.Integer, db.ForeignKey('classes.id'))
)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    classes = db.relationship('Class',
                              secondary=registrations,
                              backref=db.backref('students', lazy='dynamic'),
                              lazy='dynamic')

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

# given Student s and Class c, the code that registers the student for the class is 
s.classes.append(c)
db.session.add(s)
# list all classes from a student
s.classes.all()
# remove a class c from student s 
s.classes.remove(c)


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


# another example of many to many 

from sqlalchemy.ext.declaractive import declarative_base
from sqlalchemy import Column, Date, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship 

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    def __repr__(self):
        return "<Customer(name='%s')>" % (self.name)

# for many to many mapping 
purchases_cheeses = Table(
    'purchaes_cheeses', Base.metadata,
    Column('purch_id', Integer, ForeignKey('purchases.id', primary_key=True)),
    Column('cheese_id', Integer, ForeignKey('cheeses.id', primary_key=True))
)

class Cheese(Base):
    __tablename__ = 'cheeses'
    id = Column(Integer, primary_key=True)
    kind = Column(String, nullable=False)
    # related indirectly through the secondary table purchaes_cheeses instead of via ForeignKey
    purchaes = relationship(
        'Purchase', secondary='purchases_cheeses', back_populates='cheeses'
    )
    def __repr__(self):
        return "<Cheese(kind='%s')>" %(self.kind)

class Purchase(Base):
    __tablename__ = 'purchases'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id', primary_key=True))
    purchase_date = Column(Date, nullable=False)
    customer = relationship('Customer')
    cheeses = relationship(
        'Cheese', secondary='purchases_cheeses', back_populates='purchases'
    )
    def __repr__(self):
        return ("<Purchase(customer='%s', dt='%s')>" % 
                (self.customer.name, self.purchase_date))

'''
self-referential relationships
'''
# User self reference user table for follow relationship
# A relationship in which both sides belong to the same table is said to be selfreferential.
# In this case the entities on the left side of the relationship are users, which
# can be called the “followers.”

# https://github.com/miguelgrinberg/flasky/blob/b666ecffb44108faf624634296bb4e7d68c0be55/app/models.py

class Follow(db.Model):
    __tablename__ = 'follows'
    follow_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'),primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Here the followed and followers relationships are defined as individual one-tomany relationships.
class User(UserMixin, db.Model):
    # ...
    followed = db.relationship('Follow',
                                foreign_keys=[Follow.follower_id],
                                backref=db.backref('follower', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')
    followers = db.relationship('Follow',
                                foreign_keys=[Follow.followed_id],
                                backref=db.backref('followed', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')

# calling user.followed.all() will return a list of 100 Follow instances

# follower helper method 

class User(db.Model):
    def follow(self, user):
        if not self.is_following(user):
            f = Follow(folloer=self, followed=user)
            db.session.add(f)
    
    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)
    
    def is_following(self, user):
        if user.id is None:
            return False 
        return self.followed.filter_by(
            followed_id=user.id).first() is not None 
    
    def is_followed_by(self,user):
        if user.id is None:
            return False 
        return self.folloers.filter_by(
            follower_id=user.id).first() is not None 

##################################################
# Query
##################################################

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



##################################################
# SQLAlchemy Core 
##################################################

# https://www.youtube.com/watch?v=0PSdzUxRYpA
# Core vs. ORM 
# ORM domain model - representing models 
# Core - shcema centric, referencing things as Table

# metadata is connection between the table structure and pythonic object
# metadata.create_all(engine) bind the metadata to the engine, looks at the database 
# and makes sure table in metadata is in the database

# actor.columns.items() to access columns in a table 

# can see the printed sql 

# dialect system

# dynamic table introspection 



'''
connecting
'''
from sqlalchemy import create_engine
# echo=True a shortcut to set up logging 
engine = create_engine('sqlite:///:memory:', echo=True)

# The engine object we created is a repository for database connections capable of issuing SQL to the database.
#  To acquire a connection, we use the connect() method:

conn = engine.connect()
# The Connection object represents an actively checked out DBAPI connection resource.
result = conn.execute(ins)

# The typical form of a database URL is:
# dialect+driver://username:password@host:port/database
# psycopg2
engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')


'''
define and create tables 
'''
# a column is represented by an object Column 
# a Column is associated with a Table 
# A collection of Table objects and their associated child objects is referred to as database metadata 

# We define our tables all within a catalog called MetaData, 
# using the Table construct, which resembles regular SQL CREATE TABLE statements.

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata=MetaData
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
)

# The usual way to issue CREATE is to use create_all() on the MetaData object. 
# This method will issue queries that first check for the existence of each individual table, 
# and if not found will issue the CREATE statements
metadta.creat_all(engine)

# create_all() creates foreign key constraints between tables usually inline with the table definition itself, 
# and for this reason it also generates the tables in order of their dependency.


'''
schema migration
'''
# While SQLAlchemy directly supports emitting CREATE and DROP statements for schema constructs, the ability to alter those constructs, usually via the ALTER statement as well as other database-specific constructs, 
# is outside of the scope of SQLAlchemy itself. While it’s easy enough to emit ALTER statements and similar by hand, such as by passing a string to Connection.execute() or by using the DDL construct, 
# it’s a common practice to automate the maintenance of database schemas in relation to application code using schema migration tools.


'''
insert expressions
'''
# Insert construct represents an INSERT statement, created relative to its target table
ins = users.insert().values(name='jack', fullname='Jack Jones')
str(ins) # print the sql stmt executed
'INSERT INTO users (name, fullname) VALUES (:name, :fullname)'
# Above, while the values method limited the VALUES clause to just two columns, 
# the actual data we placed in values didn’t get rendered into the string; instead we got named bind parameters. 
# this prevents sql injection 
ins.compile().params  
{'fullname': 'Jack Jones', 'name': 'jack'}


conn = engine.connect()
result = conn.execute(ins)
# returns below as it figures out the dialect 
# INSERT INTO users (name, fullname) VALUES (?, ?)
# ('jack', 'Jack Jones')
# COMMIT

# insert many records (calls the DBAPI's executemany() method)
# a list of dictionaries
conn.execute(addresses.insert(), [
    {'user_id': 1, 'email_address' : 'jack@yahoo.com'},
    {'user_id': 1, 'email_address' : 'jack@msn.com'},
    {'user_id': 2, 'email_address' : 'www@www.org'},
    {'user_id': 2, 'email_address' : 'wendy@aol.com'},
])


'''
update
'''
stmt = actors.update().where(actors.c.name=='test').values(name='abc')
result = conn.execute(stmt)
result.rowcount



'''
select 
'''
from sqlalchemy.sql import select
s = select([users]) # automatically expands into all columns and adds the FROM clause
result = conn.execute(s) 

# iterate through the ResultProxy (with fetchone() and fetchall())
for row in result:
    print(row)

# use Column object directly as keys
for row in conn.execute(s):
    print("name:", row[users.c.name], "; fullname:", row[users.c.fullname])

result.close()
# Result sets which have pending rows remaining should be explicitly closed before discarding. 
# While the cursor and connection resources referenced by the ResultProxy will be respectively closed 
# and returned to the connection pool when the object is garbage collected, 
# it’s better to make it explicit as some database APIs are very picky about such things:



'''
executing raw (textual) SQL
'''

from sqlalchemy.sql import text
s = text(
    "SELECT users.fullname || ', ' || addresses.email_address AS title "
        "FROM users, addresses "
        "WHERE users.id = addresses.user_id "
        "AND users.name BETWEEN :x AND :y "
        "AND (addresses.email_address LIKE :e1 "
            "OR addresses.email_address LIKE :e2)")

conn.execute(s, x='m', y='z', e1='%@aol.com', e2='%@msn.com').fetchall()

# explicit types to bind parameters
stmt = stmt.bindparams(bindparam("x", type_=String), bindparam("y", type_=String))
result = conn.execute(stmt, {"x": "m", "y": "z"})


'''
upsert (ON DUEPLICATE DO UPDATE)
'''
# postgres

insert_stmt = insert(my_table).values(
    id='some_existing_id',
    data='inserted value')

do_nothing_stmt = insert_stmt.on_conflict_do_nothing(
    index_elements=['id']
)

conn.execute(do_nothing_stmt)

do_update_stmt = insert_stmt.on_conflict_do_update(
    constraint='pk_my_table',
    set_=dict(data='updated value')
)

conn.execute(do_update_stmt)


# mysql 
# data is a sequence of mappings i.e. list of dicts
insert_stmt = insert(table, bind=engine).values(data)
update_dict = {
    c.name: c
    for c in insert_stmt.inserted
}
on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(**update_dict)
self.session.execute(on_duplicate_key_stmt)
self.session.commit()




##################################################
# SQLAlchemy Session / Transactions
##################################################

# The SQLAlchemy Session - In Depth
# https://www.youtube.com/watch?v=uAtaKr5HOdA
# https://www.sqlalchemy.org/library.html#talks

'''
transactions and sessions 
'''
# ACID
# Atomic 
# - can revert back to previsou transaction
# Consistency
# - Transations used for relational databases 
# - Provides consistency with constraints like NOT NULL, primary key and foreign key constraints
# Record persistence 
# - user.save() starts a insert transaction (autocommit)
# - can also explicitly start a transaction


# Sessions
# Explicit transaction always present
# The session maintains a cached set of transactions state, consisting of rows
# A row is only present in the Session if it was selected or inserted in the span of that transaction
# Objects, when associated with a Session, are proxies for rows, represented uniquely on primary key identity
# Changes to objects are pushed out to rows before each query, and at transaction end, using unit of work 

# Unit of work lazily flushes only those rows/columns that have changed, ordering to maintain consistency

# https://github.com/oreillymedia/essential-sqlalchemy-2e/blob/master/ch02.ipynb


'''
session commands
'''
# The session is the way SQLAlchemy ORM interacts with the database. It wraps a database
# connection via an engine, and provides an identity map for objects that you load
# via the session or associate with the session. The identity map is a cache-like data
# structure that contains a unique list of objects determined by the object’s table and
# primary key. A session also wraps a transaction, and that transaction will be open
# until the session is committed or rolled back

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()

# insert new record

cc_cookie = Cookie(cookie_name='chocolate chip',
                   cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
                   cookie_sku='CC01',
                   quantity=12,
                   unit_cost=0.50)
session.add(cc_cookie)
session.commit()
# when commit, the data is actually inserted into the database
# also updates the cc_cookie with the primary key of the record in the database 
# behind the scenes, a transaction is started and ended 


'''
session states and exceptions
'''
# possible states for session  
# transient, pending, persistent, detached
# Transient
# The instance is not in session, and is not in the database.
# Pending
# The instance has been added to the session with add(), but hasn’t been flushed or
# committed.
# Persistent
# The object in session has a corresponding record in the database.
# Detached
# The instance is no longer connected to the session, but has a record in the database

# see the session state by using the inspect method 
from sqlalchemy import inspect
insp = inspect(cc_cookie)

# MultipleResultsFound and DetachedInstanceError

# MultipleResultsFound occurs when we use the .one query method but get more than one results back 
session.add(record1)
session.add(record2)
session.commit()
results = session.query(Record).one()


# DetachedInstanceError 
# This exception occurs when we attempt to access an attribute on an instance that
# needs to be loaded from the database, but the instance we are using is not currently
# attached to the database.

# Whenever we encounter an exception, we want to issue a rollback()


from sqlalchemy.exc import IntegrityError
def ship_it(order_id):
    order = session.query(Order).get(order_id)
    for li in order.line_items:
        li.cookie.quantity = li.cookie.quantity - li.quantity
        session.add(li.cookie)
    order.shipped = True
    session.add(order)
    try:
        session.commit()
        print("shipped order ID: {}".format(order_id))
    except IntegrityError as error:
        print('ERROR: {!s}'.format(error.orig))
        session.rollback()


'''
flush
'''
# A flush is like a commit; however, it doesn’t perform a database commit
# and end the transaction. Because of this, the record instances are still connected
# to the session, and can be used to perform additional database tasks without triggering
# additional database queries.

session.add(record1)
session.add(record2)
session.flush()
print(record1.id)
print(record2.id)

# another option to use bulk_save_objects method
# this will do a single insert
# but the object isn't associated with the session so can't do print(record1.id)
session.bulk_save_objects([record1, record2])
session.commit()


'''
data access layer
'''

from sqlaclchemy.ext.declaractive import declarative_base
Base = declarative_base()

class DataAccessLayer:
    def __init__(self):
        self.engine = None 
        self.conn_string = 'some conn string'
    
    def connect(self):
        self.engine = create_engine(self.conn_string)
        Base.metadata.create_all(self.engine)
        self.Session = sessionaker(bind=self.engine)

dal = DataAccessLayer()


'''
unit testing
'''
import unittest
from db import dal 

class TestApp(unittest.TestCase):
    cookie_orders = [(1, u'cookiemon', u'111-111-1111')]

    @classmethod 
    def setUpClass(cls):
        dal.conn_string = 'sqlite:///:memory:'
        dal.connect()
        dal.session = dal.Session()
        prep_db(dal.session)
        dal.session.close()

    # add setUp method and tearDown method that ia automatically run after each test 
    def setUp(self):
        dal.session = dal.Session()

    def tearDown(self):
        dal.session.rollback()
        dal.session.close()
    
    def test_orders_by_customer_blank(self):
        results = get_orders_by_customer('')
        self.assertEqual(results, [])

# example
# https://github.com/oreillymedia/essential-sqlalchemy-2e/blob/master/ch09/test_mock_app.py



##################################################
# Flask-SQLAlchemy
##################################################

# pip install flask-sqlalchemy
# recommended to use the app factory pattern 
# which assembles an application with the add-ons and configurations (e.g. in app/__init__.py)
from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy

from config import config 

db = SQLAlchemy() # create an instance 

def create_app(config_name): 
    # defines the create_app app factory
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    return app 

# in the config.py fule 
# defines the Flask settings and the SQLAlchemy connection string 

import os 
basedir = os.path.abspath(os.path.dirnam(__file__))

class Config: 
    SECRET_KEY = 'development key'
    ADMINS = frozenset(['jason@jasonamyers.com', ])

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/dev.db"

class ProductionConfig(Config):
    SECRET_KEY = 'Prod key'
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/prod.db"

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# with the app factory and the configuration 
# can define data claases 
from app import db 

class Cookie(db.Model):
    __tablename__ = 'cookies'
    
    cookie_id = db.Column(db.Integer(), primary_key=True)
    cookie_name = db.Column(db.String(50), index=True)
    cookie_recipe_url = db.Column(db.String(255))
    quantity = db.Column(db.Integer())

# sessions are nested in the db.session object 

# http://www.aosabook.org/en/index.html

'''
upsert
'''

# https://docs.sqlalchemy.org/en/13/dialects/postgresql.html#insert-on-conflict-upsert

from sqlalchemy.dialects.postgresql import insert

stmt = insert(my_table).values(user_email='a@b.com', data='inserted data')
stmt = stmt.on_conflict_do_update(
    index_elements=[my_table.c.user_email],
    index_where=my_table.c.user_email.like('%@gmail.com'),
    set_=dict(data=stmt.excluded.data)
    )
conn.execute(stmt)


# https://stackoverflow.com/questions/7165998/how-to-do-an-upsert-with-sqlalchemy
def upsert(session, model, rows):
    table = model.__table__
    stmt = postgresql.insert(table)
    primary_keys = [key.name for key in inspect(table).primary_key]
    update_dict = {c.name: c for c in stmt.excluded if not c.primary_key}

    if not update_dict:
        raise ValueError("insert_or_update resulted in an empty update_dict")

    stmt = stmt.on_conflict_do_update(index_elements=primary_keys,
                                      set_=update_dict)

    seen = set()
    foreign_keys = {col.name: list(col.foreign_keys)[0].column for col in table.columns if col.foreign_keys}
    unique_constraints = [c for c in table.constraints if isinstance(c, UniqueConstraint)]
    def handle_foreignkeys_constraints(row):
        for c_name, c_value in foreign_keys.items():
            foreign_obj = row.pop(c_value.table.name, None)
            row[c_name] = getattr(foreign_obj, c_value.name) if foreign_obj else None

        for const in unique_constraints:
            unique = tuple([const,] + [row[col.name] for col in const.columns])
            if unique in seen:
                return None
            seen.add(unique)

        return row

    rows = list(filter(None, (handle_foreignkeys_constraints(row) for row in rows)))
    session.execute(stmt, rows)


# full example https://github.com/alphagov/notifications-api/blob/master/app/dao/returned_letters_dao.py

def insert_or_update_returned_letters(references):
    data = _get_notification_ids_for_references(references)
    for row in data:
        table = ReturnedLetter.__table__

        stmt = insert(table).values(
            reported_at=datetime.utcnow().date(),
            service_id=row.service_id,
            notification_id=row.id,
            created_at=datetime.utcnow()
        )

        stmt = stmt.on_conflict_do_update(
            index_elements=[table.c.notification_id],
            set_={
                'reported_at': datetime.utcnow().date(),
                'updated_at': datetime.utcnow()
            }
        )
        db.session.connection().execute(stmt)


# full example here 
# https://gist.github.com/bhtucker/c40578a2fb3ca50b324e42ef9dce58e1

def upsert(session, model, rows, as_of_date_col='report_date', no_update_cols=[]):
    table = model.__table__

    stmt = insert(table).values(rows)

    update_cols = [c.name for c in table.c
                   if c not in list(table.primary_key.columns)
                   and c.name not in no_update_cols]

    on_conflict_stmt = stmt.on_conflict_do_update(
        index_elements=table.primary_key.columns,
        set_={k: getattr(stmt.excluded, k) for k in update_cols},
        index_where=(getattr(model, as_of_date_col) < getattr(stmt.excluded, as_of_date_col))
        )

    print(compile_query(on_conflict_stmt))
    session.execute(on_conflict_stmt)