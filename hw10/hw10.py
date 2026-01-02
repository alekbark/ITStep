import datetime
import locale
import calendar


# Домашнее задание №10: Работа с датой и временем. Файлы и каталоги
# Задание №1

# date = datetime.date(2015, 6, 16)
# week_number = date.isocalendar().week
#
# print(week_number)

# Задание №2

# locale.setlocale(locale.LC_TIME, 'ru_RU')
# year = 2015
# week = 50
# date = datetime.date.fromisocalendar(year, week, 1)
# result = datetime.datetime.combine(date, datetime.time())
# formatted = result.strftime('%a %d %B %H:%M:%S %Y')
# print(formatted)

# Задание №3

# year = 2015
# sundays = []
# date = datetime.date(year,1,1)
#
# while date.year == year:
#     if date.weekday() == 6:
#         sundays.append(date)
#     date += datetime.timedelta(days=1)
#
# for d in sundays:
#     print(d.strftime("%A %d %B %Y"))

# Задание №4

# def add_years(date_obj, years):
#     try:
#         return date_obj.replace(year=date_obj.year + years)
#     except ValueError:
#         return date_obj.replace(year=date_obj.year + years, month=3, day=1)
#
# print(add_years(datetime.date(2015, 1, 1), -1))
# print(add_years(datetime.date(2015, 1, 1), 0))
# print(add_years(datetime.date(2015, 1, 1), 2))
# print(add_years(datetime.date(2000, 2, 29), 1))

# Работа с датой и временем
# Задание №1

# local_time = datetime.datetime.now()
# utc_time = datetime.datetime.now(datetime.timezone.utc)
#
# print(f"Местное время: {local_time}")
# print(f"Время по Гринвичу: {utc_time}")

# Задание №2

# date1 = datetime.date(2015, 1, 1)
# date2 = datetime.date(2017, 6, 25)
#
# delta = date2 - date1
#
# print(abs(delta.days))

# Задание №3

# dt1 = datetime.datetime(2015, 6, 16, 12, 30, 0)
# dt2 = datetime.datetime(2022, 2, 25, 18, 45, 20)
#
# delta = dt2 - dt1
#
# total_seconds = int(delta.total_seconds())
# days = total_seconds // 86400
# hours = (total_seconds % 86400) // 3600
# minutes = (total_seconds % 3600) // 60
# seconds = total_seconds % 60
#
# print(f"Дни: {days}\nЧасы: {hours}\nМинуты: {minutes}\nСекунды: {seconds}")

# Задание №4

# year = 2015
# month = 12
#
# cal = calendar.HTMLCalendar(firstweekday=0)
# html_calendar = cal.formatmonth(year, month)
#
# with open("calendar.html", "w", encoding="utf-8") as f:
#     f.write(html_calendar)


