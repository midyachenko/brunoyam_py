data=[2,4,6,7,8,11]
chet=0
chet_els=[]
els_chet_ind=[]
for i in range(len(data)):
    number=data[i]
    if number>0:
        els_chet_ind+=1
        print(els_chet_ind)
    if number%2==0:
        chet+=1
        chet_els.append(number)

    if i%2==0:
        els_chet_ind.append(number)
print(chet)

print(chet_els)

print(els_chet_ind)

print('Среднее арифметическое = ', sum(data)/len(data))