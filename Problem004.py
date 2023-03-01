# This problem was asked by Two Sigma.

# Using a function rand5() that returns an integer from 1 to 5 
# (inclusive) with uniform probability, implement a function 
# rand7() that returns an integer from 1 to 7 (inclusive).

import random

def rand5(): # Creamos una función llamada rand5()
    return random.randint(1, 5)

# print(rand5()) Al correr este ejemplo, se imprimiría un número entre 1 y 5 con la misma probabilidad

def rand7():
    while True:
        # Generar dos números aleatorios entre 1 y 5 con rand5()
        num1, num2 = rand5(), rand5()
        # Calcular el número entre 0 y 24 utilizando los dos números generados
        temp = (num1 - 1) * 5 + (num2 - 1)
        # Si el número está dentro del rango deseado (1 a 21), devolverlo
        if temp < 21:
            return (temp % 7) + 1
        
# print(rand7())






