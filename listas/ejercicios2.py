# EJERCICIOS LISTAS

# Métodos propios

lista = [45,32,3,78]
print("lista original: ", lista)
# funcion append: añade un elemento a la lista
lista.append(995)
lista.append(7)
print("lista despues de usar append: ", lista)
# Funcion sort: ordena la lista
lista.sort()
print("lista ordenada: ", lista)
# Funcion reverse: invierte el orden de la lista
lista.reverse()
print("lista al revés:", lista)
# Funcion extend: añade los elementos de una lista a la lista
lista_extend = [1,5,87,45]
lista.extend(lista_extend)
print("lista despues de extend: ", lista)
# Funcion count: cuenta el número de veces que aparece el elemento indicado como parametro dentro de la lista
print("número de elementos 45: ", lista.count(45))
# Funcion insert: añade el  elemento pasado como parametro a la lista como parametro a la lista en la posicion indicada tambien por el parametro
lista.insert(4,111)
print("lista despues de insert: ", lista)
# Funcion remove: elimina la primera ocurrencia empezando por la izquierda por la izquierda de la lista del elemento indicado como parámetro
lista.remove(45)
print("lista desoues de remove: ", lista)
# Funcion index: devuelve la posicion de la primera ocuriencia de izquierda a derecha en la lista, del elemento pasado como parámetro
print("posicion del elemento 111: ", lista.index(111))
# Funcion pop: elimina el ultimo elemento de la lista y lo devueve como resultado de la operación
lista.pop()
print("lista despues de pop: ", lista)
# Funcion clear: elimina todos los elemetos de la lista
lista.clear()
print("lista despues de clear: ", lista)