import psycopg2

connection_parameters = {
    "host": "localhost",
    "database": "car_manufactures",
    "user": "pp2_admin",
    "password": "pp2_admin",
    "port": "5432"
}

with psycopg2.connect(**connection_parameters) as connection:
    with connection.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS car_manufactures (name VARCHAR(20) NOT NULL, foundation_year INTEGER NOT NULL, country VARCHAR(20) NOT NULL);")
    connection.commit()
