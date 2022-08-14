# 5. Користувач вводить число від 1 до 10, програма генерує рандомне число від 1 до 10,
# якщо числа співпадають надрукувати 'You won!' якщо ні - 'You lose!'.Дати користувачеві три спроби;)
import random
number = int(input('Введіть число від 1 до 10 >>> '))
any_number = random.randint(1, 10)
if number == any_number:
    print('You won!')
else:
    print('You lose!')

# if int(input('Введіть число від 1 до 10 >>> ')) == random.randint(1, 10) :
#     print('You won!')
# else:
#     print('You lose')