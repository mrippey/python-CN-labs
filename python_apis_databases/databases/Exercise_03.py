'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''

import sqlalchemy 
from pprint import pprint 

password = ''.encode('utf-8')
engine = sqlalchemy.create_engine(f'mysql+pymysql://root:password@localhost/sakila')

connection = engine.connect()

metadata = sqlalchemy.MetaData()


film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.update(film).values(rental_duration = 10).where(film.columns.rental_duration > 150)

result_proxy = connection.execute(query)

pprint(result_proxy)
