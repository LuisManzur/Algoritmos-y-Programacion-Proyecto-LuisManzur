import requests
import os
from Clases.jugador import Player
from start import start_game
from instrucciones import instrucciones
from Clases.juego import Juego, Ahorcado, SopaLetras, PreguntasPython, Adivinanzas, PreguntasMatematicas, Criptograma, EncuentraLogiga, QuizUnimet, LogicaBoolena, MemoriaEmojis, JuegoLibre, PalabraMezclada, EscogeNumero
from Clases.objeto import Objeto
from Clases.cuarto import Room
from estadisticas import estadisticas

def bring_api(): # se llama a la api y se reorna un json
    url = "https://api-escapamet.vercel.app/" 
    api = requests.request('Get', url).json()
    return api

def game(api, games): #se  buscan los distintos juegos en la api, se crean los distintos juegos como objetos con sus aributos y luego son agregados a la lista games
    for x in api:
        objects = x['objects']
        for i in objects:
            game = i['game']
            name = game['name']
            recompensa = game['award']
            reglas = game['rules']
            requerimiento = game['requirement']
            if requerimiento:
                mensaje = game['message_requirement']
            else:
                mensaje = False
            preguntas = game['questions']
            if name == 'ahorcado':
                juego = Ahorcado(name, recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)
            elif name == 'sopa_letras':
                juego = SopaLetras(name, recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)
            elif name == 'Preguntas sobre python':
                juego = PreguntasPython(name, recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)
            elif name == "Adivinanzas":
                juego = Adivinanzas(name, recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)
            elif name == 'Preguntas matemáticas':
                juego = PreguntasMatematicas(name, recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)
            elif name == 'Criptograma':
                juego = Criptograma(name, recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)
            elif name == 'Encuentra la lógica y resuelve':
                juego = EncuentraLogiga(name, recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)
            elif name == 'Quizizz Cultura Unimetana':
                juego = QuizUnimet(name, recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)
            elif name == 'memoria con emojis':
                juego = MemoriaEmojis(name, recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)
            elif name == 'Lógica Booleana':
                juego = LogicaBoolena('puerta1', recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)
            elif name == 'Juego Libre':
                juego = JuegoLibre('puerta2', recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)
            elif name == 'Palabra mezclada':
                juego = PalabraMezclada(name, recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)
            elif name == 'escoge un número entre':
                juego = EscogeNumero(name, recompensa, reglas, requerimiento, preguntas, mensaje)
                games.append(juego)

def objetct(api, games, objects): #se  buscan los distintos objetos en la api, se crean los distintos objetos como objetos con sus aributos y luego son agregados a la lista de objects
    n = 0
    i = 1
    for x in api:
        objectss = x['objects']
        for i in objectss:
            name = i['name']
            position = i['position']
            game = games[n]
            if n == 9:
                name = "Puerta Lab"
            elif n == 10:
                name = "Puerta Servidores"
            objeto = Objeto(name, position, game)
            objects.append(objeto)
            n += 1
                        
def room(api, objects, rooms): #se  buscan los distintos cuartos en la api, se crean los distintos cuartos como objetos con sus aributos y luego son agregados a la lista rooms
    c = 1
    for x in api:
        name = x['name']
        objetos = []
        objectss = x['objects']
        for i in objectss:
            for objeto in objects:
                if objeto.name == i['name']:
                    objetos.append(objeto)
                else:
                    if i['name'] == 'puerta':
                        if objeto.name == 'Puerta Lab' and c == 1:
                            objetos.append(objeto)
                            c += 1
                        elif objeto.name == "Puerta Servidores" and c == 2:
                            objetos.append(objeto)

        room = Room(name, objetos)
        rooms.append(room)
def write_partidas(partidas): #se recorre la lista partidas para guardar sus variables en la lista "ax" y luego recorrer esa lista y guardarla linea por linea en el archivo "datos_partidas.txt"
    ax=[]
    for partida in partidas:
        jugador = partida['jugador']
        tiempo = partida['tiempo']
        a = f'{jugador},{tiempo},'
        ax.append(a)
    with open('datos_partidas.txt', 'w') as f:
        for a in ax:
            f.write(f'{a}\n')
        f.close()

