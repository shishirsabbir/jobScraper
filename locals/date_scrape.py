import re
from datetime import datetime, date



# creating the date module

def getDate(posted_date):

    # regex format: (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4}
    # format: Jun 10, 2023
    # 3 day timestamp: 259200 milliseconds
    pattern_month = r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'
    pattern_day = r'\d{1,2}'
    pattern_year = r'\d{4}'

    month_dict = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }

    match_month = re.search(pattern_month, posted_date)
    month = match_month.group().replace(' ', '')
    month_num = month_dict.get(month.casefold())

    match_day = re.search(pattern_day, posted_date)
    day = match_day.group().replace(' ', '')

    match_year = re.search(pattern_year, posted_date)
    year = match_year.group().replace(' ', '')

    date_obj = datetime(int(year), int(month_num), int(day))

    date_str = date_obj.strftime('%Y-%m-%d')

    time_stm = date_obj.timestamp()

    return (int(time_stm), date_str)





# get today's timestamp

def lastStamp():
    now_date = date.today()

    today_obj = datetime.strptime(str(now_date), '%Y-%m-%d')
    today_stamp = today_obj.timestamp()
    last_stamp = int(today_stamp) - 259200

    return int(last_stamp)