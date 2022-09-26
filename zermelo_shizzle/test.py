import calendar
import datetime

# calculates unix timestamps to normal and THEN calculates yesterday
# this is a demonstration how useful unix timestamps can be

date_today = datetime.datetime.utcnow()
print(date_today)
today_utc_time = calendar.timegm(date_today.utctimetuple())
ldate_today = list(str(date_today))
ldate_yesterday = list(str(date_today))
ldate_yesterday[9] = int(ldate_today[9]) - 1
print(ldate_yesterday)
