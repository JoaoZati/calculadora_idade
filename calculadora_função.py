"""
>>> validate_date(20, 4, 1994)
True
>>> validate_date(32, 1, 2000)
False
>>> validate_date(31, 4, 2008)
False
>>> validate_date(25, 13, 2000)
False
>>> validate_date(0, 2, 2005)
False
>>> validate_date(5, 0, 2006)
False
>>> validate_date(-1, -1, 2006)
False
>>> validate_date(29, 2, 2000)
True
>>> validate_date(29, 2, 2021)
False
>>> validate_date(29, 2, 2004)
True
>>> validate_date(29, 2, 2100)
False
>>> convert_str_int('20/04/2021')
(20, 4, 2021)
>>> convert_str_int(20)
(0, 0, 0)
>>> convert_str_int('20/05/200/666')
(0, 0, 0)
>>> convert_str_int('-20/06/2021')
(-20, 6, 2021)
>>> convert_str_int('0.5/06/2022')
invalid literal for int() with base 10: '0.5'
(0, 0, 0)
>>> calcular_idade('20/04/1994') # corrigir para dia atual
('8', '5', '27')
>>> calcular_idade('27/09/2020') # corrigir para dia atual
('30', '11', '0')
"""
from datetime import datetime as dt
from datetime import timedelta


def validate_date(day, month, year):
    if day not in (range(1, 32)) or month not in range(1, 13):
        return False

    leap_year = False
    if ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0):
        leap_year = True

    last_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year:
        last_day_list[1] = 29

    for last_day in last_day_list:
        if day > last_day:
            return False

    return True


def convert_str_int(string: str):
    if not isinstance(string, str):
        return 0, 0, 0

    try:
        list_number = string.split('/')
        if len(list_number) != 3:
            return 0, 0, 0
        list_number = [int(i) for i in list_number]
    except Exception as e:
        print(e)
        return 0, 0, 0

    return list_number[0], list_number[1], list_number[2]


def calculate_idade(string_date: str) -> [str, str, str]:
    day, month, year = convert_str_int(string_date)
    today = dt.now()
    try:
        if validate_date(day, month, year):
            birth_day = dt(year, month, day)
            if birth_day > today:
                return ["", "", ""]
            diference = (today - birth_day).days
            years, days = divmod(diference, 365.2425)
            months, days = divmod(days, 30.4375)
            return str(int(days)), str(int(months)), str(int(years))
        return ["", "", ""]
    except Exception as e:
        print(e)
        return ['', '', '']


