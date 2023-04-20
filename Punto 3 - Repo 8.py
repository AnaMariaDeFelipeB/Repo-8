# Números pares menores a un número dado. 

n = int(input("Ingrese número: "))  # Inicia. Pide ingresar un número.
print("El número ingresado fue: " + str(n)) # Imprimimos valor ingresado (antes de inciar el "for")
range(n, 0, -1) # Establecemos colección. (De n, hasta 1, disminuyendo en 1)
for numeros in range(n, 0, -1): # Utilizamos "for" para recorrer cada objeto en dicha colección. 
    if not(numeros%2==0): # Establecemos condición. Para cada objeto de la colección "range" que su modulo entre 2 no sea 0. 
        continue # Si cumple la condición anterior, ignora dicho objeto y continua iterando. 
    print(numeros) # Imprime. 