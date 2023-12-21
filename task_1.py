'''
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens),
 которая проверяет все возможные пары ферзей.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
 Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
'''


from itertools import combinations
import logging

FORMAT = '{levelname:<8} - {asctime}  \nВ модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         '\nзаписала сообщение: {msg}\n'

logging.basicConfig(filename='Logs/log.log', format=FORMAT, style='{',
                    encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(f'Шахматы')

EIGHT_QUEENS = 8


def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    # Проверяем все возможные пары ферзей
    # try:
    if len(queens) == EIGHT_QUEENS:
        filtered_queens = [queen for queen in queens if len(queen) == 2]
        if len(filtered_queens) != len(queens):
            # raise ValueError("Ошибка: размер картежа не равен 2")
            logger.error(f" размер картежа не равен 2\n{queens}")
            return False
        for q1, q2 in combinations(queens, 2):
            if is_attacking(q1, q2):
                logger.info(f'\n Ферзи бьют друг друга при такой расстановке\n{queens}')
                return False
        logger.info(f'Ферзи раставлены верно при такой расстановке\n{queens}')
        return True
    else:
        logger.error(f'что-то в вводных данныох не верно\n{queens}')


if __name__ == '__main__':
    try:

        queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (3, 7), (5)]
        check_queens(queens)
        # print(check_queens(queens))
        queens = [(1, 2), (2, 4), (3, 6), (5, 8), (6, 1), (5, 3), (7, 7), (8, 5)]
        check_queens(queens)
        # print(check_queens(queens))
        queens = [(1, 2), (2, 4), (3, 6), (4, 8), (16, 1), (5, 3), (7, 7), (8, 5)]
        check_queens(queens)
        # print(check_queens(queens))
        queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6, 5), (8, 8)]
        check_queens(queens)
        # print(check_queens(queens))
        queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (5, 6), (6, bool)]
        check_queens(queens)
        # print(check_queens(queens))
    except TypeError:
        logger.critical(f'что-то в вводных данныох не верно\n{queens}')
