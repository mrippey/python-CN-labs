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


category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)

join_statement = category.join(film_category, film_category.columns.category_id == category.columns.category_id).join(film, film.columns.film_id == film_category.columns.film_id)

query_tables = sqlalchemy.select([film.columns.film_id, film.columns.title,category.columns.name, category.columns.category_id, category.columns.last_update]).select_from(join_statement)


result = connection.execute(query_tables)

result_set = result.fetchall()

pprint(result_set)
