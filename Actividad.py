print('Hola, te voy a pedir la cantidad de numeros que quiere ingresar')

num = input()

nros = []

for i in range(int(num)):
    print(f'Ingrese uno de los {num} numeros')
    try:
        nros.append(int(input()))
    except:
        print('Por favor ingresar un numero entero')
        nros.append(int(input()))



for i in range(len(nros)):
    for j in range(len(nros)-1):
        if nros[j] > nros[j+1]:
            nros[j], nros[j+1] = nros[j+1], nros[j]

print(nros)

print(f'Muy bien, ahora te pedire un numero que quieras buscar entre los {num} numeros que agregaste')

n = input()

def isIn(nros): 
    for i in range(len(nros)-1):
        if nros[len(nros)//2] == int(n):
            return True
        elif nros[len(nros)//2] > int(n):
            nros[nros[len(nros)//2]: nros[len(nros)]]
        else:   
            nros[i:len(nros)//2]
        for a in range(len(nros)):
            if int(n) == nros[a]:
                return True
            else:
                a = a + 1
    return False

isIn(nros)