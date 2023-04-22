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


users = [{
    'Bill': datetime(1983, 4, 29).date(),
    'Will': datetime(1983, 4, 24).date(),
    'Bob': datetime(1983, 4, 25).date(),
    'Dug': datetime(1983, 4, 22).date(),
    'Dwane': datetime(1983, 5, 1).date()
},
    {
        'Rob': datetime(1983, 4, 26).date(),
        'Krab': datetime(1983, 4, 27).date(),
        'Jane': datetime(1983, 4, 28).date(),
        'Lane': datetime(1983, 4, 21).date(),
        'Tane': datetime(1983, 4, 23).date(),
        'Kane': datetime(1983, 4, 22).date()
    }]


def period_of_check():
    date_now = datetime.now().date()
    start = date_now - timedelta(date_now.weekday()) + timedelta(days=5)
    end = date_now - timedelta(date_now.weekday()) + timedelta(days=11)
    return [start, end]


def get_birthdays_per_week(users: list) -> None:
    start, end = period_of_check()
    for diction in users:
        for key, value in diction.items():
            birthday_now_year = datetime(datetime.now().year, value.month, value.day).date()
            week_num = birthday_now_year.weekday()
            if end >= birthday_now_year >= start and week_num < 5:
                result[weekdays[week_num]].append(key)
            elif end >= birthday_now_year >= start and week_num >= 5:
                result[weekdays[0]].append(key)
    for key, value in result.items():
        print(key, ', '.join(value), sep=': ')

get_birthdays_per_week(users)