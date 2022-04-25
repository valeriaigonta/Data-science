weight = float(input("Введите ваш вес в кг: "))
height = float(input("Введите рост в см: "))
IMT = weight / (height ** 2)
print(f"{IMT}:")


time = int(input('Enter the time in seconds:'))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")


n = input("Введите целое число,больше 0:")
print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")


numbers = int(input("Введите целое положительное число:"))
big_num = 0
num = numbers

while num > 0:
    digit = num % 10
    if digit > big_num:
        big_num = digit
        if big_num == 9:
            break
    num //=10

print(f"Наибольшая цифра {numbers} ровна {big_num}")


revenue = float(input("Укажите вашу выручку:"))
costs = float(input("Укажите ваши издержки:"))
difference = revenue - costs
if difference > 0 :
    print(f"прибыль вашей компании составила {difference}.")
    print(f"Рентабельность ровна {100 * (difference / costs):.2f}%")
    personal = int(input("Количество сотрудников компании?"))
    print(f"Прибыль фирмы в расчете на обного сотрудника {difference / personal:5f}.")
elif difference <= 0:
        print("У вас нет выручки.")


while True:
    days = 1
    start_km = float(input("Стартовый результат: "))
    finish_km = float(input("Финальный результат: "))
    if start_km <= 0:
        print("Результаты должны быть больше нуля.")
    else:
        while start_km < finish_km:
            start_km += start_km * 0.1
            days += 1

            print(f"Спортсмен добьется результата за {days} дней")
            break