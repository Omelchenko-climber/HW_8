from datetime import datetime, timedelta


result = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': []
}


def period_of_check():
    date_now = datetime.now().date()
    start = date_now - timedelta(date_now.weekday()) + timedelta(days=5)
    end = date_now - timedelta(date_now.weekday()) + timedelta(days=11)
    return [start, end]


def get_birthdays_per_week(users: list) -> None:
    start, end = period_of_check()
    for diction in users:
        while diction:
            key,value = diction.popitem()
            birthday_now_year = datetime(datetime.now().year, value.month, value.day).date()
            week_num = birthday_now_year.weekday()
            weekday= birthday_now_year.strftime('%A')
            if end >= birthday_now_year >= start and week_num < 5:
                result[weekday].append(key)
            elif end >= birthday_now_year >= start and week_num >= 5:
                result['Monday'].append(key)
    for key, value in result.items():
        print(key, ', '.join(value), sep=': ')