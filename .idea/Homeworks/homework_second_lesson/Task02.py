from datetime import datetime, timedelta

def date_range (start_date, end_date):
    dates = []
    try:
        start_date = datetime.strptime(start_date, "%Y.%m.%d")
        end_date = datetime.strptime(end_date, "%Y.%m.%d")
        while start_date <= end_date:
                dates.append (start_date.strftime("%Y.%m.%d"))
                start_date += timedelta(days=1)
    except:
        return dates
    return dates

start = "2002.02.02"
end = "2002.02.05"
print(date_range(start, end))