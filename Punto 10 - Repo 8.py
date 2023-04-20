# Función Arcotangente. 

import math # Llamamos a la función de matematicas. 

def funciónArcotangente (x: float, n:int): # Generamos función y definimos sus variables. 
    real = math.atan(x) # Generamos una variable que sea la operación de la función del arcotangente. 
    aproximado = 0 # Generamos variable. 

    range(1, n+1, 1)  # Establecemos colección. (Esta vez representará las repeticiones)
    for i in range(1, n+1, 1): # Utilizamos "For" para recorrer cada objeto de la colección. 
        operación = ((-1)**i)*(x**((2*i)+1))/((2*i)+1) # Establecemos operación determinada. 
        aproximado = aproximado+operación # Actualizamos variable. (Suma al aproximado la operación)
    
    diferencia = abs(real - aproximado)  # Establecemos la diferencia entre la variable "real" y el valor final de la variable "aproximado"

# Indicamos con el return lo que debe devolver esta función.  
    return ("El valor real de la función del arcotangente es: " + str(real) + " comparado con su aproximado en las series de Maclaurin que es de: " + str(aproximado) + " \n  Y tienen una diferencia de: " + str(diferencia))

if __name__ == "__main__": # Nos permite correr funciones. 
    x = float(input("Ingrese valor: ")) # Pide ingresar número.(El cuál permitirá a la función tomar dicho valor)
    n = int(input("Ingrese serie de repeticiones: ")) # Pide ingresar número.(El cuál permitirá a la función tomar dicho valor)
    función = funciónArcotangente (x,n)  # Generamos variable que tomará el valor de return en la función anteriormente establecida. 
    print(función) # Imprimimos. 