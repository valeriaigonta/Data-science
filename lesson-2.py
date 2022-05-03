1.
my_list = [4, False, 5 / 6, "Str", 7.7, [5, 7], (90, 9.0), {5: 'numb'}, None]
for ind, el in enumerate(my_list, 1):
    print(f"{ind}) {el} - {type(el)}")

2.
my_list = input("Введите числа списком с пробелом :").split()
str_reverse = ' '
symbol = list(my_list)
for el in range(1, len(symbol), 2):
    symbol[el - 1], symbol[el] = symbol[el], symbol[el - 1]
str_reverse = ' '.join(symbol)
print(str_reverse)


3.
my_dict = { 1 : "зима", 2 : "зима", 3 : "весна", 4 : "весна", 5 : "весна", 6 : "лето", 7 : "лето", 8 : "лето",
           9 : "осень", 10 : "осень", 11 : "осень", 12 : "зима"}
munth = int(input("Введите номер месяца : "))
print(my_dict.setdefault(munth))

4.
a = input("Введите слова с пробелом в виде строки:").split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[:10]
    print(f"{i}. - {el}")

5.
rating = [7, 6, 5, 5, 4, 4]

while True:
    numb = input("Введите числа списком с пробелом.:")
    if numb.isdigit():
        rating.append(int(numb))
        rating.sort(reverse=True)
        print(rating)











