import random
from dibujos_juegos import dibujo_sopa
def sopa_letras(palabra1,palabra2,palabra3): #funcion que creara la matriz con la sopa de letras
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' ,'K' ,'L' ,'M' ,'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T' ,'U' ,'V' ,'W' ,'X' ,'Y' ,'Z']
    sopa_letrass = [None] * (15)
    
    for i in range(0, 15): #escoge aleatoriamente para cada casilla i/j una letra
        sopa_letrass[i] = [None] * 15 
    for i in range(15):
        for j in range(15):
            sopa_letrass[i][j] = abc[random.randint(0, 25)] 

    for i in range (len(palabra1)): #ubica las palabras letra por letra en la sopa de letras
        sopa_letrass[i][0] = palabra1[ i ]
    for i in range(len(palabra2)):
        sopa_letrass[9][i+3] = palabra2[ i ]
    for i in range(len(palabra3)):
        sopa_letrass[i][9] = palabra3[ i ]
    
    dibujo_sopa(sopa_letrass)
    return sopa_letrass