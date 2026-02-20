from zoneinfo import ZoneInfo
import pytz

from datetime import datetime, date, time

timeFormat = "%Y-%m-%dT%H-%M-%S%z"
tz = ZoneInfo("America/New_York")
time_zone = pytz.timezone("America/New_York")
print("time zone: ", time_zone)
print("local: ", time_zone.localize(datetime.now()))

fromDate = datetime(2026, 2, 1, 0, 0, 0, tzinfo=tz)
print("fromDate: ", fromDate)
print (type(fromDate))
fromDtStr = str(fromDate.strftime(timeFormat))
print ("fromDtStr type: ", type(fromDtStr))
print("fromDtStr: ", fromDtStr)

toDate = datetime(2026, 2, 18, 23, 59, 59, tzinfo=tz)
toDateStr = toDate.strftime(timeFormat)
print("toDateStr: ", toDateStr)

print ("tz: ", tz.fromutc(fromDate).strftime(timeFormat))

fDate = "2026-02-18"
day_begin = "T00:00:00"
day_end = "T23:59:59"
frmDate = fDate + day_begin
toDate = fDate + day_end
# toDate = toDate + day_end+tz.fromutc()
fromDate = datetime.fromisoformat(frmDate)
print ("lower: ",type(fromDate))
fromDtStr = fromDate.strftime(timeFormat)
print("lower: fromDtStr: ", fromDtStr)

fromDate = fromDate.replace(" ", "T")

from_date = fromDate.replace(tzinfo=tz)

toDate = datetime.fromisoformat(toDate)

# fromDate = date.fromisoformat("2021-02-18")
fromTime = time.fromisoformat("00:00:00")
toTime = time.fromisoformat("23:59:59")

# fromDate = datetime.combine(fromDate, fromTime) + tz
# toDate = datetime.combine(toDate, toTime)
print (fromDate)
print ("from_date: ", from_date)
print (toDate)
