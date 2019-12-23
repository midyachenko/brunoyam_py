words=('qwerty','abcba', 'fffff', 'ertgfd','asdcn')
for word in words:
    result=True
    for i in range(len(word)//2):
        if word[i]!=word[-i-1]:
            result=False
            print('Слово ', word, 'это не полиндром')
            break
    if result==True:
        print('Слово ', word, 'это полиндром')


