import random
import os
import time
def memoria(cartas1, cartas2, cartas3, cartas4, vidas):# funcion del juego de memoria
    linea1 =  ['🎴', '🎴', '🎴', '🎴'] # listas 4*4 con los emojis volteados
    linea2 =  ['🎴', '🎴', '🎴', '🎴']
    linea3 =  ['🎴', '🎴', '🎴', '🎴']
    linea4 =  ['🎴', '🎴', '🎴', '🎴']
    random.shuffle(cartas1) # se mezclan las listas con los emojis
    random.shuffle(cartas2)
    random.shuffle(cartas3)
    random.shuffle(cartas4)
    memoria1 = [None] * 4 # se crea la matriz de los emojis a conseguir
    for i in range(0, 4):
        memoria1[i] = [None] * 4
    for i in range(4):
        memoria1[0][i] = cartas1[ i ];
        memoria1[1][i] = cartas2[ i ];
        memoria1[2][i] = cartas3[ i ];
        memoria1[3][i] = cartas4[ i ]
    while True:
        os.system('clear')
        memoria2 = [None] * 4  #se crea la lista con los emojis volteados
        for i in range(0, 4):
            memoria2[i] = [None] * 4
        for i in range(4):
            memoria2[0][i] = linea1[ i ];
            memoria2[1][i] = linea2[ i ];
            memoria2[2][i] = linea3[ i ];
            memoria2[3][i] = linea4[ i ]
        if memoria1 == memoria2:
            break
        else: # SE IMPRIME EL TABLERO
            print('         Memoria')
            print('  0    1    2    3    4')
            print()
            print('  1  ', memoria2[0][0], ' ',  memoria2[0][1], ' ',  memoria2[0][2], ' ',  memoria2[0][3] )
            print()
            print('  2  ', memoria2[1][0], ' ',  memoria2[1][1], ' ',  memoria2[1][2], ' ',  memoria2[1][3] )
            print()
            print('  3  ', memoria2[2][0], ' ',  memoria2[2][1], ' ',  memoria2[2][2], ' ',  memoria2[2][3] )
            print()
            print('  4  ', memoria2[3][0], ' ',  memoria2[3][1], ' ',  memoria2[3][2], ' ',  memoria2[3][3] )
            try:
                print()
                x1 = int(input('Escribe la cordenada X: '))# se piden las cordenadas de la primera carta
                y1 = int(input('Escribe la cordenada Y: '))
                carta1 = memoria1[y1-1][x1-1]
                print(f'Has destapado "{carta1}"')
                x2 = int(input('Escribe la cordenada X: '))# se piden las cordenadas de la segunda carta
                y2 = int(input('Escribe la cordenada Y: '))
                carta2 = memoria1[y2-1][x2-1]
                print(f'Has destapado "{carta2}"')
                if x1 == x2 and y1 == y2:
                    print('La carta no puede ser la misma')
                if carta1 != carta2:
                    print('\nPierdes 0.25 vidas')
                    vidas -= 0.25
                elif carta1 == carta2:
                    if y1 == 1:
                        linea1[x1-1] = carta1
                    elif y1 == 2:
                        linea2[x1-1] = carta1
                    elif y1 == 3:
                        linea3[x1-1] = carta1
                    elif y1 == 4:
                        linea4[x1-1] = carta1
                    if y2 == 1:
                        linea1[x2-1] = carta1
                    elif y2 == 2:
                        linea2[x2-1] = carta1
                    elif y2 == 3:
                        linea3[x2-1] = carta1
                    elif y2 == 4:
                        linea4[x2-1] = carta1
            except:
                print('Debe ser un numero entre 1-4.')
            time.sleep(3)