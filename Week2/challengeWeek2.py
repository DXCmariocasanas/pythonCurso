import csv
import os
os.system('cls' if os.name == 'nt' else 'clear') #Limpia la pantalla al comenzar

#print("\033c", end="") #Limpia la pantalla al comenzar

# Función para calcular varlor inventario
def calcular_valor_inventario(precio, stock):
    precio = float(precio)
    stock = int(stock)    
    return precio * stock


# Leer CSV
with open("C:/Users/mcasanas/Downloads/producto.csv", newline="", encoding="utf-8") as archivo:

    lector = csv.DictReader(archivo)

    TotalProdAct = 0
    ValorTotalInv = 0
    ProdSinStock = 0
    catE = 0
    catO = 0
    catC = 0

    for producto in lector:

        if producto["activo"] == "True":
            print("Producto:", producto["producto"])
            print("Categoría:", producto["categoria"])
            print("Precio:", float(producto["precio"]))
            print("Stock:", int(producto["stock"]))
            varlor_inv = calcular_valor_inventario(producto["precio"], producto["stock"])
            print("Varlor inventario:", varlor_inv)
            print("\n------------------------------------\n")
                        
            if producto["categoria"] == 'Electronica':
                catE += 1
            elif producto["categoria"] == 'Oficina':
                catO += 1
            elif producto["categoria"] == 'Cocina':
                catC += 1            
            
            TotalProdAct += 1 #Sumarizo los productos Activos
            ValorTotalInv += int(varlor_inv) #Acumulo el Valor del Inventario
            #print("Varlor ACUM:", ValorTotalInv)
        else:
            ProdSinStock += 1 #Cuento los Productos sin Stock
        
        #print("\n------------------------------------\n")
        
    print("**************** TOTALES ****************\n")
    print("Total productos activos:", TotalProdAct)
    print("Valor total del inventario:", ValorTotalInv)
    print("Productos sin stock:", ProdSinStock)
    
    print("\n**************** TOTALES x Categoría ****************\n")    
    print("Electrónica:", catE)
    print("Oficina    :", catO)
    print("Cocina     :", catC)