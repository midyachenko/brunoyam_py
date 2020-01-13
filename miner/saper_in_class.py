print('Это САПЕР ;-)')
print('Задайте размер поля и количество мин.')
n=int(input('Введите количество клеток по горизонтали: '))
m=int(input('Введите количество клеток по вертикали: '))
k=int(input('Введите количество мин на поле: '))

print('Задайте координаты мин. Минируйте с фантазией и максимально подло ;-)')
#моделируем поле в виде матрицы размером MxN
a=[[0 for j in range(m)] for i in range(n)]
#print(a)

for i in range(k):
    row,col = (int(i)-1 for i in input().split())
    a[row][col] = -1

for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            for di in range(-1,2):
                for dj in range (-1,2):
                    ai = i + di
                    aj = j + dj

                    if 0<=ai<n and 0<=aj<m and a[ai][aj]==-1:
                        a[i][j]+=1


print('Ваше минное поле выглялит так: ')
for i in range(n):
    for j in range (m):
        if a[i][j]==-1:
            print('*',end='')
        elif a[i][j]==0:
            print('.',end='')
        else:
            print(a[i][j], end='')
    print()