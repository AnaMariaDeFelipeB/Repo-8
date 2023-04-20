# Lista de 1, hasta n, cada uno con su factorial. 

n = int(input("Ingrese número natural: ")) # Inicia. Pide ingresar número. 
print("El número ingresado fue: " + str(n)) # Imprime comentario. 

range(1, n+1, 1) # Establecemos colección. (Rango de 1, hasta el valor ingresado, de a 1 en 1)
for numero in range(1, n+1, 1): # Utilizamos "for" para recorrer cada objeto en dicha colección. 
    valornumero = numero  # Creamos nueva variable, tomará el valor de los objetos. 
    multiplicador = 1 # Creamos nueva variable. 
    while (multiplicador<numero): # Establecemos condición. (Que multiplicador sea menor al valor de numero). 
        valornumero = valornumero*multiplicador  # Actualizamos. (Multiplicamos el valor de número por multiplicador). 
        multiplicador +=1 # Actualizamos. (Sumamos 1 a multiplicador)
    print("El factorial de " + str(numero) + " es " + str(valornumero))  # Imprime comentario. (Con los valores que quedaron al haber finalizado el ciclo)