value='aasssddddbbhhh'
symbol='b'
count=0
for char in value:
    if char==symbol:
        count +=1
print('В строке ',value, 'содержится', count/len(value)*100,' % символов ',symbol)

value2=value[-1]+value[1:-1]+value[0]
print('перевертыш', value2)