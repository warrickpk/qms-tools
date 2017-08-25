import pandas_datareader.data as web
import datetime

start = datetime.datetime(2010, 1, 1)
end = datetime.date(2017, 8, 25)
f = web.DataReader("F", 'yahoo', start, end)

print(f['Close'])
