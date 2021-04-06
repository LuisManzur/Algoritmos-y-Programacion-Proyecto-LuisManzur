from Clases.jugador import Player
from play import play
import os
import time

def password_checker(password): #funcion para ver si la contraseña cumple con los requisitos.
    invalid = 0
    num = 0
    low = 0
    upper = 0
    alnum = 0

    if len(password) < 8: # se verifica si la contrase;a tiene 8 caracteres
        invalid += 1

    for i in password: # si tiene por lo menos un valor numerico
        if i.isnumeric():
            num += 1

    for i in password: # una minuscula
        if i.islower():
            low += 1
        
    for i in password:# si tiene valores alfanumericos
        if i.isalnum():
            alnum += 1
        if alnum == len(password):
            invalid += 1

    for i in password:# si tiene mayusculas
        if i.isupper():
            upper += 1
    for i in password:# si tiene algun espacio
        if i.isspace():
            invalid += 1

    if invalid == 0 and num >= 1 and low >= 1 and upper >= 1:# si cumple con estos requisitos retorna true
        return True
    else:
        return False

def new_player(players): #funcion para crear un nuevo jugador
    while True:
        try:
            username = input('\nNombre de usario: ') # se pide que se ingresen los datos
            for i in players:
                if i.username == username:
                    raise Exception
            password = input('Contraseña(8 caracteres, 1 mayuscula, 1 numero, y un caracter.): ')
            if not password_checker(password): # se llama a la funcion para validar la contraseña
                print('\nLa contraseña no cumple con los requisitos.')
                raise Exception
            age = input('Edad: ')
            if age.isnumeric():
                age = int(age)
            else:
                print('\nIntroduzca una edad valida.')
                raise Exception
            avatar = input('Avatar:\n1.- Scharifker\n2.- Eugenio Mendoza\n3.- Pelusa\n4.- Gandhi\n5.- Mando\n6.- Iron Man\n7.- El Pepe\n8.- Hitler\n9.- Bad Bunny\n10.- El Coqui\n>>> ')
            if avatar == "1": # se comprueba que avatar se ha elegido
                avatar = 'Scharifker'
            elif avatar == "2":
                avatar = 'Eugenio Mendoza'
            elif avatar == "3":
                avatar = 'Pelusa'
            elif avatar == "4":
                avatar = 'Gandhi'
            elif avatar == "5":
                avatar = 'Mando'
            elif avatar == "6":
                avatar = 'Iron Man'
            elif avatar == "7":
                avatar = 'El Pepe'
            elif avatar == "8":
                avatar = 'Hitler'
            elif avatar == "9":
                avatar = 'Bad Bunny'
            elif avatar == "10":
                avatar = 'El coqui'
            else:
                print("\nEscoge una opcion valida")
                raise Exception
            matches = []
            break
        except:
            print('Valide sus datos.')
    print('\nUsuario añadido con exito.')
    player = Player(username, password, age, avatar, matches) #se crea el objeto en la clase Player con sus distintos atributos
    player.show() # se imprimen distintos atributos como el username, el avatar y la edad
    return player

def login(players, rooms, partidas): #funcion para iniciar sesion. si no se logra en el main se imprime un mensaje de error 
    os.system('clear')
    print('\n\nIniciar sesion:')
    username = input('\nUsername: ') # se pide el username
    password = input('password: ')#se pide la contraseña
    i = 0 #contador
    while i < len(players):
        if players[i].username == username and players[i].password == password: #se comparan el nombre de usuario y la contaseña
            os.system('clear')
            print('\nSesion iniciada.')
            player = players[i] 
            lct = choose_dificulty() # se inicia la funcion de elegir dificultad 
            play(rooms, lct, player, partidas) # se inicia la funcion de jugar
            break
        else:
            i += 1


def choose_dificulty(): #funcion donde se elige la dificultad que a su vez deterina la cantidad de vidas, pistas y el tiempo de juego. Las guarda en una lista y la retorna
    while True:
        d = input('\nEliga la dificultad:\n1.- Facil: 5 vidas y 5 pistas. y un tiempo de 30 minutos.\n2.- Medio: 3 vidas y 3 pistas. y un tiempo de 25 minutos.\n3.- Difícil: 1 vida y 2 pistas. y un tiempo de 20 minutos.\n>>>  ')
        if d == '1':
            vidas = 5
            pistas = 5
            time = 1800
            break
        elif d == '2':
            vidas = 3
            pistas = 3
            time = 1500
            break
        elif d == '3':
            vidas = 1
            pistas = 2
            time = 1200
            break
        else:
            print('\nElija una opcion correcta')
    lct = [vidas, pistas, time]
    os.system('clear')
    return lct

def start_game(players, rooms, partidas):# funcion previa a iniciar el juego donde se dan distintas opciones como iniciar juego, iniciar sesion crear usuario regresar.
    if len(players) == 0: # se verifica que existan usuarios creados, si no, se le da la opcion al usuario de crear un perfil
        os.system('clear')
        print('\n Debe crear un usario para poder iniciar el juego.')
        x = input('\n Desea crear un nuevo usuario? ("S" si, "N" no): ').upper()
        if x == 'S':
            players.append(new_player(players))
    else:
        while True:
            os.system('clear')
            o = input('\nElige una opcion:\n1.- Iniciar sesion.\n2.- Crear usuario.\n3.- Volver\n>>> ')# se dan las distintas opciones
            if o == '1':
                if not login(players, rooms, partidas): # se llama a la funcion parainiciar sesion, si la funcion retorna false se imprime un mensaje de error
                    print('Usuario o contraseña incorrecto.')
                    time.sleep(1)
            elif o == '2':
                players.append(new_player(players)) #se llama a lafuncion para crear un nuevo perfil y se agregan a la lista de jugadores
            elif o == '3': # se rompe el ciclo y se regresa al main. 
                break
