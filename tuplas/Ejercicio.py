# EJERCICIOS TUPLAS

# Ejercicio 1: determina en que posicion se encuentra determinado un objeto
print("........Ejercicio 1....")
tupla = ("casa" , "2", "345", "perro",99)
print("Elemento de tupla:",tupla)
print("Elemento de la posicion 0: ",tupla[0])
print("Elemento de la posicion 1: ",tupla[1])
print("Elemento de la posicion 2: ",tupla[2])
print("Elemento de la posicion 3: ",tupla[3])
print("Elemento de la posicion 4: ",tupla[4])

# Ejercicio 2: ubica cuantos elementos hay en una variable y determina en que posicicion esta uno de ellos
print("........Ejercicio 2....")
tupla = ("Casa", "2",99, 345, "Perro",99)
print("Elementos de la tupla: ",tupla) 
print("Numero de elementos 99: ",tupla.count (99))
print("Posicion que ocupa el elemento Perro: ", tupla.index("Perro"))

# Ejercicio 3: extrae una tupla, y luego la empieza en el indice n y esta terminara en el indice m-1.
print("........Ejercicio 3....")
tupla = (1,2,3,4,5,6,7,8,9)
print(tupla)
print(tupla[4:9])
print(tupla[: 3])
print(tupla[2:])

# Ejercicio 4: Nos permite saber la cantidad de elementos que tiene una tupla garcias a la funcion len.
print("........Ejercicio 4....")
tupla1 = (29, "Televisión", 8763)
tupla2 = (1,2,3, "Videojuego")
print("Número elementos de tupla1: ", len(tupla1))
print("Tupla1: ", tupla1)
print("Número elementos de tupla2: ",len(tupla2))
print("Tupla2: ", tupla2)
tuplaconcatenada = tupla1 + tupla2
print("Número elementos de tuplaconcatenada: ", len(tuplaconcatenada))
print("tuplaconcatenada: ", tuplaconcatenada)

# Ejercicio 5: Nos permite multiplicar los valores que contiene la tupla dependiendo de cuantas veces queramos que se multiplique en este caso: 4
print("........Ejercicio 5....")
tupla = (1,2,3,4,5,6,7,8,9,0)
print(tupla)
tuplaresultante = tupla * 4
print(tuplaresultante)