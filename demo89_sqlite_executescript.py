import sqlite3

connection1 = sqlite3.connect('db\\sqlite3_lab1.sqlite')
print "open db success"
drop_and_create_sql = '''
DROP TABLE IF EXISTS EMPLOYEE;
CREATE TABLE EMPLOYEE
(ID INTEGER PRIMARY KEY,
 NAME TEXT NOT NULL,
 AGE INT NOT NULL,
 DEPT INT,
 ADDRESS CHAR(50)
 );
'''

print "create db"
connection1.executescript(drop_and_create_sql)
connection1.close()

