"""
Funciones con listas

Aquí van algunas funciones útiles cuando trabajamos con listas.

    remove(x) - remueve el primer valor X de la lista
    pop([i]) - remueve el valor en la posición i. pop() remueve el último valor de la lista
    len(x) - permite calcular el tamaño de una lista
"""
def ejemplo1():
    nombres = ["María", "Juan","Andrés"]
    nombres.append("Jorge")
    print(nombres)
    print(len(nombres))

    nombres.remove("Juan")
    print(nombres)
    print(len(nombres))

    nombres.pop(2)
    print(nombres)
    print(len(nombres))
ejemplo1()

"""
Como vemos, append(x) inserta el valor x al final de la lista.

Pero también existe la función insert(pos, x) que nos permite insertar x en la posición pos. 

Veamos un ejemplo
"""
def ejemplo2():
    a = [1, 3, 2, 5, 2]
    a.insert(4,8)
    print(a)

#ejemplo2()

#Actividad 1

#Escribamos un programa que nos permita crear con una lista de 6 números aleatorios entre 1 y 20, 
#y luego creemos tres funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos
#    orden(x) - Una función que ordene los datos de una lista x ascendentemente y la imprima en orden

#actividad1()
