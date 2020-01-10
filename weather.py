
def number_of_days(month_number):
    if month_number==1: #feb
        return 28
    else:
        if month_number<7:
            return 30 if month_number%2==0 else 31
        else:
            return 31 if month_number % 2 == 0 else 30

#print(number_of_days(6))

weather=dict()
months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
for i in range(len(months)):
    current_month=months[i]
    weather[current_month]=[0]*number_of_days(i)



with open('data_one_year.txt','r' ) as data:
    for month in months:
        current_days=weather[month]
        for i in range(len(current_days)):
            current_days[i] = int (data.readline())

    #for line in data:
        #weather.values[]=data.readline()
       # pass

#print(weather)

#print(weather['apr'],[23])

while True:
    try:
        user_input=input().split()
        command=user_input[0]

        if command=='temp':
            month=user_input[1]
            day=int(user_input[2])-1
            print(weather[month][day])
        elif command =='average':
            if len(user_input)>2:
                first=user_input[1]
                second=user_input[2]
            elif user_input[1]=='year':
                summa=0
                for month in weather:
                    summa+= sum(weather[month])
                    print(weather[month][day])
    except:
        print('Wrong command. Retry.')

