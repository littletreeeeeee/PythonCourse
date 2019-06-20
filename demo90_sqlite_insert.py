#encoding=utf-8
import sqlite3
import time

connection1 = sqlite3.connect('db\\sqlite3_lab1.sqlite')

employees = [{'NAME': 'Mark', "AGE": 38, 'DEPT': 1, 'ADDR': 'Taipei'},
             {'NAME': 'John', "AGE": 43, 'DEPT': 2, 'ADDR': 'Hsinchu'},
             {'NAME': 'James', "AGE": 47, 'DEPT': 1, 'ADDR': 'Taipei'}]

INSERT_DML = "INSERT INTO EMPLOYEE(NAME, AGE, DEPT, ADDRESS) VALUES(?,?,?,?)"

start_time = time.time()

for i in range(1000):
    for e in employees:
        connection1.execute(INSERT_DML, (e['NAME'], e['AGE'], e['DEPT'], e['ADDR']));
        # connection1.commit() #33秒
    # connection1.commit() # 11.49
connection1.commit() # 0.026  越少Commit速度越快
connection1.close()
end_time = time.time()
print ('total:', end_time - start_time)
