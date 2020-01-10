'''def max_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a=4
b=7
c=45
print('максимум из 3 чисел', a, b, c,'=', max_num(a,b,c))



def test_year(year):
    if year%4==0 or year%100==0:
        result='год високосный'
    else:
        result='год не високосный'
    return result


print(test_year(1982))


def gipotenuza(a,b):
    return (a**2+b**2)**0.5

print(gipotenuza(4,5))'''


def form_data(dat):
    date = dаt.split('.')
    print(date)
    month = date[2]
    months = {
        '01': 'январь',
        '02': 'февраль',
        '03': 'март'
    }
    return months[month]


dat = '12.02.1989'
print(form_data(dat))
