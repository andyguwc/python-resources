from sqlalchemy import create_engine 
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine('sqlite:///:memory:', echo=True)
conn = engine.connect()

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
)

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String, nullable=False)
)

metadata.create_all(engine)

ins = users.insert().values(name='jack', fullname='Jack Jones')
print(str(ins))

result = conn.execute(ins)
print(dir(result))