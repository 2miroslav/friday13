from datetime import date, timedelta, datetime


def friday_13_in_year(y):
    day = date(y, 1, 1)
    end = date(y, 12, 31)
    one_day = timedelta(days=1)
    while day < end:
        if day.weekday() == 4 and day.day == 13:
            yield day
        day += one_day


def friday_13_from():
    now = datetime.now()
    day = date(now.year, now.month, now.day)
    end = date(now.year, 12, 31)
    one_day = timedelta(days=1)
    while day < end:
        if day.weekday() == 4 and day.day == 13:
            yield day
        day += one_day


year = input("Zadajte rok pre ktorý chcete vypísať piatok 13: ")
print("Pre zadaný rok sú tieto piatky 13:")
print([str(d) for d in friday_13_in_year(int(year))])

print("Oddneska budú tento rok ešte nasledújúce piatky 13:")
print([str(d) for d in friday_13_from()])
