# 4. По даному натуральному `n ≤ 9` виведіть драбинку з `n` сходинок,
# `i`-я сходинка складається з чисел від 1 до `i` без прогалин.
#a = int(input('Введіть число "А" >>> '))
input_number = int(input('Введіть число >>> '))
numbers = ""
for x in range(1, input_number + 1):
       numbers += str(x)
       print(numbers)


