import psycopg2

connection_parameters = {
    "host": "localhost",
    "database": "car_manufactures",
    "user": "pp2_admin",
    "password": "pp2_admin",
    "port": "5432"
}

# sql_instruction_safe = """ALTER TABLE car_manufactures ADD id SERIAL UNIQUE NOT NULL;"""
sql_instruction_safe = """ALTER TABLE car_manufactures ADD PRIMARY KEY (id);"""


with psycopg2.connect(**connection_parameters) as connection:
    with connection.cursor() as cursor:
        cursor.execute(sql_instruction_safe)
    connection.commit()