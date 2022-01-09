# Задание № 1
def my_del(a, b):
   res = a / b
   return res
try:
   print(my_del(int(input('Введите число а: ')), int(input('Введите число b: '))))
except ZeroDivisionError:
   print('На ноль делить нельзя!')

# Задание № 2
def team_member(name, last_name, year_of_birth, city, email, phone_number):
    print(name, last_name, year_of_birth, city, email, phone_number)

team_member(name=input('Имя: '), last_name=input('Фамилия: '), year_of_birth=int(input('Год рождения: ')), city=input('Город проживания: '), email=input('email: '), phone_number=int(input('Номер телефона: ')))

# Задание № 3
def my_func (a, b, c):
    li_1 = [a, b, c]
    li_2 = sorted(li_1, reverse=True)
    '''сортируем список по убыванию'''
    li_2.pop()
    '''удаляем первый (наименьший) элемент'''
    res = sum(li_2)
    '''получаем сумму двух оставшихся (наибольших) элементов'''
    print(res)
    return res
my_func(5, 38, 1)

# Задание № 4
def my_func_1 (x, y):
    print(x ** y)
my_func_1 (2, -3)

# Задание № 5
def int_func():
    n = 0
    while True:
        st_lst = input('Введите числа через пробел, для выхода введите stop: ').split()
        for elem in st_lst:
            if elem.lower() == 'stop': # не могу понять, почему вознкает ошибка, если ввожу число и stop
                return
            else:
                st_num = list(map(int, st_lst))
        s = sum(st_num)
        res = n + s
        print(res)
        n = res
int_func()

# Задание № 6
def my_text():
    t_1 = input('Введите текст: ').capitalize()
    print(t_1)
my_text()

def my_text(a):
    print(a.capitalize())
my_text(a=input('Введите текст: '))
'''два способа реализации, но не могу понять, как использовать эту функцию для дальнейшего решения'''

