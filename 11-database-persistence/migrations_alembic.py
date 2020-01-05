##################################################
# Database Migration Using Alembic
##################################################

# database migration
# - incremental, reversible changes to a relational database 
# - allows us to make changes without resetting
# alembic is SqlAlchemy specific 

'''
setup
'''
# $ alembic init migrations

# in alembic.ini
# change the script_location
# and the sqlalchemy.url = 'postgresql://{username}:{password}@{host}:{port}/{database}

# env.py
# configures and generat a SQLAlchemy engine
# refers to the sqlalchemy.url in alembic.ini
# modify so it gets access to a table metadata object containing the target
# from project_name import models (in the project_name/models we imported declaractive_base())
target_metadata = models.DeclarativeBase.metadata

# alembic tutorial 
# https://alembic.sqlalchemy.org/en/latest/tutorial.html


'''
revision
'''
# $ alembic revision -m "messages"
# this will generate a migration file with upgrade and downgrade parts 

# auto-generate migrations 
# https://alembic.sqlalchemy.org/en/latest/autogenerate.html
# $ alembic revision --autogenerate -m "add new stuff"


'''
run migrations
'''
# head is a shortcut to the latest revision
# $ alembic upgrade head 

# how it works
# alembic checks if the alembic_version table exists, if not it creates one 
# revision hash will be a new row


# check current and history
# $ alembic current 
# $ alembic history --verbose 


'''
add schema
'''
# https://causecode.com/postgres-schema-level-migration-using-alembic-for-python/
# modify the env.py
def run_migrations_online():
    # ... 
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table_schema=target_metadata.schema,
            include_schemas=True
        )
        with context.begin_transaction():
            context.execute('SET search_path TO sample')
            context.run_migrations()

# modify the db.py
engine = create_engine(settings.JDBC_CONN_STRING)
session = sessionmaker(bind=engine)()
session.execute("SET search_path TO sample")

# modify the models.py
DeclarativeBase = declarative_base()

class Task(DeclarativeBase):
    __tablename__ = "task"
    __table_args__ = {"schema": "sample"}




