# EJERCICIOS LISTAS

# Ejercicios manipulación

# 1. Consiste en la definición de una lista con elementos de diferentes tipos y en mostrarla por pantalla, tanto entera como por elementos accdiendo a la posicisión que ocupa dentro de la lista.
print("........Ejercicio 1....")
lista = ["Python", "Guaneta", 2022, "libro", 3]
print(lista)
print(lista[0])
print(lista[2])

# 2. Consiste en el uso del operador + para realizar uniones de lista. Además, utilizar la funcion len para conocer el número de elementos que componen la lista.
print("........Ejercicio 2....")
lista1 = ["camiseta", "pantalon", "zapatillas"]
lista2 = ["Abrigo", "Jersey", "sudadera", "calcetines"]
print("Numero elementos lista1: ",len(lista1))
print("lista1: ",lista1)
print("Numero elementos lista2: ", len(lista2))
print("lista2: ", lista2)
lista_concatenada = lista1 + lista2
print("Numero elementos lista_concatenada: ", len(lista_concatenada))
print("lista_concatenada: ", lista_concatenada)

# 3. Añadir elementos a la lista de diferentes formas
print("........Ejercicio 3....")
lista = ["camiseta", "pantalon", "zapatillas"]
print(lista)
lista = lista + ["Abrigo"]
print(lista)
lista = lista + ["Jersey", "sudadera"]
print(lista)
lista = lista + ["calcetines"] + ["Bufanda"]
print(lista)

# 4. Modificar elementos de unaa lita y borrar elementos de la misma
print("........Ejercicio 4....")
lista = ["camiseta", "pantalon", "zapatillas"]
print(lista)
lista[1] = "cazadora"
print(lista)
del lista[0]
print(lista)

# 5. Uso del operador ". Permite concatenar una  lista con ella misma un número finito de veces.
print("........Ejercicio 5....")
lista = ["camiseta", "pantalon", "zapatillas"]
print(lista)
lista_resultante = lista*3
print(lista_resultante)

# 6. Creación de listas como elementos de listas y acceso a dichos elementos.
print("........Ejercicio 6....")
lista = ["camiseta", ["calcetines", "cazadores"], "zapatillas"]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][0])
print(lista[1][1])

# 7. Extraer una porción de la lista en una lista nueva.
print(".......Ejercicio 7.....")
lista = [1,2,3,4,5,6,7,8,9]
print(lista)
lista1 = lista[3:7]
print(lista1)
lista2 = lista[:5]
print(lista2)
lista3 = lista[6:]
print(lista3)
