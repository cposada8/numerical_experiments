import numpy as np


def get_biggest(num):
    lista = list(str(num))
    lista.sort()

    letras = "".join(lista)

    low = int(letras)
    big = int(letras[::-1])
    
    return big, low


def kaprekar_4_cifras(num):
    
    num_iters = 0
    for _ in range(10):
        big, low = get_biggest(num)
        substraction = big-low
        #print(i, substraction)
        num = substraction
        num_iters +=1
        if num == 6174:
            break
    return num_iters



for i in range(1000, 9999):
    print(i, " -> ",kaprekar_4_cifras(i))
