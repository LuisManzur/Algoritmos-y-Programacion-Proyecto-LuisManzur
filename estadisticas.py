import time
def estadisticas(partidas):
    if len(partidas) > 0:
        tiempos = []
        for i in partidas:
            tiempo = i['tiempo']
            tiempos.append(tiempo)

        tiempos.sort()
        n = 1
        for i in tiempos:
            for x in partidas:
                if n <=5:
                    if i == x['tiempo']:
                        jugador = x['jugador']
                        print("_____", n, "_____")
                        print(f'Jugador: {jugador}\nTiempo: {i}')
                        n+=1
    else:
        print('\ntodavia no se han guardado partidas.')
    time.sleep(5)
