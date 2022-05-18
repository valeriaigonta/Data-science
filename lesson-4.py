from sys import argv

def salary():
    try:
        tame, rate, bonus = map(floatargv[1:])
        print(f"Salary - {tame * rate + bonus}")
    except ValueError:
        print("Enter all 3 number")

salary()

2.
result_list = []
list = [int(i) for i in input("Введите список чисел: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result_list.append(list[i]))
print("Исходный список: ", list)
print("Список, элементы которого больше предыдущего: ", result_list)


3.
list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]

print("Список чисел кратных 20 или 21 в диапазоне [20..240): ", list)

4.
from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
new_list = [i for i in my_list if my_list.count(i) == 1]
print("Элементы списка, не имеющие повторений:\n", new_list)

5.
from functools import reduce

list = [i for i in range(100, 1001, 2)]
print("Список чётных чисел в диапазоне [100..1000]:\n", list)
print("Произведение всех элементов списка:\n", reduce(lambda x,y: x*y, list))

6.
from itertools import count

print("<<Бесконечный итератор целых чисел, начиная с указанного>>")
n = int(input("Введите целое число:"))

for i in count(n):
    print(i, end=' ')
