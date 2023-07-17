'''Bucles'''
'''1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .'''
'''1a'''
max = 10
number = 1
for iterador in range(max):
  print (number)
  number +=1

'''2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .'''
number2 = 2
while number2 % 2 == 0 and number2<= 20:
  print(number2)
  number2 +=2

'''3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.'''
number3 = 0
max2 = 100
total = 0
for totales in range(max2):
  number3 +=1
  total = total + number3
print(total)
  