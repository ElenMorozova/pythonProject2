# Задание 1
name = 'Elen'
print(name)
age = 18
print(age)
Film1 = "Д'Артоньян и три мушкетера"
print (Film1)

user_name = input('Ваше имя ')
print('Привет, ', user_name, '!')
user_age = input('Ваш возраст ')
print(user_name, ',тебе', user_age, ', значит, ты можешь получить водительские права')

product = 'яблоки'
price = 150
print('наименование:', product, 'цена:', price)
print('наименование: %s цена: %d' %(product, price))
print('наименование: {} цена: {}'.format(product, price))
print(f'наименование: {product} цена: {price}')

# Задание 2
time_second = int(input('Укажите время в секундах: '))
hour = time_second // 3600 # определяем количество часов
min = time_second % 3600 # определяем остаток минут
minute = min // 60 # определяем количество минут
second = min % 60 # определяем остаток - количество секунд
print('{:02}:{:02}:{:02}'.format(hour, minute, second))

# Задание 3
number = int(input('Введите число от 1 до 9 '))
print(number + number * 11 + number * 111)
# или
number = int(input('Введите число от 1 до 9 '))
result = number + number * 11 + number * 111
print(result)

# Задание 4
n = int(input('Введите целое положительное число: '))
print(n)
m = 0
while n > 0:
    a = n % 10 # остаток от деления на 10, последняя цифра в числе
    n = n // 10
    if a >= m:
        m = a
print(m)

# Задание 5
revenue = int(input('Выручка за месяц: '))
expenses = int(input('Расходы за месяц: '))
profit = (revenue - expenses)
if revenue > expenses:
    print('Фирма получила прибыль в сумме', profit)
    profitability = (profit / revenue)
    print('Рентабельность: ', round(profitability, 2))
    number_employees = int(input('Численность сотрудников фирмы: '))
    print('Прибыль фирмы в расчете на 1 сотрудника: ', round(profit / number_employees, 2))
else:
    print('Фирма получила убыток в сумме', (expenses - revenue))

# Задание 6
a = int(input('Результат в первый день, км: '))
b = int(input('Требуемый общий результат, км: '))
с = 0 # количество итераций в цикле
while a < b:
    a += a / 10
    с += 1
else:
    с+= 1
    print(f'Спортсмен достигнет результата {b} км на {с} день.')





