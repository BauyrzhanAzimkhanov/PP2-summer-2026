import psycopg2

connection_parameters = {
    "host": "localhost",
    "database": "car_manufactures",
    "user": "pp2_admin",
    "password": "pp2_admin",
    "port": "5432"
}

table_name = "car_manufactures"

sql_instruction = f"""INSERT INTO {table_name} 
(name, foundation_year, country) VALUES ('Audi', 1909, 'Germany');"""

sql_instruction_safe = """INSERT INTO car_manufactures 
(name, foundation_year, country) VALUES (%s, %s, %s);"""

values = ("BMW", 1916, "Germany")

with psycopg2.connect(**connection_parameters) as connection:
    with connection.cursor() as cursor:
        cursor.execute(sql_instruction_safe, values)
    connection.commit()