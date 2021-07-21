"""
Matrices o vectores bidimensionales

Vamos a utilizar esta sesión para repasar los conceptos vistos y a aprender otras funciones interesantes 
en Python.

La función string.split(), por ejemplo, toma una cadena de caracteres (string) y la pasa a una lista.
Por defecto el separador es cada espacio en blanco, pero se puede seleccionar cualquier separador. 
Veamos un ejemplo:
"""
def ejemplo1(frase):
    lista = frase.split()
    print(lista)

ejemplo1("Esta es una prueba para pasar a una lista")

#Actividad 1
#
#Escribe una función actividad1(x, n) que reciba una frase x y un numero entero n 
#e imprima una lista con las palabras cuya longitud sea mayor a n de entrada.

#print(actividad1("Esta es una prueba para pasar a una lista",3))

#Actividad 2
#
#Creemos ahora una función crearMatriz(m,n) que genere una matriz de M * N con números aleatorios 
#entre 0 y 9 y la retorne.
#
#Creemos también una función calcularPromedio(T) que dada una matriz T, genere un promedio de todos 
#sus elementos y lo retorne.
#
#Finalmente una función actividad2(m,n) que llame a crearMatriz, pase esa matriz a calcularPromedio(T) 
#y que genere una matriz que tenga el valor 1 en aquellas posiciones donde el valor sea mayor o igual 
#al promedio en T y cero (0) donde el valor de la posición en T sea menor que el promedio.
#
#Imprimir ambas matrices.

#actividad2(3,3)