# Potencia de 2 a la n. 

n = int(input("Ingrese número natural: ")) # Inicia. Pide ingresar número. 
print("El número ingresado fue: " + str(n)) # Imprime comentario. 

range(0, n+1, 1) # Crear colección. (De 0 al valor ingresado, de 1 en 1)
for potenciaDeDos in range(0, n+1, 1):
    potencia = 2**potenciaDeDos # Establecemos operación. (2 elevado a cada valor de la colección)
    print("Dos elevado a " + str(potenciaDeDos) + " es " + str(potencia)) # Imprime comentario. 