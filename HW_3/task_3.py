#3. Друкувати список list_ten = [10, 20, 30, 40, 50] реверсивно - тобто. програма має повернути [50, 40, 30, 20, 10].
list_ten = [10, 20, 30, 40, 50]
# list_ten.reverse()
# print(list_ten)

# Спосіб №1
list_reverse = []
for elem in range(len(list_ten)-1, -1, -1):
    list_reverse.append(list_ten[elem])
print(list_reverse)


# Спосіб №2
list_reverse = list_ten[::-1]
print(list_reverse)

# Спосіб №3
list_ten.reverse()
print(list_ten)