import os
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

procesando = ["/","-","\\","/","-","\\"]
#procesando = ["Mario", "Ana  ", "Bruno"]

def gotoxy(x, y):
    # Moves the cursor to column x and row y
    print(f"\033[{y};{x}H", end="")

def proceso():
    cls()
    for proceso in procesando:
        gotoxy(63,5)
        print('Calculando... '+proceso)
        time.sleep(0.5)
    cls()


#Ejercicios de Python - Funciones (Challenges)
#----------------------------------------
#CHALLENGE 1: Función simple
#----------------------------------------
# Crea una función llamada saludar que reciba un nombre
# y muestre: "Hola <nombre>"
def saludar():
        nombre = input('Ingrese un Nombre: ')
        if nombre != '':
            print(f'\n\n\nHola {nombre}, comencemos!! :-)')
#saludar()

#----------------------------------------
#CHALLENGE 2: Función que retorna valor
#----------------------------------------
# Completa la función para que regrese la suma de dos números

def suma(a,b):
    return int(a)+int(b)

#----------------------------------------
#CHALLENGE 3: Usar input + función
#----------------------------------------
# Pide dos números al usuario y usa la función sumar
"""
a = input('Ingrese un Número: ')
b = input('Ingrese un segundo Número: ')

print(f'Sumamos {a} + {b} :', suma(a,b))
"""
#----------------------------------------
#CHALLENGE 4: Función con validación
#----------------------------------------
# Crear función que diga si un número es par o impar
def parono(num):
    par = num % 2
    if par == 0:
        return 'Par'
    else:
        return 'Impar'

#a = int(input('Ingrese un Número: '))
#print(f'El número {a} es: '+ parono(a))

#----------------------------------------
#CHALLENGE 5: Reutilizar función varias veces
#----------------------------------------
# Usa la misma función varias veces con diferentes valores
import random
num1 = random.randint(1, 30)
num2 = random.randint(1, 30)
num3 = random.randint(1, 30)
print(f'El número {num1} es: '+ parono(num1))
print(f'El número {num2} es: '+ parono(num2))
print(f'El número {num3} es: '+ parono(num3))

#----------------------------------------
#CHALLENGE 6: Función con lógica
#----------------------------------------
# Crear función que calcule bono basado en sueldo

def calculaBono(sueldo):
    if sueldo >= 1500 and sueldo < 2000:
        print('Su bono es de 30%')
    elif sueldo >= 2000 and sueldo < 3000:
        print('Su bono es de 25%')
    elif sueldo >= 3000:
        print('Su bono es de 15%')
    else:
        print('Su bono es de 45% por ser pobre!! :)')

#Ma = int(input('Ingrese su Sueldo para calcular su bono: '))
#calculaBono(a)

#----------------------------------------
#CHALLENGE 7: Combinar funciones
#----------------------------------------
# Usa varias funciones juntas

#saludar()
num1 = random.randint(1, 30)
num2 = random.randint(1, 30)
sumados = suma(num1, num2)

proceso()
print(f'Sumamos dos números ranbom ({num1} + {num2}): ', sumados)
print(f'El número {num1}, es: ' + parono(num1))
print(f'El número {num2}, es: ' + parono(num2))
print(f'La Suma, ({sumados}), es: ' + parono(sumados))

