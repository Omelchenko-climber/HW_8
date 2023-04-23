from datetime import datetime, timedelta


result = {          # result what would be printed after executing the function
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': []
}


def period_of_check() -> list:          # after executing this function we get period from saturday to friday next week
    date_now = datetime.now().date()
    start = date_now - timedelta(date_now.weekday()) + timedelta(days=5)
    end = date_now - timedelta(date_now.weekday()) + timedelta(days=11)
    return [start, end]


def get_birthdays_per_week(users: list) -> None:            # This function give list of users with weekdays of their birthdays
    start, end = period_of_check()
    for diction in users:
        while diction:
            key,value = diction.popitem()
            birthday_now_year = datetime(datetime.now().year, value.month, value.day).date() # here we get birthday of user with this year
            week_num = birthday_now_year.weekday() # number of weekday from 0 to 6
            weekday= birthday_now_year.strftime('%A') # here we get name of the day of the week
            if end >= birthday_now_year >= start and week_num < 5: # we check if this date meets with requirements
                result[weekday].append(key) # we write the date to the result
            elif end >= birthday_now_year >= start and week_num >= 5: # we check if this date meets with requirements
                result['Monday'].append(key) # we write the date to the result
    for key, value in result.items():
        print(key, ', '.join(value), sep=': ') # we print the result to console