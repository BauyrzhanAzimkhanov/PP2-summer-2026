import psycopg2

connection_parameters = {
    "host": "localhost",
    "database": "car_manufactures",
    "user": "postgres",
    "password": "admin",
    "port": "5432"
}

with psycopg2.connect(**connection_parameters) as connection:
    with connection.cursor() as cursor:
        cursor.execute("CREATE TABLE example_table_1 (my_string VARCHAR(20) NOT NULL);")
        result = cursor.fetchall()

print(result)
