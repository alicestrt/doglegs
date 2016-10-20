import datetime as dt


DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


def next_days(search_days, starting_date):
    """Datetime objects for all 'search_days' since 'starting_date'."""
    days = [next_day(day, starting_date) for day in search_days]
    latest_day = days[-1]
    if latest_day is None:
        return list(filter(None, days))
    next_date = dt.date(
        day=days[-1].day+1,
        month=starting_date.month,
        year=starting_date.year
    )
    return days + next_days(search_days, next_date)


def next_day(search_day, starting_date):
    """Datetime object for 'search_day' since 'starting_date'."""
    try:
        idx = starting_date.day + 1
        while True:
            day = dt.date(
                day=idx,
                month=starting_date.month,
                year=starting_date.year
            )
            if day.ctime().split()[0] == search_day:
                return day
            idx += 1
    except ValueError:
        pass
