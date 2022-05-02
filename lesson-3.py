1.
def calc():
    try:
        a = float(input("укажите число"))
        b = float(input("укажите число"))
        ab = a / b
        return ab
    except ZeroDivisionError:
        print(f'Ошибка!На ноль делить нельзя')


ab = calc()
print(ab)

2.
def personal_data(**kwargs):
    return ";".join(kwargs.values())


print(personal_data(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '), ))

3.
def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших чисел равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(int(input('Число 1:')), int(input('Число 2:')), int(input('Число 3:')), )

4.
def my_func():
    x = int(input("действительное положительное число x: "))
    y = int(input("целое отрицательное число y: "))
    xy = x ** y
    return xy

xy = my_func()
print(xy)

5.
def calc(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            flag = True
    return sum, flag

general = 0

while True:
    numbers = input('Введите числа через пробел: ').split(' ')
    sum, stop_flag = calc(*numbers)
    general += sum
    print(f'сумма {general}')

    if stop_flag:
        break

6.
my_title = lambda word: word.title() if word.islower() and ascii(word)[1:-1].isalpha() else ''
print('_'.join(map(my_title, input("Введите строку:").split())))