import psycopg2
from psycopg2 import Error
from main import records

try:
    connection = psycopg2.connect(user="postgres",
                                  password="Prometei1905",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="5")
    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE IF NOT EXISTS posts(
	                            id INT GENERATED ALWAYS AS IDENTITY,
	                            created_at TIMESTAMP,
	                            title varchar(64)
                            );'''
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

    for i in range(len(records)):
        insert_query = f'''INSERT INTO posts (created_at, title)
                            VALUES
                            ('{records[i][0]}', '{records[i][1]}')'''
        cursor.execute(insert_query)
        connection.commit()
    print('Записи добавлены в таблицу')
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
