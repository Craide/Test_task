import datetime
from random import randint
records = []

for i in range(10000):
    customer_id = randint(1,50)
    item_id = randint(1,100)
    item_number = randint(1,20)
    transaction_dttm = datetime.datetime(randint(2000,2023), randint(1,11), randint(1,21), randint(0,23))
    records += [[customer_id, item_id, item_number, transaction_dttm]]

print('Данные успешно подготовлены')
