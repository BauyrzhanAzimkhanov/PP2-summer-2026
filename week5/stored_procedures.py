import psycopg2
from connection_parameters import connection_parameters

create_stored_procedure = """CREATE OR REPLACE PROCEDURE insert_car_manufacture(new_name IN VARCHAR, new_foundation_year IN INT, new_country IN VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO car_manufactures (name, foundation_year, country) VALUES (new_name, new_foundation_year, new_country);
END;
$$;"""

create_selecting_stored_procedure = """CREATE OR REPLACE PROCEDURE select_car_manufacture(searching_name IN VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT ALL * FROM car_manufactures WHERE name = searching_name;
END;
$$;"""

sql_instruction = """CALL select_car_manufacture(%s);"""

values = ('BMW', )


with psycopg2.connect(**connection_parameters) as connection:
    with connection.cursor() as cursor:
        cursor.execute("DROP PROCEDURE insert_car_manufacture;")
        cursor.execute(create_stored_procedure)
        cursor.execute(create_selecting_stored_procedure)
        cursor.execute(sql_instruction, values)
    connection.commit()
