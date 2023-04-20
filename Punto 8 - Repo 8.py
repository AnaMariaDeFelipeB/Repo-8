# Función exponencial. 

import math # Llamamos a la función de matematicas. 

def funciónExponencial (exponente: float, n: int) -> float:  # Generamos función y definimos sus variables. 
    real = math.exp(exponente) # Generamos una variable que sea la operación de la función exponencial. 
    aproximado = 0 # Generamos variable. 
    

    range(0, n+1, 1)   # Establecemos colección. (Esta vez representará las repeticiones)
    for i in range(0, n+1, 1): # Utilizamos "For" para recorrer cada objeto de la colección. 
        operación = (exponente**i)/(math.factorial(i))  # Establecemos operación determinada. 
        aproximado = aproximado+operación  # Actualizamos variable. (Suma al aproximado la operación)
            
    
    diferencia = abs(real - aproximado)  # Establecemos la diferencia entre la variable "real" y el valor final de la variable "aproximado"

 # Indicamos con el return lo que debe devolver esta función.  
    return ("El valor real de la función exponencial es: " + str(real) + " comparado con su aproximado en las series de Maclaurin que es de: " + str(aproximado) + " \n  Y tienen una diferencia de: " + str(diferencia))   





if __name__ == "__main__": # Nos permite correr funciones. 
    exponente = float(input("Ingrese exponente: ")) # Pide ingresar número.(El cuál permitirá a la función tomar dicho valor)
    n = int(input("Ingrese número de repeticiones: ")) # Pide ingresar número.(El cuál permitirá a la función tomar dicho valor)
    función = funciónExponencial (exponente, n) # Generamos variable que tomará el valor de return en la función anteriormente establecida. 
    print(función) # Imprimimos. 