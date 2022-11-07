x = int(input('Введите первое число: '))
expression = input('Выберите операцию (+, -, *, /): ')
y = int(input('Введите второе число: '))

def sum():
    return f"Результат {x+y}"

def minus():
    return f'Результат {x-y}'

def multiplication():
    return f"Результат {x*y}"

def division():
    return f"Результат {x/y}"

def choise():
    while input == 'Нет':
        if expression == '+':
            print(sum())
        elif expression == '-':
            print(minus())
        elif expression == '*':
            print(multiplication())
        elif expression == '/':
            print(division())
        else:
            print('Таких вычислений я не провожу')
    print(input('Продолжить?'))



print (choise())
