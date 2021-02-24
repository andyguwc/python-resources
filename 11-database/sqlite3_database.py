
##################################################
# sqlite3
##################################################

# https://pymotw.com/3/sqlite3/index.html


'''
sqlite3 conn
'''

# An SQLite database is stored as a single file on the file system. The library manages access to the file, including locking it to prevent corruption when multiple writers use it. The database is created the first time the file is accessed, but the application is responsible for managing the table definitions, or schema, within the database.

import os
import sqlite3

db_filename = 'todo.db'

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

conn.close()

'''
create schema
'''

-- todo_schema.sql
-- Schema for to-do application examples.

-- Projects are high-level activities made up of tasks
create table project (
    name        text primary key,
    description text,
    deadline    date
);

-- Tasks are steps that can be taken to complete a project
create table task (
    id           integer primary key autoincrement not null,
    priority     integer default 1,
    details      text,
    status       text,
    deadline     date,
    completed_on date,
    project      text not null references project(name)
);


db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Inserting initial data')

        conn.executescript("""
        insert into project (name, description, deadline)
        values ('pymotw', 'Python Module of the Week',
                '2016-11-01');

        insert into task (details, status, deadline, project)
        values ('write about select', 'done', '2016-04-25',
                'pymotw');

        insert into task (details, status, deadline, project)
        values ('write about random', 'waiting', '2016-08-22',
                'pymotw');

        insert into task (details, status, deadline, project)
        values ('write about sqlite3', 'active', '2017-07-31',
                'pymotw');
        """)
    else:
        print('Database exists, assume schema does, too.')

'''
retrieving data
'''

# To retrieve the values saved in the task table from within a Python program, create a Cursor from a database connection. A cursor produces a consistent view of the data, and is the primary means of interacting with a transactional database system like SQLite.

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select id, priority, details, status, deadline from task
    where project = 'pymotw'
    """)

    for row in cursor.fetchall():
        # returned rows are tuples
        task_id, priority, details, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))

# retrieved one at a time with fetchone()

# fixed-size batches with fetchmany()

for row in cursor.fetchmany(5):
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))

'''
query parameters
'''

import sqlite3
import sys

db_filename = 'todo.db'
project_name = sys.argv[1]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """
    select id, priority, details, status, deadline from task
    where project = ?
    """

    cursor.execute(query, (project_name,))

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))


# named parameters
with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    query = """
    select id, priority, details, status, deadline from task
    where project = :project_name
    order by deadline, priority
    """
    cursor.execute(query, {'project_name': project_name})

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    query = "update task set status = :status where id = :id"
    cursor.execute(query, {'status': status, 'id': id})


'''
bulk loading
'''

# use executemany to apply the same SQL instruction to a large set of data

import csv
import sqlite3
import sys

db_filename = 'todo.db'
data_filename = sys.argv[1]

SQL = """
insert into task (details, priority, status, deadline, project)
values (:details, :priority, 'active', :deadline, :project)
"""

with open(data_filename, 'rt') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.executemany(SQL, csv_reader)


'''
transactions
'''

# https://pymotw.com/3/sqlite3/index.html#transactions

# One of the key features of relational databases is the use of transactions to maintain a consistent internal state. With transactions enabled, several changes can be made through one connection without effecting any other users until the results are committed and flushed to the actual database.

# Changes to the database, either through insert or update statements, need to be saved by explicitly calling commit(). This requirement gives an application an opportunity to make several related changes together, so they are stored atomically instead of incrementally, and avoids a situation where partial updates are seen by different clients connecting to the database simultaneously.

# Data within the same conn is consistent, insert only affects other connections after commit()

def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name, description from project')
    for name, desc in cursor.fetchall():
        print('  ', name)


with sqlite3.connect(db_filename) as conn1:
    show_projects(conn1)

    cursor1 = conn1.cursor()
    cursor1.execute("""
    insert into project (name, description, deadline)
    values ('virtualenvwrapper', 'Virtualenv Extensions',
            '2011-01-01')
    """)

    print('\nAfter changes in conn1:')
    show_projects(conn1)

    # Select from another connection, without committing first
    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        show_projects(conn2)

    # Commit then select from another connection
    conn1.commit()
    print('\nAfter commit:')
    with sqlite3.connect(db_filename) as conn3:
        show_projects(conn3)


'''
sql functions
'''
# https://pymotw.com/3/sqlite3/index.html#transactions


def encrypt(s):
    print('Encrypting {!r}'.format(s))
    return codecs.encode(s)

with sqlite3.connect(db_filename) as conn:
    conn.create_function('encrypt', 1, encrypt)
    cursor = conn.cursor()

    query = "select id, details from task"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)


