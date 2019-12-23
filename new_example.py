data=[]
while True:
    user_input=input('Enter command: ').split()
    user_command=user_input[0]
    if user_command=='append':
        data+= [int(x) for x in user_input[1:]]
        print(data)
    elif user_command == 'max':

        data=max(user_input[1:])
        print(data)
    elif user_command == 'min':
        data = min(user_input[1:])
        print(data)
    elif user_command == 'second_max':
        data += [int(x) for x in user_input[1:]]
        sort_data=sorted(data)
        print(sort_data[-2])
