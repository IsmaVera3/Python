import random
import sys

tablero = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]

print('Bienvenidos a TaTeTi', end='\n\n') 
while True:
    try:
        p1 = input('Ingrese su nombre jugador 1 : ')
        int(p1)
        print('Recuerda que no puedes introducir numeros ')
    except ValueError:
        break
while True:
    try:
        p2 = input('Ingrese su nombre jugador 2: ')
        int(p2)
        print('Recuerda que no puedes introducir numeros')
    except ValueError:
        break

jugRan = [p1,p1]
jugadores = [p1,p2,p1,p2,p1,p2,p1,p2,p1,p2]
jugadores[0] = random.choice(jugRan)
juga = ['x','o','x','o','x','o','x','o','x','o']

print(f'Bienvenidos {p1} y {p2}', end='\n\n')
print('Este es el tablero: ', end='\n\n')
print(tablero[0])
print(tablero[1])
print(tablero[2], end='\n\n')

def juego(jugadores,tablero,juga):
    while True:
        for i in range(9):
            print(f'Turno del jugador -> {jugadores[i]} <- tu ficha es:  {juga[i]}')
            print('¡recuerda que tienes del 1 al 3 para marcar tu jugada!',end='\n\n')
            x = int(input('En que rango de x quieres jugar? = '))
            y = int(input('En que rango de y quieres jugar? = '))
            if (x <= 3 and x >= 1) and (y <= 3 and y >= 1):
                if tablero[x-1][y-1] == 'x' or tablero[x-1][y-1] == 'o':
                    print('no puedes jugar en esta posicion, ya hay una ficha', end='\n\n')
                elif jugadores[i] == p1:
                    tablero[x-1][y-1] = 'x'
                elif jugadores[i] == p2:
                    tablero[x-1][y-1] = 'o'
            else:
                print(f'{jugadores[i]} te pasaste del tablero! tienes que introducir un numero del 1 al 3 para marcar tu jugada ', end='\n\n')
            x = 0
            y = 0
            print(tablero[0])
            print(tablero[1])
            print(tablero[2], end='\n\n')
            if (tablero[0][0] == 'x' and tablero[0][1] == 'x' and tablero[0][2] == 'x') or (tablero[0][0] == 'o' and tablero[0][1] == 'o' and tablero[0][2] == 'o'):
                sys.exit(print(f'Felicitaciones {jugadores[i]} has ganado'))
            if (tablero[0][0] == 'x' and tablero[1][0] == 'x' and tablero[2][0] == 'x') or (tablero[0][0] == 'o' and tablero[1][0] == 'o' and tablero[2][0] == 'o'):
                sys.exit(print(f'Felicitaciones {jugadores[i]} has ganado'))
            if (tablero[0][2] == 'x' and tablero[1][2] == 'x' and tablero[2][2] == 'x') or (tablero[0][2] == 'o' and tablero[1][2] == 'o' and tablero[2][2] == 'o'):
                sys.exit(print(f'Felicitaciones {jugadores[i]} has ganado'))
            if (tablero[2][0] == 'x' and tablero[2][1] == 'x' and tablero[2][2] == 'x') or (tablero[2][0] == 'o' and tablero[2][1] == 'o' and tablero[2][2] == 'o'):
                sys.exit(print(f'Felicitaciones {jugadores[i]} has ganado'))
            if (tablero[0][0] == 'x' and tablero[1][1] == 'x' and tablero[2][2] == 'x') or (tablero[0][0] == 'o' and tablero[1][1] == 'o' and tablero[2][2] == 'o'):
                sys.exit(print(f'Felicitaciones {jugadores[i]} has ganado'))
            if (tablero[0][2] == 'x' and tablero[1][1] == 'x' and tablero[2][0] == 'x') or (tablero[0][2] == 'o' and tablero[1][1] == 'o' and tablero[2][0] == 'o'):
                sys.exit(print(f'Felicitaciones {jugadores[i]} has ganado'))
            if (tablero[1][0] == 'x' and tablero[1][1] == 'x' and tablero[1][2] == 'x') or (tablero[1][0] == 'o' and tablero[1][1] == 'o' and tablero[1][2] == 'o'):
                sys.exit(print(f'Felicitaciones {jugadores[i]} has ganado'))
            if (tablero[0][1] == 'x' and tablero[1][1] == 'x' and tablero[2][1] == 'x') or (tablero[0][1] == 'o' and tablero[1][1] == 'o' and tablero[2][1] == 'o'):
                sys.exit(print(f'Felicitaciones {jugadores[i]} has ganado'))
        print(f'Es un Empate!')
        break
    return False

juego(jugadores,tablero,juga)
#nombre jugador
#programacion defensiva
#asignar jugadores
#sortear aletoriamente quien arranca
#Mostrar estado del tablero todo el tiempo
#si se llena el tablero se empata
