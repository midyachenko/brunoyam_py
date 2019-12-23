a=int(input('Введите число a '))
b=int(input('Введите число b '))
c=int(input('Введите число c '))

if a>b:
    if b>c:
        print('Второй максимум = ', b)
    else:
        print('Второй максимум = ', c)

if b>c:
    if a>c:
        print('Второй максимум = ', a)
    else:
        print('Второй максимум = ', c)
else:
    if c>a:
        print('Второй максимум = ', b)
    else:
        print('Второй максимум = ', a)