# Potencia de dos valores dados.
 
x: float = float(input("Ingrese base: ")) # Inicia. Pide ingresar número. 
n: int = int(input("Ingrese exponente natural: "))  # Pide ingresar número. 


datos = [n] # Generamos una lista. 

for valores in datos: # Utilizamos "For" para recorrer cada objeto de la colección. 
    operación = x**valores # Opera los objetos de la colección. 
    print(str(x) + " a la " + str(valores) + " es: " + str(operación)) # Imprime. 