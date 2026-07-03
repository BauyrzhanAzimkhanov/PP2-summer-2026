import psycopg2

connection_parameters = {
    "host": "localhost",
    "database": "car_manufactures",
    "user": "pp2_admin",
    "password": "pp2_admin",
    "port": "5432"
}

sql_instruction_safe = """UPDATE car_manufactures SET name = %s, foundation_year = %s WHERE id = %s;"""

values = ("AUDI", 1909, 2)

with psycopg2.connect(**connection_parameters) as connection:
    with connection.cursor() as cursor:
        cursor.execute(sql_instruction_safe, values)
    connection.commit()