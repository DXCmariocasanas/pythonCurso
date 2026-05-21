a=20
b=5
suma=a+b

print(f'Suma: {suma} - con la variable String -> '+ str(suma)) #Muesta como String
print('Dime el Tipo de la variable: ',type(str(suma)))

print(f'Suma: {suma} - con la variable Numérica -> ',suma) #Muestra como número
print('Dime el Tipo de la variable: ',type(suma))

precio = 123.456 
print(f"Precio: ${precio:.2f}")

def sumar(a, b): 
    return a + b 

def main(): 
    print("Calculadora simple") 
    numl = int(input("Nümero 1: ")) 
    num2 = int(input("Nümero 2: ")) 
    print("Resultado:", sumar(numl, num2)) 

if __name__ == "__main__":
    main()