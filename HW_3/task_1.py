#1. Користувач вводить трицифрове число. Знайдіть суму його цифр.

numbers = input('Введіть трицифрове число >>> ')
numbers_list = []
for x in numbers:
    numbers_list.append(int(x))
print(f'Сума = {sum(numbers_list)}')