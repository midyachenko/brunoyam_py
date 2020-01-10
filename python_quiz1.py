"""
Определить, какой тип будет иметь результат операции (переменная c)
"""
print('Task 1')
a = 3
b = 4
c = a / b

print(type(c))

"""
Посчитать сумму чисел от 1 до 100
"""
print('Task 2')
count = 0
for i in range(0, 101):
    count = count + i
print(count)


"""
Проверить, что число является четным
"""
print('Task 3')
number = 4
if number % 2 == 0:
    print('ok')
else:
    print('ne ok')

"""
Будет ли работать данный код?
name = "Svetozar"
age = 24
name_and_age = name + age
"""
print('Task 4')
print('нет')

"""
Проверить, если ли заданное число в списке
"""
print('Task 5')
number = 3
data = [1, 4, 2]
if number in data:
    print('yes')
else:
    print('no')

#data.index(3, 0, 3):


"""
Написать функцию, которая проверяет, делится ли одно число на другое без остатка
"""
print('Task 6')
def delenie(a, b):
    if a % b==0:
        return 'yes'
    else:
        return 'no'

a=int(input('Enter A '))
b=int(input('Enter B '))
print(delenie(a,b))