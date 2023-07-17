'''Funciones'''

'''1. Ejercicio: Define una función que tome dos números y retorne su suma.'''
def suma(numero1, numero2):
    print(numero1 + numero2)
    return(numero1 + numero2)
suma(4,5)

'''2. Ejercicio: Define una función que tome un número y retorne su factorial.'''
def factorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado
numero = 5
total = factorial(numero)
print(f"El factorial de {numero} es: {total}")

'''3. Ejercicio: Define una función que tome un número y determine si es primo.'''
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero = 17
if es_primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")

'''4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.'''
def suma_numeros(lista_numeros):
  x = 0
  for y in lista_numeros:
    x += y
  return (x)
lista1 = suma_numeros([3,6,8,12,14])
print(lista1)

'''5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa'''
def revertir_cadena(texto):
  cadena_invertida = texto[::-1]
  return cadena_invertida
texto_invertido = revertir_cadena('hola mundo')
print(texto_invertido)