n=5
m=5
bomb='x'
data=[[0for i in range(n)] for j in range(m)]
data[0][1]=bomb
data[2][3]=bomb
data[2][1]=bomb
#print(data)
x=1
y=1
data.insert(0,[0]*(n+2))
data.append([0]*(n+2))
for i in range (1,m+1):
     data[i].append(0)
     data[i].insert(0,0)


x+=1
y+=1
bomb_count = 0
for i in range (-1,2):
    for j in range(-1,2):
        if data[x+i][y+j]==bomb:
            bomb_count+=1
#print(bomb_count)

for row in range(m):
    for column in range(n):
        x=row+1
        y=column+1
        if data[x][y] != bomb:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if data[x + i][y + j] == bomb:
                        bomb_count += 1
            data[x][y]=bomb_count


for row in data:
    print(row)