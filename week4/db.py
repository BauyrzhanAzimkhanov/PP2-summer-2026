import psycopg2

try:
    connection = psycopg2.connect(
        host = "localhost",
        database = "car_manufactures",
        user = "pp2_admin",
        password = "pp2_admin",
        port = "5432"
    )

    cursor = connection.cursor()

    cursor.execute("SELECT version()")
    db_version = cursor.fetchone()
    print(f"Connceted to: {db_version}")

except (Exception, psycopg2.Error) as error:
    print(f"Error happened while connecting to PostgreSQL: {error}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
        print("PostgreSQL connection is closed")