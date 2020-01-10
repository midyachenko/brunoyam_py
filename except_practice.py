
#try:
   # a=int(input())
   # b=int(input())
    #print(a+b)
#except ValueError as error:
 #   print ('incorrect input')
  #  print(error)
#finally:
   # print ('finally')

try:
    file = open('...\data_one_year.txt', 'r')
    for line in file:
        print(line)
except:
    print('error occured')
finally:
    if file is not None:
        file. close()
        print('file closed')

with open ('../test.txt', 'r'):
    for line in file:
        print(line, end='')


