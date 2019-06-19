#encoding=utf-8
from datetime import datetime

now = datetime.now()
# python REPL
print now
print [now]  #放在Set list...物件中會是REPR
print {now}
print {'k1': now}
print (now,)
print(now)
print [str(now)] #放在物件中 要自行轉換str