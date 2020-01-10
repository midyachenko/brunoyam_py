from typing import List

def sum_of_el(a,b):
    '''
    функция для вычисления 2-х чисел

    :param a: слагаемое
    :type a: int
    :param b: слагаемое
    :type b: int
    :return: сумма двух слагаемых
    :rtype: int
    '''
    return a+b


print(sum_of_el(3,6))

data=[]

def find_positive(data):
    '''

    :type data: List[int]
    :return:
    '''
    result=[]

    for el in data:
        if el>0:
            result.append(el)
    return result



def my_join(*args, delimiter=' '):
    print(args)
    return delimiter.join(args)

print(my_join('Hello', 'world','!!!'))
print(my_join('a','b','c','d'))


def most_common_function (*args, **kwargs):
    print (args)
    print(kwargs)