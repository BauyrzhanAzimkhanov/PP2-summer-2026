import psycopg2
from connection_parameters import connection_parameters

sql_instruction_safe = """BEGIN TRANSACTION;
INSERT INTO car_manufactures (name, foundation_year, country) VALUES ('Subaru', 1953, 'Japan');
SAVEPOINT my_save;
SELECT ALL * FROM car_manufactures;
INSERT INTO car_manufactures (name, foundation_year, country) VALUES ('Subaru', 1953, 'Japan');
SELECT ALL * FROM car_manufactures;
ROLLBACK TO my_save;
SELECT ALL * FROM car_manufactures;
COMMIT;"""

sql_instruction = """INSERT INTO car_manufactures (name, foundation_year, country) VALUES ('Volvo', 1927, 'Sweden');"""


with psycopg2.connect(**connection_parameters) as connection:
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(sql_instruction)
    # connection.rollback()
    # connection.commit()