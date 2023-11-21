import datetime
from random import randint
records = []
titles = ['Sberbank is the best bank', 'Visa vs Mastercard', 'Visa vs UnionPay', 'Mastercard vs UnionPay', 'Hadoop or Greenplum: pros and cons', 'NFC: wireless payment']
for i in range(1000):
    created_at = datetime.datetime(randint(2000,2022), randint(1,12), randint(1,25), randint(0,23))
    title = titles[i%6]
    records += [[created_at, title]]
print('Данные успешно подготовлены')
