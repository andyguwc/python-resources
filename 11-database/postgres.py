
##################################################
# Postgres Setup
##################################################

# https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb
'''
setup 
'''
$ brew install postgresql
# make sure postgres starts everytime the computer start

$ pg_ctl -D /usr/local/var/postgres start && brew services start postgresql


'''
common commands
'''
# https://github.com/andyguwc/go-resources/blob/master/08-databases/postgres/postgres.md

# # databases
# \l 
# \c <database name>

# # tables 
# \d 
# \d <table name>


# # users
# select current_user
# \du

# CREATE USER abc WITH PASSWORD 'password'
# CREATE ROLE abc with LOGIN PASSWORD 'password'

# GRANT ALL PRIVILEGES ON DATABSE company to abc 

# ALTER ROLE abc CREATEDB; 

# # sequence 

# postgres=# CREATE ROLE patrick WITH LOGIN PASSWORD 'Getting started'; 

# login not as root user but as another user
# psql postgres -U patrick

# CREATE DATABASE super_awesome_application;
# GRANT ALL PRIVILEGES ON DATABASE super_awesome_application TO patrick; postgres=> \list 
# \connect super_awesome_application 
# \dt 
# \q



##################################################
# UI Tools - Pgadmin and Postico 
##################################################


##################################################
# Running Postgres in a Docker Container 
##################################################
# docker-compose.yaml

# https://linuxhint.com/run_postgresql_docker_compose/
# with just docker itself https://severalnines.com/database-blog/deploying-postgresql-docker-container

version:'3.7'
services:
    database:
        image: postgres:10.6
        ports:
            - "5440:5432"
    environment:
        - POSTGRES_USER=sample
        - POSTGRES_PASSWORD=sample 
        - POSTGRES_DB=sample 
    volumes:
        - sampledb:/var/lib/postgresql/data
    networks:
        - sample 
volumes:
    sampledb:
networks:
    sample:
        driver: bridge 
