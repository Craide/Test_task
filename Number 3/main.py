import datetime
from random import randint
records = []

for i in range(1000):
    item_id = randint(1,100)
    item_name = f'Товар {item_id}'
    item_price = randint(1,100000)/100
    created_dttm = datetime.datetime(randint(2000,2023), randint(1,11), randint(1,21), randint(0,23))
    records += [[item_id, item_name, item_price, created_dttm]]

print('Данные успешно подготовлены')
