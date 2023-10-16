from collections import OrderedDict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    birthdays_per_week = OrderedDict(
        [
            ("Monday", []),
            ("Tuesday", []),
            ("Wednesday", []),
            ("Thursday", []),
            ("Friday", []),
        ]
    )

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        birthday_weekday = birthday_this_year.strftime("%A")

        if delta_days <= 7:
            if birthday_weekday not in birthdays_per_week.keys():
                birthdays_per_week["Monday"].append(name)
            else:
                birthdays_per_week[birthday_weekday].append(name)

    for day in birthdays_per_week.keys():
        if len(birthdays_per_week[day]):
            print(f"{day}: {', '.join(birthdays_per_week[day])}")

    return birthdays_per_week


user = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 21)}]
res = get_birthdays_per_week(user)
