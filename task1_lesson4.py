a=''
b=''
op=''
while op!='exit' or a!='exit' or b!='exit':
    a = input( 'Введите значение A:' )
    op = input( 'Введите значение операции:' )
    b = input('Введите значение B:')
    if op=='+':
        print(a,op,b,'=',int(a)+int(b))
    elif op=='-':
        print(a,op,b,'=',int(a)-int(b))
    elif op == '*':2
        print(a, op, b, '=', int(a) * int(b))
    elif op=='/':
        print(a,op,b,'=',int(a)/int(b))
    else:
        print('Я не умею выполнять эту операцию')