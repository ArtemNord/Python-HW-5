# Создайте программу для игры в ""Крестики-нолики"".

# desk = [['_', '_', '_'],
#         ['_', '_', '_'], 
#         ['_', '_', '_']]

# s = ''
# stop = False
# for i in range(9):
#     if stop == True:
#         break
#     if i % 2 == 0:
#         print('Ходит игрок 1')
#         j = int(input('Введите номер строки (от 1 до 3): '))
#         k = int(input('Введите номер столбца (от 1 до 3): '))
#         s = '0'
#         desk[j - 1][k - 1] = s
#         print(desk)
#     else:
#         print('Ходит игрок 2')
#         j = int(input('Введите номер строки (от 1 до 3): '))
#         k = int(input('Введите номер столбца (от 1 до 3): '))
#         s = 'X'
#         desk[j - 1][k - 1] = s
#     for a in range(3):
#         if desk[a][0] == desk[a][1] == desk[a][2] and desk[a][0] != '*':
#             winner_s = desk[a][0]
#             stop = True
#             break
#         elif desk[0][a] == desk[1][a] == desk[2][a] and desk[0][a] != '*':
#             winner_s = desk[0][a]
#             stop = True
#             break
#     if desk[0][0] == desk[1][1] == desk[2][2] and desk[0][0] != '*':
#             winner_s = desk[0][0]
#             stop = True
#     elif desk[0][2] == desk[1][1] == desk[2][0] and desk[0][a] != '*':
#             winner_s = desk[0][2]
#             stop = True

# if winner_s == '0':
#     print('Победил игрок 1')
# elif winner_s == 'X':
#     print('Победил игрок 2')
# else:
#     print('Ничья')
    
# print(desk[0])
# print(desk[1])
# print(desk[2])


#-----------------------------------

# 2(Кретиски-нолики)

def input_position():
    row = int(input('Введите номер строки(1-3): '))
    while row < 1 or row > 3:
        row = int(input('Введите номер строки(1-3): '))

    columns = int(input('Введите номер стобца(1-3): '))
    while columns < 1 or columns > 3:
        columns = int(input('Введите номер строки(1-3): ')) 
    
    return row, columns


def check(array):
    if array[0][0] == array[1][0] == array[2][0] != '*':
        return f'Выиграл {array[0][0]}'
    elif array[0][1] == array[1][1] == array[2][1] != '*':
        return f'Выиграл {array[0][1]}'
    elif array[0][2] == array[1][2] == array[2][2] != '*':
        return f'Выиграл {array[0][2]}'
    elif array[0][0] == array[0][1] == array[0][2] != '*':
        return f'Выиграл {array[0][0]}'
    elif array[1][0] == array[1][1] == array[1][2] != '*':
        return f'Выиграл {array[1][0]}'
    elif array[2][0] == array[2][1] == array[2][2] != '*':
        return f'Выиграл {array[2][0]}'
    elif array[0][0] == array[1][1] == array[2][2] != '*':
        return f'Выиграл {array[0][0]}'
    elif array[0][2] == array[1][1] == array[2][0] != '*':
        return f'Выиграл {array[2][0]}'
    return None


array = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

value = 'X'
i = 0
flag = True
while i < 9 and flag:
    print('\n'.join(['\t'.join(i) for i in array]))
    if i % 2 == 0:
        print('Сейчас ходят крестики')
        value = 'X'
    else:
        print('Сейчас ходят нолики')
        value = '0'
    row, columns = input_position()

    if array[row - 1][columns - 1] != '*':
        print('Эта позиция занята')
        row, columns = input_position()
    
    array[row - 1][columns - 1] = value
    result = check(array)
    if result:
        print(result)
        flag = False
    
    i += 1
