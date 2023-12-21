'''Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске, 
в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом, 
что они не находятся на одной вертикали, горизонтали или диагонали.

Список из 4х комбинаций координат сохраните в board_list.'''
import random
from itertools import combinations
import logging
import datetime

FORMAT = '{levelname:<8} - {asctime}  \nВ модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         '\nзаписала сообщение: {msg}\n'

logging.basicConfig(filename='Logs/generate_boards.log', format=FORMAT, style='{',
                    encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(f'4 доски ')


def generate_board():
    # Генерируем случайную доску
    board = []

    for i in range(1, 8 + 1):
        queen = (i, random.randint(1, 8))
        board.append(queen)
    return board


def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True


def generate_boards():
    # Генерируем доски, пока не получим 4 успешные расстановки
    count = 0
    num = 0
    board_list = []
    while count < 4:
        board = generate_board()
        if check_queens(board):
            count += 1
            board_list.append(board)
        num += 1
    logger.info(f'Общее колличество итераций, вариантов\n{num} ')
    logger.info(f'Расстановка ферзей на шахматной доске\n{board_list} ')
    return board_list


start = datetime.datetime.now()
generate_boards()
finish = datetime.datetime.now()
logger.info(f'Время работы программы \n{finish - start} ')
