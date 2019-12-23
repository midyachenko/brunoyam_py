words=['qwe','aaabbbcba', 'fffff', 'ertgfd','asdcn']
big_words=[]
for value in words:
    value += '$'
    last_change=0
    result=''
    for i in range(len(value)-1):

        if value[i] != value[i+1]:
            current_value=value[last_change:i+1]
            result+=value[i]+str(len(current_value))
            last_change=i+1
    print(result)
    if len(value)>5:
        big_words.append(value[0:len(value)-1])
print(big_words)



