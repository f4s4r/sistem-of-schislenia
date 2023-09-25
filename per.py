listforCC = [str(x) for x in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']  # список с значениями цифр


def perevod(x, osn):  # фукнция переводит число x с СС с основанием y
    new = ''
    while x > 0:
        new = listforCC[x % osn] + new
        x //= osn
    return new


def obrperevod(x, osn):  # функция переводит x в десятичную СС из osn СС
    new = 0
    x = str(x)
    x = x[::-1]
    for i in range(len(x)):
        new += listforCC.index(x[i]) * osn ** i
    return new


def summ(osn, x, y, oper):  # "операция"  чисел x и y по основанию osn
    n1 = int(obrperevod(x, osn))
    n2 = int(obrperevod(y, osn))
    itog = 0
    if oper == '*':
        itog = n1 * n2
    elif oper == '+':
        itog = n1 + n2
    elif oper == '-':
        itog = n1 - n2
    return perevod(itog, osn)


vetv = input('---Вы хотите перевести число в какую-либо СС от 2 до 16 -> [P] \n---Сделать какую-либо операцию над числами в СС от 2 до 16 -> [O]\n---Перевести из какой-либо СС от 2 до 16 в десятичную? -> [D]\n')

if vetv == 'P' or vetv == 'p':
    n1 = int(input('Введите число: '))
    osn1 = int(input('Введите основание СС: '))
    if osn1 < 2 or osn1 > 16:
        exit('Неверное основание СС')
    print(perevod(n1, osn1))

elif vetv == 'O' or vetv == 'o':
    osn1 = int(input('Введите основание СС: '))
    if osn1 < 2 or osn1 > 16:
        exit('Неверное основание СС')
    x1 = input('Введите первое число: ')
    y1 = input('Введите второе число: ')
    oper1 = input('Введите операцию("+", "-", "*"): ')
    print(summ(osn1, x1, y1, oper1))

elif vetv == 'D' or vetv == 'd':
    osn1 = int(input('Введите основание СС: '))
    if osn1 < 2 or osn1 > 16:
        exit('Неверное основание СС')
    x1 = input('Введите число: ')
    print(obrperevod(x1, osn1))

else:
    print('Неправильный ввод.')
