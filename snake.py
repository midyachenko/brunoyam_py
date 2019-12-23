'''result=[]
n=10

for i in range (n):
    current_list=[x for x in range(n*i+1, n*(i+1)+1)]
    if i%2==1:
        current_list.reverse()
    result.append(current_list)
for row in result:
    print(row)'''



n = 4
x=0
y=0
direction=0
result = [[0 for i in range(n)] for j in range(n)]
current=1
while current <n *n +1:
    if result[x][y]==0:
        result[x][y]=current
        current+=1
    #print(x,y,value)
    if direction ==0:
        if y+1<n:
            y+=1
        else:
            direction+=1
    elif direction ==1:
        if x+1<n:
            x+=1
        else:
            direction+=1
    elif direction == 2:
        if y-1 < 0:
            x -= 1
        else:
            direction += 1
    elif direction == 3:
        if x - 1 < 0:
            x -= 1
        else:
            direction += 1

for row in result:
    print(row)





