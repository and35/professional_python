from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

latam = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {latam}')

usa = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {usa}')

random_format = my_datetime.strftime('año %Y mes %m día %d')
print(f'Formato random: {random_format}')

formato_utc = datetime.utcnow()
print(f'Formato UTC: {formato_utc}')

import datetime 
# uses of delta
delta = datetime.timedelta(minutes=20)
#si no se cumple con el formato lanzara un ValueError
fecha_hora = datetime.datetime.strptime('2021-09-29 21:30:00' , '%Y-%m-%d %H:%M:%S' )
resultato_delta = fecha_hora+delta
print(resultato_delta) #2021-09-29 21:50:00

# how to check the time in an specific city 
import pytz
from datetime import datetime

fmt = '%Y-%m-%d %H:%M:%S %Z%z'
# Indian Standard Time
tz_india = pytz.timezone('Asia/Kolkata')
ist_local = tz_india.localize(datetime.now())
print("Indian Standard Time::", ist_local.strftime(fmt))