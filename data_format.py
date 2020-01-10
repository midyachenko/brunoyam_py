def form_data(d):
    date = d.split('.')
    print(date)
    month = date[1]
    months = {
        '01': 'январь',
        '02': 'февраль',
        '03': 'март',
        '04': 'апрель'
    }
    return months[month]



print(form_data('12.03.1989'))






phones=set()
phones.add('123456')
print(phones)
phones.add('123457')
print(phones)