def write_players_file(players): #se recorre la lista players para guardar sus variables en la lista "ax" y luego recorrer esa lista y guardarla linea por linea en el archivo "datos_players.txt"
    ax = []
    for p in players:
        username = p.username
        password = p.password
        age = p.age
        avatar = p.avatar
        matches = p.matches
        a = f'{username},{password},{age},{avatar},{matches}'
        ax.append(a)
    with open('datos_players.txt', 'w') as f:
        for a in ax:
            f.write(f'{a}\n')
        f.close()
def open_partidas(partidas):
     with open('datos_partidas.txt') as f:
        for line in f:
            a = line
            n = len(a)
            i = 0
            while True:
                if a[i] == ',':
                    jugador = a[0:i]
                    a = a[i+1: n]
                    i = 0
                    break
                else:
                    i += 1
            while True:
                if a[i] == ',':
                    tiempo = a[0:i]
                    a = a[i+1: n]
                    i = 0
                    break
                else:
                    i += 1
            partida = {'jugador': jugador, 'tiempo': int(tiempo)}
            partidas.append(partida)
def open_players_file(players): # se abre el aarchivo "datos_players.txt" que contiene la informacion de los jugadores y va recorriendo linea por linea para ir ubicando la informacion especifica de cada jugador y crear un objeto en la clase player con todos sus atributos para luego ser agregado a la lista players
    with open('datos_players.txt') as f:
        for line in f:
            a = line
            n = len(a)
            i = 0
            while True:
                if a[i] == ',':
                    username = a[0:i]
                    a = a[i+1: n]
                    i = 0
                    break
                else:
                    i += 1
            while True:
                if a[i] == ',':
                    password = a[0:i]
                    a = a[i+1: n]
                    i = 0
                    break
                else:
                    i += 1
            while True:
                if a[i] == ',':
                    age = a[0:i]
                    a = a[i+1: n]
                    i = 0
                    break
                else:
                    i += 1
            while True:
                if a[i] == ',':
                    avatar = a[0:i]
                    a = a[i+1: n]
                    i = 0
                    break
                else:
                    i += 1
            matches = []
            player = Player(username, password, age, avatar, matches)
            players.append(player)
            
def main():
    api = bring_api() # se iguala la funcion que conecta con la api y lo iguala a una variable
    games = [] #lista donde se guardaran los juegos
    players = [] #lista donde se guardaran los jugado
    objects = [] #lista donde se guardaran los objetos
    rooms = [] #lisa donde se guardaran los cuartos
    partidas = []
    game(api, games) #funcion para crear los objetos de la clase juegos
    objetct(api, games, objects) #funcion para crear los objetos de la clase objetos
    room(api, objects, rooms) #funcion para crear los objetos de la clase cuartos
    open_players_file(players) # funcion para abrir el archivo donde se guarda la info de los jugadores
    open_partidas(partidas) # funcion donde se encuentran las partidas
    print('\n\nBienvenid@ a Escapamet')
    while True: #loop para darle las opciones al jugador
        os.system('clear')
        option = input('\nElige una opcion:\n1.- Comenzar Partida.\n2.- Ver instrucciones del juego.\n3.- ver los records.\n4.- Salir\n>>> ') #se dan las distintas opciones
        if option == '1': # se verifica la opcion seleccionada
            start_game(players, rooms, partidas) #se inicia la funcion de inicio de juego
        elif option == '2':
            instrucciones() # se llamaa a la funcion que muestra las instruccion 
        elif option == '3':
            estadisticas(partidas)
        elif option == '4':
            write_players_file(players) #se escribe sobre el archivo la info de los jugadores
            write_partidas(partidas)
            print('Hasta Luego.')
            break # se cierra el programa

main() # se llama a la funcion main