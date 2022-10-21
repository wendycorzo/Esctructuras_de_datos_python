# EJERCICIOS LISTAS

# Ejercicios manipulación

# 1. Consiste en la definición de una lista con elementos de diferentes tipos y en mostrarla por pantalla, tanto entera como por elementos accdiendo a la posicisioón que ocupa dentro de la lista.
lista = ["Python", "Guaneta", 2022, "libro", 3]
print(lista)
print(lista[0])
print(lista[2])

# 2. Consiste en el uso del operador + para realizar uniones de lista. Además, utilizar la funcion len para conocer el número de elementos que componen la lista.
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
lista = ["camiseta", "pantalon", "zapatillas"]
print(lista)
lista = lista + ["Abrigo"]
print(lista)
lista = lista + ["Jersey", "sudadera"]
print(lista)
lista = lista + ["calcetines"] + ["Bufanda"]
print(lista)

# 4. Modificar elementos de unaa lita y borrar elementos de la misma
lista = ["camiseta", "pantalon", "zapatillas"]
print(lista)
lista[1] = "cazadora"
print(lista)
del lista[0]
print(lista)
