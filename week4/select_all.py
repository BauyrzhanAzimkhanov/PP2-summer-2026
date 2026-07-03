import psycopg2

import psycopg2

connection_parameters = {
    "host": "localhost",
    "database": "car_manufactures",
    "user": "pp2_admin",
    "password": "pp2_admin",
    "port": "5432"
}

table_name = "car_manufactures"

sql_instruction = f"""SELECT ALL * FROM {table_name};"""

with psycopg2.connect(**connection_parameters) as connection:
    with connection.cursor() as cursor:
        cursor.execute(sql_instruction)
        result = cursor.fetchall()
        column_names = []
        for i in cursor.description:
            column_names.append(i[0])
    connection.commit()
print(len(result), "rows in result", "\n",column_names, "\n", result)