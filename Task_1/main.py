from birthdays import get_birthdays_per_week as birthdays
from datetime import datetime

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 12, 4)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 12, 10)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 12, 7)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Mila Jovovich", "birthday": datetime(1975, 12, 15)},
    {"name": "Stephen King", "birthday": datetime(1947, 9, 21)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)}
    ]

for day, names in birthdays(users).items():
        print(day + ': ' + ', '.join(names))
