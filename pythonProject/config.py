import mysql.connector

from main import USD, TZS, GBP, KES, EUR,ZAR, date

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rest_api"
)
crsr = mydb.cursor()

# sql = "INSERT INTO currencyexchange (ID,BaseCurreny,DateRequest,TargetCurrency,Amount) VALUES (%s,%s,%s,%s,%s)"
sql = "INSERT INTO currencyexchange (ID,BaseCurreny,DateRequest,TargetCurrency,Amount) VALUES (%s,%s,%s,%s,%s)"
val = [('1','USD', date, 'TZS', USD), ('2', 'GBP', date, 'TZS', GBP), ('3', 'KES', date,'TZS', KES),
       ('4', 'EUR',date,' TZS', EUR)]
crsr.executemany(sql, val)
mydb.commit()
print(crsr.rowcount, "successful")
