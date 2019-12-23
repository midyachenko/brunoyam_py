'''a=10
b=20
values=[x**2 for x in range(a,b+1)]

print(values)

values=[]
for x in range(a,b+1)
    values.append(x**2)

values=[x for x in values if x%2==0]
print(values)

values = [100 if x<200 else 400 for x in values]
print(values)


a=10
b=20
values=[x for x in range(a,b+1)]
print('Список от 10 до 20',values)

n=10
values=[2**x for x in range(0,n+1)]
print('Список степеней двойки от 0 до ',n,values)


values=['ZZZ','Rth', 'ttt']
values=[x for x in values if x==x.upper()]
print('Список верхний регистер',values)


n=10
values=[x for x in range(1,n+1)]
print('Список возрастающего количества возрастающих значений до',n,values)

n=4
m=5
zero_matrix=[ [0 for y in range(m)] for x in range(n)]
print (zero_matrix)

for row in zero_matrix:
    for el in row:
        print (el, end=' ')
    print()

n=10
for i in range (1,n+1):
    for j in range (1,n+1):
        c=j*i
        if c < 10:
            print(c, end='  ')
        else:
            print(c, end=' ')

    print()

values =[]
k=10
n=4
for k in range (1,n+1):
    for i in range(k):
        values.append(k)
print(values)

values =[]
k=10
n=4
for k in range (1,n+1):
    values +=[k]*k
print(values)

values=[k for k in range(1,n+1) for i in range(k)]
print(values)'''
