# 3. Дано два цілих числа 'A' і 'В'.
# Виведіть усі числа від `A` до `B` включно, в порядку зростання,
# якщо `A < B`, або в порядку зменшення в іншому випадку.

number_a = int(input('Введіть число "А" >>> '))
number_b = int(input('Введіть число "В" >>> '))
if number_a < number_b:
    print(list(range(A, number_b + 1)))
if number_a > number_b:
    list_reverse = list(range(number_b, number_a + 1))
    list_reverse.reverse()
    print(list_reverse)