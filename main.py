import random
from marks import Bounds
import csv


def generateMessage(mainText: str, name: str = 'имя') -> str:
    return f'Здравствуйте, {name}!' + '\n\n' + \
           mainText + '\n\n' + \
           'Желаю успехов в следующих заданиях!' + '\n'


def generateMainText(mark: str) -> str:
    mark = mark.strip()
    if mark == '5+':
        rez = fivePlus()
    elif mark == '5' or mark == '5-':
        rez = five()
    elif mark == '4+' or mark == '4' or mark == '4-':
        rez = four()
    elif mark == '3+' or mark == '3' or mark == '3-':
        rez = three()
    else:
        rez = two()
    return rez


def fivePlus() -> str:
    first = ['Отличная работа, Вы прекрасно поработали!', 'Великолепно выполнили задание!', 'Отличная работа, замечания отсутствуют!']
    second = ['Продолжайте в том же духе.', 'Превосходно, ни одной ошибки.']
    return first[int(random.random() * 1e5 % len(first))] + ' ' + second[int(random.random() * 1e5 % len(second))]


def five() -> str:
    first = ['Отличная работа, Вы прекрасно поработали!', 'Замечательная работа, практически нет замечаний.!']
    second = ['Здорово ответили на все вопросы.']
    return first[int(random.random() * 1e5 % len(first))] + ' ' + second[int(random.random() * 1e5 % len(second))]


def four() -> str:
    first = ['Хорошая работа, видно, что освоили тему.', 'Тема освоена, Вы хорошо постарались.']
    second = ['Есть неточности, обратите внимание на мои правки.',
              'В некоторых заданиях присутствуют неточности, обратите внимание на мои правки.',
              'Присутствует некоторое количество недочётов, смотрите мои исправления.'
              ]
    return first[int(random.random() * 1e5 % len(first))] + ' ' + second[int(random.random() * 1e5 % len(second))]


def three() -> str:
    first = ['Неплохая работа, но есть недочёты.', 'К сожалению, не всё получилось решить.']
    second = ['Обратите внимание на мои комментарии, есть неточности.',
              'Обратите внимание на мои исправления и решение авторов.',
              'Если не успеваете, можете писать мне о продлении.',
              'Есть несколько неотправленных задач, если не успеваете, можете писать мне о продлении.']
    return first[int(random.random() * 1e5 % len(first))] + ' ' + second[int(random.random() * 1e5 % len(second))]


def two() -> str:
    first = ['К сожалению, слишком мало получилось решить.', 'К сожалению, много недочётов.']
    second = ['Если не успеваете, можете писать мне о продлении.']
    return first[int(random.random() * 1e5 % len(first))] + ' ' + second[int(random.random() * 1e5 % len(second))]


pupils = []

FLAGMARKS = True
MATHEMATICA = Bounds([40., 32., 24., 12.])

with open('data.txt', 'r', encoding="utf-8") as f:
    for line in f:
        tmp = line.split()
        if FLAGMARKS:
            pupils.append([tmp[0], MATHEMATICA.determineMark(float(tmp[1]))])
        else:
            pupils.append(tmp)

print(pupils)

with open('rez.txt', 'w', encoding="utf-8") as f:
    for item in pupils:
        print(generateMessage(generateMainText(item[1]), item[0]), file=f)
        print(file=f)
