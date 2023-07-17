'''Bucles y Funciones'''

'''1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci.'''
def fibonacci(n):
    if n <=1 :
        return n
    else:
        return fibonacci(n-2) + fibonacci (n-1)
maximo = 3
for iterador in range(maximo):
    print(fibonacci(iterador))

'''2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores'''
def obtener_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores
numero = 6
print(obtener_divisores(numero))

'''3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.'''
def list_unique(lista_elementos):
    elementos_unicos = []
    for i in lista_elementos:
        if i not in elementos_unicos:
            elementos_unicos.append(i)
    return elementos_unicos
lista1 = ['tomates','naranjas','platanos','naranjas','kiwis','platanos']
print(list_unique(lista1))

'''4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.'''
def suma_digitos(numero):
  suma = 0
  for digito in str(numero):
    suma += int(digito)
  return suma
numero =  53394
print(suma_digitos(numero))

'''5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena.'''
def vocales_cadena(cadena):
    contador = 0
    vocales ='aeiouAEIOU'
    for vocal in cadena:
        if vocal in vocales:
            contador += 1
    return contador

texto = 'los niños juegan en el parque'
print(vocales_cadena(texto))

'''6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.'''
def primeros_elementos_lista(lista,n):
    return lista [:n]
lista_elementos = [1,2,'patata',34,4,'coche']
n = 4
primeros_elementos = primeros_elementos_lista(lista_elementos,n)
print(primeros_elementos)

'''7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena.'''
def upper_lower(cadena):
    upper = 0
    lower = 0
    for caracter in cadena:
        if caracter.isupper():
            upper += 1
        elif caracter.islower():
            lower += 1
    return upper, lower
cadena = "Esto Es Una Prueba Con un TEXTO"
resultado = upper_lower(cadena)
print(resultado)

'''8. Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.'''
def is_numero_perfecto(numero):
    suma_divisores = 0
    for divisores in range(1,int(numero/2)+1):
        if numero % divisores == 0:
            suma_divisores += divisores
    if suma_divisores == numero:
        return True
    else:
        return False
numero = 496
resultado = is_numero_perfecto(numero)
if resultado == True:
    print(f'{numero} es un numero perfecto')
else: print(f'{numero} no es un numero perfecto') 

'''9. Ejercicio: Define una función que reciba un número y retorne su
representación en binario'''

def numero_binario(numero):
    binario = []
    while numero >=1:
        if numero % 2 == 0:
            binario.append(0)
        else:
            binario.append(1)
        numero = numero // 2
    return binario[::-1]
numero = 79
resultado = numero_binario(numero)
print(resultado)

'''10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas).'''
def interseccion_listas(lista1,lista2):
    lista_final = []
    for listas in lista1:
        if listas in lista2:
            lista_final.append(listas)
    return lista_final
lista1 = [10,20,30,40]
lista2 = [5,10,15,20,25,30,35,40]
resultado = interseccion_listas(lista1,lista2)
print(resultado)

