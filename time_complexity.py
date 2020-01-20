import time

def run_timed(fun):
    begin_time = time.time()
    fun()
    end_time = time.time()
    print(end_time - begin_time)






def first():
    s=0
    n=1000000
    for i in range (1,n):
        s+=i
    print(s)


def third():
    pairs = []
    n=100
    for i in range(n):
        for j in range(n):
            pass
            #airs[i][j]=1
    #print(pairs)


def bubble_sort(data):
    n=len(data)
    for i in range (n):
        for j in (0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print(data)

def join_sort(data):



run_timed(first)
#run_timed(third)
run_timed(bubble_sort([4,5,3,1,2]))


#numbers =