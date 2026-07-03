import psycopg2
from psycopg2.extras import execute_values
from connection_parameters import connection_parameters

sql_instruction_safe = """INSERT INTO car_manufactures 
(name, foundation_year, country) VALUES %s;"""

values = [("Nissan", 1933, "Japan"),("Ford", 1903, "USA"),("Toyota", 1937, "JAPAN"),("Vauxhall", 1857, "UK")]

with psycopg2.connect(**connection_parameters) as connection:
    with connection.cursor() as cursor:
        execute_values(cursor, sql_instruction_safe, values)
    connection.commit()