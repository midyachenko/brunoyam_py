

def just_line():
    print('---------------------------------------------------------------------------------')


def sum_of_digits(number):
    #Подсчитать сумму цифр числа
    result=0
    while number!=0:
        result+=number%10
        number=number//10
    return result

just_line()
print(sum_of_digits(234))
just_line()
    