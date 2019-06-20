import pandas as pd
import pandas_datareader.wb as wb

data1 = wb.download(
    indicator='SE.PRM.TENR',
    country=['all'],
    start='2002',
    end='2016'
)

print type(data1)
print data1.shape