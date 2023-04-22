from datetime import datetime, timedelta

weekdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday'
}

result = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': []
}


def period_of_check():
    date_now = datetime.now().date()
    this_monday = date_now - timedelta(date_now.weekday())
    start = this_monday + timedelta(days=5)
    end = this_monday + timedelta(days=11)
    return [start, end]


def get_birthdays_per_week(users: list) -> None:
    period = period_of_check()
    for diction in users:
        for key, value in diction.items():
            birthday_now_year = datetime(datetime.now().year, value.month, value.day).date()
            week_num = birthday_now_year.weekday()
            if period[1] >= birthday_now_year >= period[0] and week_num < 5:
                result[weekdays[week_num]].append(key)
            elif period[1] >= birthday_now_year >= period[0] and week_num >= 5:
                result[weekdays[0]].append(key)
    for key, value in result.items():
        print(key, ', '.join(value), sep=': ')

