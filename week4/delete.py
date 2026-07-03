import psycopg2
from connection_parameters import connection_parameters

sql_instruction_safe = """DELETE FROM car_manufactures WHERE id = %s;"""

values = (4,)

with psycopg2.connect(**connection_parameters) as connection:
    with connection.cursor() as cursor:
        cursor.execute(sql_instruction_safe, values)
    connection.commit()