'''11. Ejercicio: Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''
def is_palindromo(cadena):
    if cadena == cadena[::-1]:
        return True
cadena = 'radar'
resultado = is_palindromo(cadena)
if resultado == True:
    print(f'{cadena} es un palindromo')
else: print(f'{cadena} no es un palindromo')

'''12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para
múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de
cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco
imprima “FizzBuzz”'''
def numbers_FizzBuzz(numbers):
    lista_final = []
    for listas in numbers:
        if listas % 3 == 0 and listas % 5 == 0:
            lista_final.append('FizzBuzz')
        elif listas % 3 == 0:
            lista_final.append('Fizz')
        elif listas % 5 == 0:
            lista_final.append ('Buzz')
        else: lista_final.append(listas)
    return lista_final
resultado = numbers_FizzBuzz(range(1,51))
print(resultado)

'''13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en
orden ascendente.'''
def lista_ascendente(lista):
    return sorted(lista, reverse=False)
lista_1 = [4,5,3,2,7,12,4,13,11]
resultado = lista_ascendente(lista_1)
print(resultado)

'''14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n.'''
def palabras_mas_largas_n(lista,n):
    lista_final = []
    for palabra in lista:
        if len(palabra) > n:
            lista_final.append(palabra)
    return(lista_final)
lista = ['sauce', 'olivo', 'pino', 'haya', 'roble']
numero = 4
resultado = palabras_mas_largas_n(lista,numero)
print(resultado)

'''15. Ejercicio: Define una función que tome un número y calcule su serie de
Fibonacci.'''
def fibonacci_numero(n):
    if n <= 1:
        return n
    else:
        return fibonacci_numero(n-2) + fibonacci_numero(n-1)

n = 3
resultado = fibonacci_numero(n)
print(resultado)

'''16. Ejercicio: Define una función que tome una lista de números y retorne el
número más grande de la lista.
'''
def maximo(lista):
    return max(lista)
lista = [5,6,7]
resultado = maximo(lista)
print(resultado)

'''17. Ejercicio: Define una función que reciba un número y retorne la suma de sus
dígitos al cubo'''
def suma_digitos_cubo(n):
    total = 0
    for i in str(n):
        total += int(i) ** 3
    return total
n = 222
resultado = suma_digitos_cubo(n)
print(resultado)

'''18. Ejercicio: Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista.'''
def segundo_numero_max(lista):
    maximo = max(lista)
    lista.remove(maximo)
    segundo_maximo = max(lista) 
    return segundo_maximo
lista = [7,12,13,24,8]
resultado = segundo_numero_max(lista)
print(resultado)

'''19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False'''
def listas_comun(lista1, lista2):
    lista_final = []
    for element in lista1:
        if element in lista2:
            lista_final.append(element)
    return lista_final
lista_1 = ['Courtois', 'Alaba', 'Modric']
lista_2 = ['Kroos', 'Vinicius', 'Alaba']
resultado = listas_comun(lista_1,lista_2)
print(resultado)

'''20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso.'''
def lista_inversa(lista):
    return lista[::-1]
lista = [4,5,6]
resultado = lista_inversa(lista)
print(resultado)

'''21. Ejercicio: Define una función que reciba una cadena y cuente el número de
dígitos y letras que contiene.'''
def contar_elementos(cadena):
    contador_digitos = 0
    contador_letras = 0
    for elementos in str(cadena):
        if elementos.isdigit():
            contador_digitos += 1
        else: contador_letras += 1
    return f'En esta cadena hay {contador_digitos} digitos y {contador_letras} letras'
cadena = 'madrid36'
resultado = contar_elementos(cadena)
print(resultado)

'''22. Ejercicio: Define una función que reciba una lista de números y retorne la
suma acumulada de los números'''
def suma_acumulada(lista_numeros):
    total = 0
    total_acumulado = []
    for numeros in lista_numeros:
        total += numeros
        total_acumulado.append(total)
    return f'La suma acumulada de los números es {total_acumulado}'
lista_numeros = {10,20,30}
resultado = suma_acumulada(lista_numeros)
print(resultado)

'''23. Ejercicio: Define una función que encuentre el elemento más común en una
lista.'''
def encontrar_elemento_mas_comun(lista):
    contador = {}
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    print(contador)
    elemento_mas_comun = None
    maximo_contador = 0
    for elemento, count in contador.items():
        if count > maximo_contador:
            maximo_contador = count
            elemento_mas_comun = elemento
    return f'El elemento más común en la lista es {elemento_mas_comun} con un total de {maximo_contador} veces'
mi_lista = [1, 9, 3, 9, 17, 2, 12, 6, 6]
elemento_comun = encontrar_elemento_mas_comun(mi_lista)
print(elemento_comun)

'''24. Ejercicio: Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10.'''
def tabla_multiplicar(numero):
    diccionario = {}
    for tabla in range(1,11):
        multiplicacion = numero * tabla
        diccionario[tabla] = multiplicacion
    return diccionario
numero = 5
resultado = tabla_multiplicar(numero)
print(resultado)

'''25. Ejercicio: Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena.'''
def apariciones_cadena(cadena):
    contador = {}
    for elemento in str(cadena):
        if elemento in contador:
            contador[elemento] += 1
        else: contador[elemento] = 1
    maximo_contador = 0
    caracter_mas_comun =  None
    for elemento, count in contador.items():
        if count > maximo_contador:
            maximo_contador = count
            caracter_mas_comun = elemento
    return maximo_contador, caracter_mas_comun
cadena = 'Losgatostienenhambre'
resultado = apariciones_cadena(cadena)
print(resultado)

'''26. Ejercicio: Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas.'''
def elementos_unavez(lista1, lista2):
    lista_final = []
    for elemento in lista1:
        if elemento not in lista_final:
            lista_final.append(elemento)
    for elemento in lista2:
        if elemento in lista_final:
            lista_final.remove(elemento)
        else: lista_final.append(elemento)
    return(lista_final)
lista1 = ['azul','blanco','rojo','verde']
lista2 = ['azul','blanco','amarillo','verde']
resultado = elementos_unavez(lista1,lista2)
print(resultado)

'''27. Ejercicio: Define una función que tome una lista y retorne la lista sin
duplicados.'''
def lista_sin_duplicados(lista):
    lista_final = []
    for elemento in lista:
        if elemento not in lista_final:
            lista_final.append(elemento)
    return lista_final
lista = ['tomates','lechugas','queso','aguacate','tomates','queso']
resultado = lista_sin_duplicados(lista)
print(resultado)

'''28. Ejercicio: Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese
número'''
def suma_cuadrados_pares_menores_igual(n):
    numero = n
    suma = 0
    while n > 1:
        if n % 2 == 0:
            suma += n ** 2
            n = n-1
        else: 
            n = n -1
    return suma
n = 6
resultado = suma_cuadrados_pares_menores_igual(n)
print(resultado)

'''29. Ejercicio: Define una función que reciba una lista de números y retorne el
promedio de los números en la lista.'''
def promedio_lista(numeros):
    sum(numeros)
    promedio = sum(numeros) / len(numeros)
    return promedio
numeros = [2,4,3]
resultado = promedio_lista(numeros)
print(resultado)

'''30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista.'''
def cadena_mas_larga(lista_cadenas):
    maximo = 0
    cadena_maxima = ''
    for cadena in lista_cadenas:
        if len(cadena) > maximo:
            maximo = len(cadena)
            cadena_maxima = cadena
    return f'{cadena_maxima} es la cadena más larga de la lista'
lista_cadenas =['losniños','juegan','enelparque']
resultado = cadena_mas_larga(lista_cadenas)
print(resultado)

'''31. Ejercicio: Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos.'''
def lista_primos(entero, n):
    lista = []
    contador = 0
    if entero > 1:
        for i in range(2, entero + 1):
            es_primo = True
            for j in range(2, i):
                if i % j == 0:
                    es_primo = False
                    break
            if es_primo:
                lista.append(i)
                contador += 1
                if contador == n:
                    break
    return lista[::-1]
entero = 6
n = 3
resultado = lista_primos(entero, n)
print(resultado)

'''32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.'''   
def invertir_palabras(cadena):
    palabras = cadena.split()
    palabras_invertidas = palabras[::-1]
    cadena_invertida = ' '.join(palabras_invertidas)
    return cadena_invertida
cadena = "Hola Mundo Python"
cadena_invertida = invertir_palabras(cadena)
print(cadena_invertida) 

'''33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.'''
def ordenar_por_ultimo_elemento(lista_tuplas):
    lista_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[-1])
    return lista_ordenada
lista_tuplas = [(1, 4), (2, 2), (3, 5), (4, 1)]
lista_ordenada = ordenar_por_ultimo_elemento(lista_tuplas)
print(lista_ordenada)

'''34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena.'''
def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador
cadena = "Hola Mundo"
cantidad_vocales = contar_vocales(cadena)
print(cantidad_vocales)

'''35. Ejercicio: Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False.'''
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero =766
resultado = es_primo(numero)
print(resultado)
