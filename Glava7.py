data = dict()

for i in range(0,3):
    key = input('Введите имя: ')
    value = input('Введите возраст: ')
    data[key] = value
print(data.get(input('Введите имя: ')))
#print(data)