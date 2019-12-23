'''number=123

#Подсчитать сумму цифр числа
result=0
delit=0
while number!=0:
    result+=number%10
    number=number//10
print(result)
#подсчитать количество делителей
number=123
count=0
for i in range(2,number):
    if number%i==0:
        count+=1
        print(i)
print(count)

print(sum([1 if number%x ==0 else 0 for x in range(2,number)]))'''


