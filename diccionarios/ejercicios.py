# ejercicios
"Los ejercicios con diccionarios los hemos dividido en do grupos diferentes. El primer grupo de ejercicios consiste en la manipulación de los diccionarios y el segundo grupo consiste en el aprendizaje de los métodos propios de los tipos de datosdiccionario"

# MANIPULACIÓN

# ejercicio 1: Muestra algunos elementos del mismo diccionario. Para acceder a los elementos del diccionario deberas de utilizar la clave del elemento.

print("--------Ejercicio 1--------")

diasemanaingles = {"Lunes" : "Monday", "Martes" : "Tuesday", "Miercoles" : "Wednesday", "Jueves" : "Thursday", "Viernes" : "Friday"}
print(diasemanaingles["Lunes"])
print(diasemanaingles["Miercoles"])
print(diasemanaingles["Viernes"])

# Ejericio 2: Modifica el valor de algun elemento y borrando algun elemento. En el ejercicio utilizaremos el diccionario del ejercicio anteriorañadiendo los dias sabado y domingo, modificando el valor de algun elemento y borrando algun elemento

print("--------Ejercicio 2--------")

diassemanaingles = {"Lunes":"Monday","Martes":"Tuesday","Miercoles": "Wednesday","Jueves": "Thursday","Viernes": "Friday"}

print(diassemanaingles)
diassemanaingles["Sabado"] = "Saturday"
print(diassemanaingles)
diassemanaingles["Domingo"] = "Sunday"
print(diassemanaingles)
diassemanaingles["Lunes"] = "MondayBORRAR"
print(diassemanaingles)

print("--------Ejercicio 3--------")

diassemanaingles = {"Lunes" : "Monday","Martes" : "Tuesday","Jueves":"Thursday","Miercoles": "Wednesday", "Viernes" : "Friday"}
print("Número de elementos del diccionario: ",len(diassemanaingles)) 
print("Elemento mayor del diccionario: ",max(diassemanaingles)) 
print("Elemento menor del diccionario: ",min(diassemanaingles))


#Ejercicio 4: Un ejercicio que nos permite aprender todas  la funciones

print("--------Ejercicio 4-----------")

diassemanaingles= {"Lunes": "Monday", "Martes" : "Tuesday",

"Miercoles": "Wednesday",

"Jueves": "Thursday",

"Viernes": "Friday"}

print("Diccionario original: ", diassemanaingles)

diccionariocopia =diassemanaingles.copy()

print("Diccionario copy: ",diccionariocopia)

print("Valor del Lunes (pop): ", diassemanaingles.pop("Lunes"))

print("Diccionario después del pop: ",diassemanaingles)

print("Elemento al azar con popitem: ", diassemanaingles.popitem())

print("Diccionario después del popitem: ", diassemanaingles)

print("Valor del Martes (get): ",diassemanaingles.get("Martes"))

print("Valor del Lunes (get) (no existe): ",diassemanaingles.get("Lunes"))
print("Valor del Lunes (get) (no existe): ",diassemanaingles.get("Lunes","No existe")) 

diassemanaingles.update({"Lunes":"MondayNUEVO", "Martes":"TuesdayNUEVO"})

print("Diccionario después del update: ",diassemanaingles)

print("setdefault del Sábado: ",diassemanaingles.setdefault("Sabado", "Saturday"))

print("Diccionario después del setdefault (nuevo elemento): ",diassemanaingles) 
print("setdefault del Lunes: ",diassemanaingles.setdefault("Lunes", "Lunes"))

print("Diccionario después del setdefault (elemento existente): ",diassemanaingles)

print("Elemento iterable (items): ",diassemanaingles.items())

print("Elemento iterable (claves): ",diassemanaingles.keys()) 
print("Elemento iterable (valores): ",diassemanaingles.values())

print("Diccionario después del clear: ",diassemanaingles.clear())