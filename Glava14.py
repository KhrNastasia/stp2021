try:
    z = int(input('Введите делимое: '))
    y = int(input('Введите делитель: '))
    x = z/y
    print(x)
except ZeroDivisionError:
    print('Ошибка! Деление на ноль запрещено!')
#else:
 #   print("")