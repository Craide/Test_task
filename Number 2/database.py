import psycopg2
from psycopg2 import Error
from main import records

try:
    connection = psycopg2.connect(user="postgres", #Вставить корректные данные
                                  password="Prometei1905",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Test_q")
    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE IF NOT EXISTS abonents 
                            (
	                        abonent BIGINT NOT NULL,
	                        region_id INT NOT NULL,
    	                    dttm TIMESTAMP NOT NULL
                            );'''
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

    for i in range(len(records)):
        insert_query = f'''INSERT INTO abonents
                            VALUES 
                            ({records[i][0]}, {records[i][1]}, '{records[i][2]}')'''
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
