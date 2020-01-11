parking=['', '', '', '']

def park(car_nom):
    for slot in range (0,len(parking)+1):
        if parking[slot]=='':
            parking[slot] = car_nom
            break
    return parking




def leave(car_nom):
    for slot in range(0,len(parking)+1):
        if parking[slot]==car_nom:
            parking[slot]=''
            break
    else:
        print('Автомобиля с таким номером нет на парковке.')
    return parking


def free(parking):
    free_slots=0
    for i in parking:
        if i=='':
            free_slots += 1

    return free_slots


def show(parking):
    print('Парковка: ',parking)
    return parking

print('Приложение "Парковка", введите команду в формате: [команда] пробел [номер машины]')
show(parking)
command=''
while command != 'exit':
    command = input('Введите команду: ')
    command_list = command.split()
    com = command_list[0]
    if com=='park':
        # команда добавляет машину на следующее пустое место (сохраняет номер) и печатает текущий список
        # если места закончились, сообщает об этом пользователю
        if free(parking) > 0:
            park(command_list[1])
        else:
            print('К сожалению, все места заняты!')
        show(parking)
        if free(parking) == 0:
            print('Предупреждение: места закончились!')

    elif com=='leave':
        # команда убирает машину (удаляет номер из списка) и печатает текущий список
        leave(command_list[1])
        show(parking)
    elif com=='free':
        # печатает количество свободных мест
        print(free(parking))
    elif com=='show':
        # печатает текущее расположение машин
        show(parking)
    elif com == 'exit':
        print('До свидания!')
    else:
        print('Ошибка. Неизвестная команда.')



