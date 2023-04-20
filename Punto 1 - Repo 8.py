# Números del 1 al 100 con su respectivo cuadrado. 

range(0, 101, 1) # Generemos una colección rango y establecemos el intervalo. (De 0 a 100 y que vaya de 1 en 1). 
for numeros in range(0, 101, 1): # Utilizamos el "for" para recorrer cada objeto en dicha colección. 
    print("El cuadrado del número " + str(numeros) + " es:", numeros**2) # Imprimimos. 