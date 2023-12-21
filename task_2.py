'''Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
 На вход будет подаваться дата в формате "день.месяц.год". 
 Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
'''

from sys import argv
import re
from datetime import date
import logging

FORMAT = '{levelname:<8} - {asctime}  \nВ модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         '\nзаписала сообщение: {msg}\n'

logging.basicConfig(filename='Logs/data.log', format=FORMAT, style='{',
                    encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(f'Провверка,парсинг даты ')


def is_leap(year: int):
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))


def valid(full_date: str):
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        logger.error(f'Ошибка: что-то напутано с годами, днями и месяцами\n{full_date}')
        return False
    if month in (4, 6, 9, 11) and date > 30:
        logger.error(f'Ошибка: что-то напутано с днями в месяце\n{full_date}')
        return False
    if month == 2 and is_leap(year) and date > 29:
        logger.error(f'Ошибка: в феврвле 29 дней в высокосный год, проверте, что ввели\n{full_date}')
        return False
    if month == 2 and not is_leap(year) and date > 28:
        logger.error(f'Ошибка: в феврвле 28 дней в году, проверте, что ввели\n{full_date}')
        return False
    logger.info(f'Такая дата существует\n{full_date}')
    return True


date_to_prove = ('12.12.1596', '31.4.1269', '25.23.1458', 12.48, 'hh,h,hhhh', True, 'ghhhjkkk', bool, 15, '45.10.1598')
for elem in date_to_prove:
    try:
        if len(argv) > 1:
            print(valid(argv[1]))
        else:
            print(valid(str(elem)))
    except ValueError:
        logger.critical(f'Ошибка: не правильный формат ввода данных\n {date_to_prove}\n{elem} ')
