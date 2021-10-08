print('Введите необходимое для пересчёта в другую систему счисления целое десятичное число: ')
flag = True
while flag:
    try:
        num = int(input())
    except ValueError:
        print('Вы ввели текст, повторите ввод: ')
    else:
        if num < 0:
            print('Введённое число не может быть отрицательным, повторите ввод: ')
        if num >= 0:
            flag = False
print('Введите необходимую систему счисленя:\n')
flag = True
while flag:
    try:
        base = int(input("Base (2-9): "))
    except ValueError:
        print('Ошибка, повторите ввод: ')
    else:
        if not(2 <= base <= 9):
            print('Введена неверная система счисления, повторите ввод: ')
        if 2 <= base <= 9:
            flag = False
newNum = ''
while num > 0:
    newNum = str(num % base) + newNum
    num //= base
print('Готово, ваше число: ')
print(newNum)