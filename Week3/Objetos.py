import os
os.system('cls' if os.name == 'nt' else 'clear') #Limpia la pantalla al comenzar

empleados_data = [ 
    {"nombre": "Ana", "salario": 1800},
    {"nombre": "Luis", "salario": 1508},
    {"nombre": "Pedro", "salario": 888},
    {"nombre": "Mario", "salario": 15000}
]

class Empleado: 
    def __init__(self, nombre, salario): 
        self.nombre = nombre 
        self.salario = salario 

    def aumentar_salario(self): 
        self.salario += 100 

    def mostrar(self): 
        print(self.nombre, "- Salario:", self.salario) 

empleados = []

for emp in empleados_data:
    empleado = Empleado(emp["nombre"], emp["salario"])
    empleados.append(empleado) 

for emp in empleados: 
    emp.aumentar_salario()

for emp in empleados:
    emp.mostrar()
