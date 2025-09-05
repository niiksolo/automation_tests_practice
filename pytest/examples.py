from db import session
import tables

results = session.query(
    tables.Films.film_id, tables.Films.title
).filter(
    tables.Films.film_id > 100        # поиск по фильтрам
).all

film_ids = session.query(tables.Films.film_id).filter(tables.Films.film_id > 180).subquery()

result = session.query(tables.Films.title).filter(tables.Films.film_id.in_(film_ids)).all()
print(result)
