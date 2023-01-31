import ntplib
from time import ctime
c = ntplib.NTPClient()
response = c.request('ar.pool.ntp.org', version=3)
a = ctime(response.tx_time)
print(a)