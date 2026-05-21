#1. Lista 
datos = ["Pedro", "Ana", "Luis"] 
#2. Tuple 
colores = ("rojo", "azul","verde")

#3 Set
nombres = {"Ana", "Luis", "Pedro"} 

# 4 Diccionario
empresa = {
    "empleado1": {
        "nombre": "Ana", 
        "puesto": "IT"
        },
    "empleado2": {
        "nombre": "Luis", 
        "puesto": "HR"
        }
    }

#LOOPS
#i=1
for i in range(5):
    print('I: ', int(i))

contador = 1
while contador <= 5:
    print('contador: ', int(contador))
    contador += 1


frutas = ["Manzana", "Pera", "Uva", "Naranja"]
for i in range(len(frutas)):
    print('I: ', i, frutas[i])

nombres = ["Felipe", "Hora", "Carlos", "Mario"]
for i in range(len(nombres)):
    if nombres[i] == "Carlos":
        print('Carlos, encontrado en el indice: ', i)

for i in range(2,7):
    print('indice: ', i)