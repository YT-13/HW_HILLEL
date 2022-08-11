# 2. Напишіть програму, яка зчитує ціле число та виводить текст, аналогічний наведеному у прикладі (Прогалини важливі!).
# Перший рядок містить наступне значення, а другий рядок містить попереднє значення введеного числа:
#     Please enter an integer number: 1234
#     Next number for number 1234 is 1235.
#     Previous number for number 1234 is 1233.

number = input('Please enter an integer number >>> ')
number_next = int(number) + 1
number_before = int(number) - 1
print(number_next)
print(f'Next number for number {number} is {number_next}')
print(f'revious number for number {number} is {number_before}')