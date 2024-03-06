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



def juego(p1,p2,x,y,tablero):
    while True:
        
        print('Turno del jugador: ' + p1 + ' vas a ser x')
        x = input('En que rango de x quieres jugar?')
        y = input('En que rango de y quieres jugar?')
        tablero[x][y] = 'x'
        print(tablero)
        break


juego(p1,p2,x,y,tablero)
#nombre jugador
#programacion defensiva
#asignar jugadores
#sortear aletoriamente quien arranca
#Mostrar estado del tablero todo el tiempo
#si se llena el tablero se empata