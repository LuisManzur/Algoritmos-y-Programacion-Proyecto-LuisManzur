partidas = [{'jugador': 'Tululo', 'tiempo': 13},{'jugador': 'pedro', 'tiempo': 11}]
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