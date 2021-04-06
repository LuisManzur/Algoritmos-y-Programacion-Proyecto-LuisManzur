def imprimir_ahorcado(intentos):
    if intentos == 1:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                     / \  |
                    ______|
        """)
    elif intentos == 2:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                       \  |
                    ______|
        """)
    elif intentos == 3:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                          |
                    ______|
        """)
    elif intentos == 4:
        print("""
                       ___
                      |   |
                     _O/  |
                          |
                          |
                    ______|
        """)
    elif intentos == 5:
        print("""
                       ___
                      |   |
                      O/  |
                          |
                          |
                    ______|
        """)
    elif intentos == 6:
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """)

def dibujo_sopa(sopa_letras):
    print("                                  Sopa de letras\n")

    print('          1   2   3   4   5   6   7   8   9   10   11   12   13   14   15\n')
    print('       1 ', sopa_letras[0][0], ' ',sopa_letras[0][1], ' ',sopa_letras[0][2], ' ',sopa_letras[0][3], ' ',sopa_letras[0][4], ' ',sopa_letras[0][5], ' ',sopa_letras[0][6], ' ',sopa_letras[0][7], ' ',sopa_letras[0][8], '  ',sopa_letras[0][9], '  ',sopa_letras[0][10], '  ',sopa_letras[0][11], '  ',sopa_letras[0][12], '  ',sopa_letras[0][13], '  ',sopa_letras[0][14])
    print('       2 ', sopa_letras[1][0], ' ',sopa_letras[1][1], ' ',sopa_letras[1][2], ' ',sopa_letras[1][3], ' ',sopa_letras[1][4], ' ',sopa_letras[1][5], ' ',sopa_letras[1][6], ' ',sopa_letras[1][7], ' ',sopa_letras[1][8], '  ',sopa_letras[1][9], '  ',sopa_letras[1][10], '  ',sopa_letras[1][11], '  ',sopa_letras[1][12], '  ',sopa_letras[1][13], '  ',sopa_letras[1][14])
    print('       3 ', sopa_letras[2][0], ' ',sopa_letras[2][1], ' ',sopa_letras[2][2], ' ',sopa_letras[2][3], ' ',sopa_letras[2][4], ' ',sopa_letras[2][5], ' ',sopa_letras[2][6], ' ',sopa_letras[2][7], ' ',sopa_letras[2][8], '  ',sopa_letras[2][9], '  ',sopa_letras[2][10], '  ',sopa_letras[2][11], '  ',sopa_letras[2][12], '  ',sopa_letras[2][13], '  ',sopa_letras[2][14])
    print('       4 ', sopa_letras[3][0], ' ',sopa_letras[3][1], ' ',sopa_letras[3][2], ' ',sopa_letras[3][3], ' ',sopa_letras[3][4], ' ',sopa_letras[3][5], ' ',sopa_letras[3][6], ' ',sopa_letras[3][7], ' ',sopa_letras[3][8], '  ',sopa_letras[3][9], '  ',sopa_letras[3][10], '  ',sopa_letras[3][11], '  ',sopa_letras[3][12], '  ',sopa_letras[3][13], '  ',sopa_letras[3][14])
    print('       5 ', sopa_letras[4][0], ' ',sopa_letras[4][1], ' ',sopa_letras[4][2], ' ',sopa_letras[4][3], ' ',sopa_letras[4][4], ' ',sopa_letras[4][5], ' ',sopa_letras[4][6], ' ',sopa_letras[4][7], ' ',sopa_letras[4][8], '  ',sopa_letras[4][9], '  ',sopa_letras[4][10], '  ',sopa_letras[4][11], '  ',sopa_letras[4][12], '  ',sopa_letras[4][13], '  ',sopa_letras[4][14])
    print('       6 ', sopa_letras[5][0], ' ',sopa_letras[5][1], ' ',sopa_letras[5][2], ' ',sopa_letras[5][3], ' ',sopa_letras[5][4], ' ',sopa_letras[5][5], ' ',sopa_letras[5][6], ' ',sopa_letras[5][7], ' ',sopa_letras[5][8], '  ',sopa_letras[5][9], '  ',sopa_letras[5][10], '  ',sopa_letras[5][11], '  ',sopa_letras[5][12], '  ',sopa_letras[5][13], '  ',sopa_letras[5][14])
    print('       7 ', sopa_letras[6][0], ' ',sopa_letras[6][1], ' ',sopa_letras[6][2], ' ',sopa_letras[6][3], ' ',sopa_letras[6][4], ' ',sopa_letras[6][5], ' ',sopa_letras[6][6], ' ',sopa_letras[6][7], ' ',sopa_letras[6][8], '  ',sopa_letras[6][9], '  ',sopa_letras[6][10], '  ',sopa_letras[6][11], '  ',sopa_letras[6][12], '  ',sopa_letras[6][13], '  ',sopa_letras[6][14])
    print('       8 ', sopa_letras[7][0], ' ',sopa_letras[7][1], ' ',sopa_letras[7][2], ' ',sopa_letras[7][3], ' ',sopa_letras[7][4], ' ',sopa_letras[7][5], ' ',sopa_letras[7][6], ' ',sopa_letras[7][7], ' ',sopa_letras[7][8], '  ',sopa_letras[7][9], '  ',sopa_letras[7][10], '  ',sopa_letras[7][11], '  ',sopa_letras[7][12], '  ',sopa_letras[7][13], '  ',sopa_letras[7][14])
    print('       9 ', sopa_letras[8][0], ' ',sopa_letras[8][1], ' ',sopa_letras[8][2], ' ',sopa_letras[8][3], ' ',sopa_letras[8][4], ' ',sopa_letras[8][5], ' ',sopa_letras[8][6], ' ',sopa_letras[8][7], ' ',sopa_letras[8][8], '  ',sopa_letras[8][9], '  ',sopa_letras[8][10], '  ',sopa_letras[8][11], '  ',sopa_letras[8][12], '  ',sopa_letras[8][13], '  ',sopa_letras[8][14])
    print('      10 ', sopa_letras[9][0], ' ',sopa_letras[9][1], ' ',sopa_letras[9][2], ' ',sopa_letras[9][3], ' ',sopa_letras[9][4], ' ',sopa_letras[9][5], ' ',sopa_letras[9][6], ' ',sopa_letras[9][7], ' ',sopa_letras[9][8], '  ',sopa_letras[9][9], '  ',sopa_letras[9][10], '  ',sopa_letras[9][11], '  ',sopa_letras[9][12], '  ',sopa_letras[9][13], '  ',sopa_letras[9][14])
    print('      11 ', sopa_letras[10][0], ' ',sopa_letras[10][1], ' ',sopa_letras[10][2], ' ',sopa_letras[10][3], ' ',sopa_letras[10][4], ' ',sopa_letras[10][5], ' ',sopa_letras[10][6], ' ',sopa_letras[10][7], ' ',sopa_letras[10][8], '  ',sopa_letras[10][9], '  ',sopa_letras[10][10], '  ',sopa_letras[10][11], '  ',sopa_letras[10][12], '  ',sopa_letras[10][13], '  ',sopa_letras[10][14])
    print('      12 ', sopa_letras[11][0], ' ',sopa_letras[11][1], ' ',sopa_letras[11][2], ' ',sopa_letras[11][3], ' ',sopa_letras[11][4], ' ',sopa_letras[11][5], ' ',sopa_letras[11][6], ' ',sopa_letras[11][7], ' ',sopa_letras[11][8], '  ',sopa_letras[11][9], '  ',sopa_letras[11][10], '  ',sopa_letras[11][11], '  ',sopa_letras[11][12], '  ',sopa_letras[11][13], '  ',sopa_letras[11][14])
    print('      13 ', sopa_letras[12][0], ' ',sopa_letras[12][1], ' ',sopa_letras[12][2], ' ',sopa_letras[12][3], ' ',sopa_letras[12][4], ' ',sopa_letras[12][5], ' ',sopa_letras[12][6], ' ',sopa_letras[12][7], ' ',sopa_letras[12][8], '  ',sopa_letras[12][9], '  ',sopa_letras[12][10], '  ',sopa_letras[12][11], '  ',sopa_letras[12][12], '  ',sopa_letras[12][13], '  ',sopa_letras[12][14])
    print('      14 ', sopa_letras[13][0], ' ',sopa_letras[13][1], ' ',sopa_letras[13][2], ' ',sopa_letras[13][3], ' ',sopa_letras[13][4], ' ',sopa_letras[13][5], ' ',sopa_letras[13][6], ' ',sopa_letras[13][7], ' ',sopa_letras[13][8], '  ',sopa_letras[13][9], '  ',sopa_letras[13][10], '  ',sopa_letras[13][11], '  ',sopa_letras[13][12], '  ',sopa_letras[13][13], '  ',sopa_letras[13][14])
    print('      15 ', sopa_letras[14][0], ' ',sopa_letras[14][1], ' ',sopa_letras[14][2], ' ',sopa_letras[14][3], ' ',sopa_letras[14][4], ' ',sopa_letras[14][5], ' ',sopa_letras[14][6], ' ',sopa_letras[14][7], ' ',sopa_letras[14][8], '  ',sopa_letras[14][9], '  ',sopa_letras[14][10], '  ',sopa_letras[14][11], '  ',sopa_letras[14][12], '  ',sopa_letras[14][13], '  ',sopa_letras[14][14])
            
