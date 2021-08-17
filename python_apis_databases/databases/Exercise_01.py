'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
from pprint import pprint
import sqlalchemy 

mysql_pass = ''.encode('utf-8')
engine = sqlalchemy.create_engine(f'mysql+pymysql://root:mysql_pass@localhost/sakila')

connection = engine.connect()

metadata = sqlalchemy.MetaData()

actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)

join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)

query_tables = sqlalchemy.select([film.columns.film_id, film.columns.title,actor.columns.first_name, actor.columns.last_name]).select_from(join_statement)

result = connection.execute(query_tables)

result_set = result.fetchall()

pprint(result_set)
