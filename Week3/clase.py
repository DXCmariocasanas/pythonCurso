import os
os.system('cls' if os.name == 'nt' else 'clear') #Limpia la pantalla al comenzar

#palabras = ["python", "java", "go for it"] 
#
#resultado = list(map(lambda p: len(p), palabras))
#doble = list(map(lambda p: len(p)*2, palabras))
#
#print('resultado: ', resultado)
#print('doble: ', doble)
#
#
#suma = lambda x, y: x+y
#print(suma(5,3))
#
#numeros = [1, 2, 3, 4, 5] 
#pares = list(filter(lambda x: x % 2 == 0, numeros))
#
##Lista los números pares
#print(pares)

doble = lambda x: x*2
valor = 10
print(f'Imprime el doble de lo ingresado: ({valor}), resultado: ', doble(10))

# ************************************************************* 
# ************************** OBJETOS ************************** 
# ************************************************************* 
class Perro: 
    def __init__(self, nombre, altura, peso, raza): 
        self.nombre = nombre 
        self.altura = altura 
        self.peso = peso 
        self.raza = raza 

    def ladrar(self): 
        if self.raza == "Labrador": 
            return "Woof woof!"
        elif self.raza == "Beagle": 
            return "Guau guau!"
        else: 
            return "Ladrido no definido para la Raza: "+self.raza
    
    def saludar(self): 
        print("Hola, soy", self.nombre)
    
    def obtener_peso(self):
        return self.peso
    
mi_perro = Perro("Fido", 50, 20, "Labrador")
print(mi_perro.nombre)
mi_perro.ladrar()

tu_perro = Perro("Ronaldito", "40 cm", "15 Kg", "Beagle")
print(tu_perro.nombre + ': Altura: '+tu_perro.altura)

tu_perro.saludar()
mi_perro.saludar()

print("Peso de tu perro: ",tu_perro.obtener_peso())
print("Como ladra tu perro: ",tu_perro.ladrar())

print("Peso de Mi perro: ",mi_perro.obtener_peso())
print("Como ladra Mi perro: ",mi_perro.ladrar())

perrito = Perro("El Perrito", "40 cm", "15 Kg", "Breton")
print("Como ladra 'El Perrito': ",perrito.ladrar())

