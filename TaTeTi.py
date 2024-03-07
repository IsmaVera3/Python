from random import*



tablero = [['.', '.', '.'],
           ['.', '.', '.'],
           ['.', '.', '.']]



x = 0
y = 0
p1 = ''
p2 = ''

print('Bienvenidos a TaTeTi') 
while True:
    try:
        p1 = input("Ingrese su nombre jugador 1 : ")
        int(p1)
        print("Por favor, ingrese un nombre válido, no un número.")
    except ValueError:
        break
while True:
    try:
        p2 = input("Ingrese su nombre jugador 2: ")
        int(p2)
        print("Por favor, ingrese un nombre válido, no un número.")
    except ValueError:
        break

print(f'Bienvenidos {p1} y {p2}')

jugadores = [p1,p2,p1,p2,p1,p2,p1,p2,p1,p2]
juga = ['x','o','x','o','x','o','x','o','x','o']

def juego(jugadores,x,y,tablero,juga):
    while True:
        for i in range(9):
            print(f'Turno del jugador: {jugadores[i]} vas a ser {juga[i]}')
            x = int(input('En que rango de x quieres jugar? = '))
            y = int(input('En que rango de y quieres jugar? = '))
            if (x <= 3 and x >= 1) and (y <= 3 and y >= 1):
                if tablero[x-1][y-1] == 'x' or tablero[x-1][y-1] == 'o':
                    print('no puedes jugar en esta posicion, ya hay una ficha')
                elif jugadores[i] == p1:
                    tablero[x-1][y-1] = 'x'
                elif jugadores[i] == p2:
                    tablero[x-1][y-1] = 'o'
            else:
                print(f'{jugadores[i]} te pasaste del tablero! pierdes el turno')
            x = 0
            y = 0
            print(tablero[0])
            print(tablero[1])
            print(tablero[2])
            if tablero[0][0] == 'x' and tablero[0][1] == 'x' and tablero[0][2] == 'x':
                print(f'Felicitaciones {jugadores[0]} has ganado')
                break
            if tablero[0][0] == 'x' and tablero[1][0] == 'x' and tablero[2][0] == 'x':
                print(f'Felicitaciones {jugadores[0]} has ganado')
                break
            if tablero[0][2] == 'x' and tablero[1][2] == 'x' and tablero[2][2] == 'x':
                print(f'Felicitaciones {jugadores[0]} has ganado')
                break
            if tablero[2][0] == 'x' and tablero[2][1] == 'x' and tablero[2][2] == 'x':
                print(f'Felicitaciones {jugadores[0]} has ganado')
                break
            if tablero[0][0] == 'x' and tablero[1][1] == 'x' and tablero[2][2] == 'x':
                print(f'Felicitaciones {jugadores[0]} has ganado')
                break
            if tablero[0][2] == 'x' and tablero[1][1] == 'x' and tablero[2][0] == 'x':
                print(f'Felicitaciones {jugadores[0]} has ganado')
                break
            if tablero[1][0] == 'x' and tablero[1][1] == 'x' and tablero[1][2] == 'x':
                print(f'Felicitaciones {jugadores[0]} has ganado')
                break
            if tablero[0][1] == 'x' and tablero[1][1] == 'x' and tablero[2][1] == 'x':
                print(f'Felicitaciones {jugadores[0]} has ganado')
                break



            if tablero[0][0] == 'o' and tablero[0][1] == 'o' and tablero[0][2] == 'o':
                print(f'Felicitaciones {jugadores[1]} has ganado')
                break
            if tablero[0][0] == 'o' and tablero[1][0] == 'o' and tablero[2][0] == 'o':
                print(f'Felicitaciones {jugadores[1]} has ganado')
                break
            if tablero[0][2] == 'o' and tablero[1][2] == 'o' and tablero[2][2] == 'o':
                print(f'Felicitaciones {jugadores[1]} has ganado')
                break
            if tablero[2][0] == 'o' and tablero[2][1] == 'o' and tablero[2][2] == 'o':
                print(f'Felicitaciones {jugadores[1]} has ganado')
                break
            if tablero[0][0] == 'o' and tablero[1][1] == 'o' and tablero[2][2] == 'o':
                print(f'Felicitaciones {jugadores[1]} has ganado')
                break
            if tablero[0][2] == 'o' and tablero[1][1] == 'o' and tablero[2][0] == 'o':
                print(f'Felicitaciones {jugadores[1]} has ganado')
                break
            if tablero[1][0] == 'o' and tablero[1][1] == 'o' and tablero[1][2] == 'o':
                print(f'Felicitaciones {jugadores[1]} has ganado')
                break
            if tablero[0][1] == 'o' and tablero[1][1] == 'o' and tablero[2][1] == 'o':
                print(f'Felicitaciones {jugadores[1]} has ganado')
                break
        break
    return False


juego(jugadores,x,y,tablero,juga)
#nombre jugador
#programacion defensiva
#asignar jugadores
#sortear aletoriamente quien arranca
#Mostrar estado del tablero todo el tiempo
#si se llena el tablero se empata
