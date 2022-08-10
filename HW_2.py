# Всі завдання повинні бути в гіт-репозиторії, кожна у своєму окремому файлі та новій директорії lesson_2 (або у окремі гілці lesson_2)
#
# 1. Напишіть програму, яка вітає користувача, виводячи слово `Hello`,
# введене користувачем ім'я та розділові знаки за зразком:
# Hello, Kitty!

# name = input("Ведіть ваше імя >>>")
# print("Hello, %s!" % name)

# 2. Напишіть програму, яка зчитує ціле число та виводить текст, аналогічний наведеному у прикладі (Прогалини важливі!).
# Перший рядок містить наступне значення, а другий рядок містить попереднє значення введеного числа:
#     Please enter an integer number: 1234
#     Next number for number 1234 is 1235.
#     Previous number for number 1234 is 1233.
# number = input('Please enter an integer number >>>')
# number_next = int(number) + 1
# number_before = int(number) - 1
# print(number_next)
# print(f'Next number for number {number} is {number_next}')
# print(f'revious number for number {number} is {number_before}')

#
# 3. Довжина маршруту велоралі "100 кілометрів за 10 годин" - приблизно 100 кілометрів.
# Велосипедист Вася стартує з нульового кілометра маршруту та їде зі швидкістю `v` кілометрів на годину.
# На якій відмітці він зупиниться через `t` годин?
# Програма отримує на вхід значення `v` та `t`. Якщо `v > 0`, то Вася рухається у позитивному напрямку за маршрутом,
# якщо ж значення `v < 0`, то негативному.
# Програма має вивести ціле число від 0 до 100 – номер позначки, на якій зупиниться Вася.
#
#
#
# 4. Дано натуральне число. Потрібно визначити, чи є рік із цим числом високосним. Якщо рік є
# високосним, то виведіть `YES`, інакше виведіть `NO`.
# Нагадаємо, що відповідно до григоріанського календаря, рік є високосним, якщо його номер кратний 4, але не кратний 100,
# а також якщо він кратний 400.
#
# year = input('Введіть будь-який рік >>> ')
# if int(year) % 400 == 0:
#     print('YES')
# elif int(year) % 4 == 0 and int(year) % 100 != 0:
#     print('YES')
# else:
#     print('NO')
#
# 5. У математиці функцію `sign(x)` (знак числа) визначено так:
#   ``
#   sign(x) = 1, якщо x > 0,
#   sign(x) = -1, якщо x < 0,
#   sign(x) = 0 якщо x = 0.
#   ``
#   Для цього числа x виведіть значення sign(x). Це завдання бажано вирішити за допомогою каскадних інструкцій if... elif... else.
#
#
#
# 6. Програма отримує на вхід число х.
#   Даний список із 10 елементів [10, 20, 30, 40, 50, 60, 70, 80, 90, 100].
#   Написати програму яка поверне:
#   Чи є x серед елементів.
number = input('Введіть число >>> ')
number = int(number)
elements = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in range(len(elements)):
    if elements[x] == number:
        print(f'Число {number} є серед')

#
#
#   Число на введення може бути як цілим числом, числом з точкою, що плаває, так і від'ємним,
#   тобто. x = -10.00 має повернути що x є у списку.
#  ** В ідеалі список повинен бути записаний як кортеж один раз.
#
# 7. Написати програму "Показати зірки". На вхід приймає звичайне ціле число, має надрукувати кількість зірок:
#   Приклад:
#   Input number of stars: 8
#   ********
# print('Вас вітає програма "Показати зірки"!')
# number = input('Введіть ціле число >>> ')
# print(int(number) * '*')


