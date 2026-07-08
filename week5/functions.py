import psycopg2
from connection_parameters import connection_parameters

# sql_instruction_safe = """SELECT power(12, 2);"""
# sql_instruction_safe = """CREATE OR REPLACE FUNCTION add_numbers(a INT, b INT)
# RETURNS INT AS $$
# BEGIN
#     RETURN a + b;
# END;
# $$ LANGUAGE plpgsql;"""

# sql_instruction_safe = """CREATE OR REPLACE FUNCTION german_manufacture_check(country VARCHAR)
# RETURNS BOOLEAN
# LANGUAGE plpgsql
# AS $$
# DECLARE
#     result BOOLEAN;
# BEGIN
#     IF country = 'Germany' THEN
#         result := true;
#     ELSE 
#         result := false;
#     END IF;
#     RETURN result;
# END;
# $$;"""

sql_instruction_safe = """CREATE OR REPLACE FUNCTION print_japan_manufactures()
RETURNS TABLE (name VARCHAR, foundation_year INT, country VARCHAR, id INT)
LANGUAGE sql
AS $$
SELECT ALL * FROM car_manufactures WHERE country = 'Japan';
$$;"""

sql_instruction = """SELECT print_japan_manufactures();"""
sql = """SELECT *, german_manufacture_check(country) FROM car_manufactures;"""

values = ('Japan',)


with psycopg2.connect(**connection_parameters) as connection:
    with connection.cursor() as cursor:
        cursor.execute(sql)
        # cursor.execute(sql_instruction)
        result = cursor.fetchall()
    connection.commit()
print(result)