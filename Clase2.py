#cadenas son objetos

str1 = 'isma'

print('La cantidad de letras de tu nombre es: ', len(str1))


#input guarda siempre como cadena

print('ingrese un numero:')

n = input()

print('el siguiente numero es: ' + str(int(n)+1))


#condiciones or expresiones booleanas

5<6 and 6<9

#while 

num1 = 1

while num1<10:
    print('hola')
    num1 += 1
    break

#continue

numero = 5
while numero >0:
    numero-=1;
    continue
    print('hola')


#for

cad = 'belgrano'

#imprime letra por letra hacia atras
for i in range(len(cad)-1 ,-1,-1):
    print(cad[i])


#range
for i in range(3,10,2):#start, end, step
    print(i)


#modulos
import random
if 8<9:
    print(random.randint(0,10))    

#pip install requests
    
#import sys cierra todo el archivo

#funciones
    
def calcular(a,b):
    return a + b
#scope (variables)
a = 1
print(f'el resultado es: {calcular(2,3)}')
print(f'la variable a vale: {a}')

#listas

