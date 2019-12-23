
while True:
    value = input('Введите выражение: ')
    print(value.split())
    if 'exit' in value:
        break

    a = value[0]
    op = value[1]
    b = value[2]
    if op=='+':
        print(a,op,b,'=',int(a)+int(b))
    elif op=='-':
        print(a,op,b,'=',int(a)-int(b))
    elif op == '*':
        print(a, op, b, '=', int(a) * int(b))
    elif op=='/':
        print(a,op,b,'=',int(a)/int(b))
    else:
        print('Я не умею выполнять эту операцию')