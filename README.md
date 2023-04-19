# Repostorio reto 8. 
### _Desarrollado por Ana Maria De Felipe Briñez._
---
Bienvenidos a este repostorio del reto 8 de la clase de programación. Nuevamente estaré resolviendo los problemas de la clase de programación. 

Para comenzar, desarrolle el ejercicio planteado en clase. 

1.	¿Qué se genera con range(-2)?

![image](https://user-images.githubusercontent.com/124607045/232943176-523491c8-288e-4b3c-9ec7-c709335067c1.png)

RESPUESTA: Al realizar el ejercicio se pudo observar que no se genera nada. 

---
Ahora bien, una vez ya terminado el ejercicio, evidenciare lo desarrollado en los problemas planteados. (No olvidar revisar los archivos donde se muestra más a detalle el desarrollo. 

Iniciando con el primer punto. 

1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```Python
# Números del 1 al 100 con su respectivo cuadrado. 

range(0, 101, 1) # Generemos una colección rango y establecemos el intervalo. (De 0 a 100 y que vaya de 1 en 1). 
for numeros in range(0, 101, 1): # Utilizamos el "for" para recorrer cada objeto en dicha colección. 
    print("El cuadrado del número " + str(numeros) + " es:", numeros**2) # Imprimimos. 
```
---

Continuamos con el siguiente punto. 

2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
Desarrolle el siguiente código para la solución de dicho punto.  

```Python
# Listado números impares. 

range(1, 1000, 2) #Generamos colección rango. (De 1 a 999, de 2 en 2)
for impares in range(1, 1000, 2): # Utilizamos el "for" para recorrer cada objeto en dicha colección. 
    print(str(impares)) # Imprimimos
```
```Python
# Lista números pares. 

range(0, 1001, 2) # Generamos colección rango. (De 0 a 1000, de 2 en 2)
for pares in range(0, 1001, 2): # Utilizamos el "for" para recorrer cada objeto en dicha colección. 
    print(pares) # Imprimimos. 
```

--- 

Avanzando, nos encontramos con el siguiente punto. 

3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
Para ello, desarrolle el siguiente código. 

```Python
# Números pares menores a un número dado. 

n = int(input("Ingrese número: "))  # Inicia. Pide ingresar un número.
print("El número ingresado fue: " + str(n)) # Imprimimos valor ingresado (antes de inciar el "for")
range(n, 0, -1) # Establecemos colección. (De n, hasta 1, disminuyendo en 1)
for numeros in range(n, 0, -1): # Utilizamos "for" para recorrer cada objeto en dicha colección. 
    if not(numeros%2==0): # Establecemos condición. Para cada objeto de la colección "range" que su modulo entre 2 no sea 0. 
        continue # Si cumple la condición anterior, ignora dicho objeto y continua iterando. 
    print(numeros) # Imprime. 
```
---

Ahora bien, observamos el siguiente punto. 

4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectiva factorial. 

Para ello desarrolle el siguiente código.

```Python
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
```
---
Avanzamos con el siguiente punto. 

5. Calcular el valor de 2 elevado a la potencia n usando ciclos for. 

Desarrolle el siguiente código para la solución de dicho punto.  

```Python
# Potencia de 2 a la n. 

n = int(input("Ingrese número natural: ")) # Inicia. Pide ingresar número. 
print("El número ingresado fue: " + str(n)) # Imprime comentario. 

range(0, n+1, 1) # Crear colección. (De 0 al valor ingresado, de 1 en 1)
for potenciaDeDos in range(0, n+1, 1): # Utilizamos "For" para recorrer cada objeto de la colección. 
    potencia = 2**potenciaDeDos # Establecemos operación. (2 elevado a cada valor de la colección)
    print("Dos elevado a " + str(potenciaDeDos) + " es " + str(potencia)) # Imprime comentario. 
```
--- 

Avanzando, nos encontramos con el siguiente punto. 

6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

Para ello, desarrolle el siguiente código. 

```Python
LLENAR 
```
---

Ahora bien, observamos el siguiente punto. 

7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9. 

Para ello desarrolle el siguiente código. 

```Python
# Tabla de multiplicar del 9 
for tablaNueve in range(9, 91, 9):  # Establecemos rango y utilizamos "for" para recorrer la colección. 
    print(tablaNueve) # Imprime 
```
---
Avanzamos con los siguientes puntos, mi némesis.

8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. 

Desarrolle el siguiente código para la solución de dicho punto.  

```Python
LLENAR
```
--- 
9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin.

Para ello, desarrolle el siguiente código. 

```Python
LLENAR 
```
---
10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin.

Para ello desarrolle el siguiente código. 

```Python
LLENA 
```

---

Bueno eso fue todo por el momento, muchas gracias por ver todo. No olvides dejar tu estrella.
