import datetime
from random import randint
records = []

for i in range(1000):
    abonent = randint(1,100)
    region_id = randint(1,10000)
    datetime_to_record = datetime.datetime(randint(2020,2021), randint(8,9), randint(15,17), randint(9,20))
    records += [[abonent, region_id, datetime_to_record]]
print('Данные успешно подготовлены')
