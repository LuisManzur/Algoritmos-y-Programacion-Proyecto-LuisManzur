import random
import time
from dibujos_juegos import imprimir_ahorcado, dibujo_sopa
from derivadas import derivar
import os
from cifrado_cesar import cifrado_cesar, codigo_cifrado
from sopa_letras import sopa_letras
from memoria import memoria
class Juego:
    def __init__(self, name, recompensa, reglas, requerimiento, mensaje, preguntas):
        self.name = name
        self.recompensa = recompensa
        self.reglas = reglas
        self.requerimiento = requerimiento
        self.mensaje = mensaje
        self.preguntas = preguntas
    
    def show(self):
        print(f'\n\nnombre: {self.name}\nrecompensa: {self.recompensa}\nreglas: {self.reglas}\nrequerimiento: {self.requerimiento}\npreguntas: {self.preguntas}')
    

class Ahorcado(Juego):
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)

    def play(self, player, vidas, inventory, pistas): #metodo para el jueg
        n = random.randrange(0,2) #Elige un numero random para escoger la pregunta
        q = self.preguntas[n]
        pregunta = q['question'] #Selecciona la pregunta aleatoriamente
        palabra = q['answer'] #Selecciona la palabra a ser encontrada
        n = 0 #variable para saber si volver a desplegar el juego una vez ganado 
        while True:
            if n == 1:
                break
            os.system('clear')
            print(f'\n\nJuego: {self.name}\nReglas: {self.reglas}')
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print("Ya has ganado este juego.")
                break
            if vidas <= 0: #verifica que no te hayas quedado sin vidas
                break
            
            print(f'\npregunta: {pregunta}') 
            palabra = palabra.upper()
            intentos = 6 # Numero de intentos
            option = input('\n1.- Para regresar\n2.- Para responder\n3.- Para mostrar pista\n>>> ') # muestra las opciones al jugador
            if intentos == 0: #Verifica que aun queden intentos
                print('Se te han acabado los intentos') 
            
            if option == '1':
                break
            elif option == '2': #inicia el juego
                letras_correctas = "" #Todas las letras correctas dichas por el usuario
                letras_escritas = "" #Todas las letras dichas por el usuario
                print('Tienes 6 intentos.')
                 
                while intentos > 0:
                    os.system("clear")
                    print(f'pregunta: {pregunta}') 
                    print(f'Te quedan {intentos} intentos.')
                    imprimir_ahorcado(intentos) #imprime el muñeco del ahorcado.

                    resultado = ""
                    for letra in palabra: #Mostramos las letras acertadas o guiones bajos
                        if letra in letras_correctas: 
                            resultado += letra
                        else:
                            resultado += "_"
                    print(f"             {resultado}")

                    if  resultado == palabra: #comprobamos si se ha acertado la palabra
                        print(f"\nBien {player.avatar}, has ganado el juego y has conseguido un {self.recompensa}")
                        inventory.append(self.recompensa) #agrega la recompensa al inventario
                        n = 1
                        break

                    
                    while True: #While pra introduccion de letras
                        letra = input('\nIngresa una letra: ')
                        letra = letra.upper()
                        if len(letra) != 1 or letra.isnumeric():
                            print("\nIntroduce una letra")
                        elif letra in letras_escritas:
                            print("\nYa habias escrito esa letra.")
                        else:
                            letras_escritas += letra
                            break
                    
                    if letra not in palabra: #disminuimos intentos y quitamos vidas por letras incorrectas
                        intentos -= 1 
                        vidas -= 0.25
                        print('\npierdes 0.25 vidas')
                        time.sleep(0.5)
                    else:
                        letras_correctas += letra
            elif option == '3':    #selccion aleatoria de pista
                if pistas > 0: #Verifica que tengas pistas disponibles
                    n = random.randrange(1,3)
                    if n == 1:
                        print(f"Pista: {q['clue_1']}")
                    
                    elif n == 2:
                        print(f"Pista: {q['clue_2']}")
                    
                    elif n == 3:
                        print(f"Pista: {q['clue_3']}")
                    pistas -= 1
                else:
                    print(f'Lo siento {player.avatar}, no tienes mas pistas')
                
class SopaLetras(Juego):
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)

    def play(self, player, vidas, inventory, pistas): #metodo para el juego
        self.recompensa = 'vida2'
        os.system('clear')
        print(f'\n\nJuego: {self.name}\nReglas: {self.reglas}')
        n = 1
        while True:
            if n == 2:
                break
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print(self.recompensa)
                print("Ya has ganado este juego.")
                break
            if vidas <= 0: #verifica que no te hayas quedado sin vidas
                break
            n = random.randrange(0,2) #Elige un numero random para escoger la pregunta
            q = self.preguntas[n]
            palabra1 = q['answer_1'] #se buscan las palabras de la pregunta
            palabra2 = q['answer_2']
            palabra3 = q['answer_3']
            palabra1 = palabra1.upper() #convierte en mayuscula las palabras.
            palabra3 = palabra3.upper()
            palabra2 = palabra2.upper()
            pista1 = q['clue_1'] #se buscan las pistas de la pregunta
            pista2 = q['clue_2']
            sopa_de_letras = sopa_letras(palabra1, palabra2, palabra3)
            pista3 = q['clue_3']
            correctas = []
            totales = []
            while True:
                if len(correctas) == 3:
                    print(f"\nBien {player.avatar}, has ganado el juego y has conseguido una vida extra")
                    vidas += 1 #se suma la vida 
                    n = 2
                    inventory.append(self.recompensa)
                    break
                os.system('clear')
                dibujo_sopa(sopa_de_letras) #se imprime la sopa de letras
                print('\ncorrectas:')
                if len(correctas) > 0:
                    for i in correctas:
                        print(i)
                print(f'\n\nPistas:\n1.- {pista1}\n2.- {pista2}\n3.- {pista3}') #se muestran las pistas
                respuesta = input('Respuesta: ')
                respuesta = respuesta.upper() # se le pide la respuesta al ussuario y se convierte en mayusculas
                if respuesta in totales: #verifica que no haya escrito la palabra previamente
                    print('ya habias escrito la palabra')
                elif respuesta == palabra1: #verifica si la palabra es correcta o no
                    correctas.append(respuesta)
                    totales.append(respuesta)
                elif respuesta == palabra2:
                    correctas.append(respuesta)
                    totales.append(respuesta)
                elif respuesta == palabra3:
                    correctas.append(respuesta)
                    totales.append(respuesta)
                else: # Si la palabra es incorrecta te resta la cantidad de vida determinada y agrega la palabra a la lista de dichas anteriormente
                    print('La palabra es incorrecta')
                    vidas -= 0.5
                    totales.append(respuesta)
                
class PreguntasPython(Juego):
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)
        os.system('clear')

    def play(self, player, vidas, inventory, pistas): #metodo para el juego
        os.system('clear')
        print(f'\n\nJuego: {self.name}\nReglas: {self.reglas}')
        n = random.randrange(0,2) #Elige un numero random para escoger la pregunta
        q = self.preguntas[n]
        while True:
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print("Ya has ganado este juego.")
                break
            if vidas <= 0: #verifica que no te hayas quedado sin vidas
                break
            pregunta = q['question'] #Selecciona la pregunta aleatoriamente
            print(f'\npregunta: {pregunta}') 
            i1 = 0#extremo izquierdo
            i2 = 0#extremo derecho
            i = 0
            for w in pregunta: #se busca cada extremo de la oracion
                if w == '\"':
                    if i1 != 0:
                        i2 = i
                    else:
                        i1 = i
                i += 1
            oracion = pregunta[i1+1: i2] #oracion a trabajar
            option = input('\n1.- Para regresar\n2.- Para responder\n3.- Para mostrar pista\n>>> ') # muestra las opciones al jugador
            if option == '1': # se termina el while loop
                break
            elif option == '2': #inicia el juego
                print('la variable de se llama oracion.')
                try:
                    respuesta = eval(input('\nRespuesta: ')) # se ingresa la respuesta del usuario
                except:
                    print('\ncodigo invalido.')
                    vidas -= 0.5 #se restan las vidas respectivas
                if q['answer'] == "Validar en python que de el siguiente resultado: 50.00 en formato entero": #se ve cual es la respuesta correcta
                    if respuesta == 50:
                        print(f"\nBien {player.avatar}, has ganado el juego y has conseguido un {self.recompensa}")
                        inventory.append(self.recompensa) #agrega la recompensa al inventario
                        break
                    else:
                        print('\nRespuesta invalida.')
                        vidas -= 0.5 #se restan las vidas respectivas
                elif q['answer'] == "string invertido":
                    if respuesta == 'sistemas de ingenieria metro la en estudio':
                        print(f"\n\nBien {player.avatar}, has ganado el juego y has conseguido un {self.recompensa}.")
                        inventory.append(self.recompensa) #agrega la recompensa al inventario
                        break
                    else:
                        print('\nRespuesta invalida.')
                        vidas -= 0.5 #se restan las vidas respectivas
            elif option == '3':    #selccion aleatoria de pista
                if pistas > 0: #Verifica que tengas pistas disponibles
                    n = random.randrange(1,3)
                    if n == 1:
                        print(f"Pista: {q['clue_1']}")
                    
                    elif n == 2:
                        print(f"Pista: {q['clue_2']}")
                    
                    elif n == 3:
                        print(f"Pista: {q['clue_3']}")
                    pistas -= 1
                else:
                    print(f'Lo siento {player.avatar}, no tienes mas pistas')
                
class Adivinanzas(Juego):
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)
    
    def play(self, player, vidas, inventory, pistas): #metodo para el juego
        os.system('clear')
        print(f'\n\nJuego: {self.name}\nReglas: {self.reglas}')
        n = random.randrange(0,2) #Elige un numero random para escoger la pregunta
        q = self.preguntas[n]
        while True:
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print("Ya has ganado este juego.")
                break
            if vidas <= 0: #verifica que no te hayas quedado sin vidas
                break
            pregunta = q['question'] #Selecciona la pregunta aleatoriamente
            print(f'\npregunta: {pregunta}') 
            palabras = q['answers'] #Selecciona las palabras a ser encontradas
            option = input('\n1.- Para regresar\n2.- Para responder\n3.- Para mostrar pista\n>>> ') # muestra las opciones al jugador
            if option == '1':
                break
            elif option == '2': #inicia el juego
                respuesta = input('\nRespuesta: ') # se ingresa la respuesta del usuario
                if respuesta in palabras: #se verifica que la respuesta sea correcta
                    print(f"\n\nBien {player.avatar}, has ganado el juego y has conseguido un {self.recompensa}.")
                    inventory.append(self.recompensa) #agrega la recompensa al inventario
                    break
                else:
                    print('\nRespuesta invalida.')
                    vidas -= 0.5 #se restan las vidas respectivas
            elif option == '3': # se termina el while loop
                break

class PreguntasMatematicas(Juego): 
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)
    
    def play(self, player, vidas, inventory, pistas): #Metodo para el juego
        self.recompensa = 'vida1'
        os.system("clear")
        print(f'\n\nJuego: {self.name}\nReglas: {self.reglas}')
        n = random.randrange(0,2)
        q = self.preguntas[n] #Selecciona la pregunta aleatoriamente
        while True: #Loop del juego.
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print("\nYa has ganado este juego.")
                break
            if vidas <= 0:
                break
            pregunta = q['question']
            respuesta = derivar(pregunta)
            print(f'\npregunta: {pregunta}(usa pi = 3.14)')
            option = input('\n1.- Para regresar\n2.- Para responder\n3.- Para mostrar pista\n>>> ') # muestra las opciones al jugador
            if option == '1':
                break
            elif option == '2':
                respuesta_u = input('\nRespuesta: ') # el usuario introduce la respuesta
                if respuesta_u in str(respuesta) : #Se verifica que la respuesta sea correcta
                    print(f"\n\nBien {player.avatar}, has ganado el juego y has conseguido una {self.recompensa}")
                    vidas += 1 #agrega la recompensa al inventario
                    break
                else:
                    print('\nRespuesta incorrecta pierde 1/4 de vida.')
                    vidas -= 0.25
            elif option == '3':    #selccion aleatoria de pista
                if pistas > 0: #Verifica que tengas pistas disponibles
                    n = random.randrange(1,3) #se elige aleatoriamente la pista
                    if n == 1:
                        print(f"Pista: {q['clue_1']}")
                    
                    elif n == 2:
                        print(f"Pista: {q['clue_2']}")
                    
                    elif n == 3:
                        print(f"Pista: {q['clue_3']}")
                    pistas -= 1
                else:
                    print(f'Lo siento {player.avatar}, no tienes mas pistas')

class Criptograma(Juego):
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)

    def play(self, player, vidas, inventory, pistas): #metodo para el juego
        os.system("clear")
        print(f'\n\nJuego: {self.name}\nReglas: {self.reglas}')
        while True:
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print("Ya has ganado este juego.")
                break
            if vidas <= 0: #verifica que no te hayas quedado sin vidas
                break
            n = random.randrange(0,2) #Elige un numero random para escoger la pregunta
            q = self.preguntas[n]
            pregunta = q['question'] #Selecciona la pregunta aleatoriamente
            pregunta = pregunta.replace('á', 'a')
            desplazamientos = q["desplazamiento"]
            mensaje_cifrado = cifrado_cesar(pregunta, desplazamientos) #se llama a la funcion que hara el cifrado
            print(f'Mensaje: {mensaje_cifrado}')
            print(f'\n\nDecodificador:\n{codigo_cifrado(desplazamientos)}') # Se muestran el mensaje cifrado y la chuleta
            option = input('\n1.- Para regresar\n2.- Para responder\n>>> ') # muestra las opciones al jugador
            if option == '1':
                break
            elif option == '2':
                respuesta_u = input('\nRespuesta: ') # el usuario introduce la respuesta
                if pregunta.lower() == respuesta_u.lower(): #Se verifica que la respuesta sea correcta
                    print(f"\nBien {player.avatar}, has ganado el juego y has conseguido un {self.recompensa}")
                    inventory.append(self.recompensa) #agrega la recompensa al inventario
                    break
                else:
                    print('\nRespuesta incorrecta pierde 1 vida.')
                    vidas -= 1

class EncuentraLogiga(Juego):
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)

    def play(self, player, vidas, inventory, pistas): #Metodo para el juego
        os.system("clear")
        print(f'\n\nJuego: {self.name}\nReglas: {self.reglas}')
        n = random.randrange(0,1)
        q = self.preguntas[n] #Selecciona la pregunta aleatoriamente
        while True: #Loop del juego.
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print("\nYa has ganado este juego.")
                break
            if vidas <= 0:
                break
            respuesta = int(input(f'\n{q}\nRespuesta: ')) #se le pide la respuesta al jugardor
            if n == 0:
                if respuesta == 67:
                    print(f"\nBien {player.avatar}, has ganado el juego y has conseguido un {self.recompensa}")
                    inventory.append(self.recompensa) #agrega la recompensa al inventario
                    break
                else: 
                    print('Respuesta incorrecta intentelo mas tarde.')
                    break

            elif n == 1:
                if respuesta == 41:
                    print(f"\nBien {player.avatar}, has ganado el juego y has conseguido un {self.recompensa}")
                    inventory.append(self.recompensa) #agrega la recompensa al inventario
                    break
                else: 
                    print('Respuesta incorrecta intentelo mas tarde.')
                    break
            
class QuizUnimet(Juego):
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)

    def play(self, player, vidas, inventory, pistas): #metodo para el juego
        os.system('clear')
        print(f'\n\nJuego: {self.name}\nReglas: {self.reglas}')
        n = random.randrange(0,3) #Elige un numero random para escoger la pregunta
        q = self.preguntas[n]
        while True:
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print("Ya has ganado este juego.")
                break
            if vidas <= 0: #verifica que no te hayas quedado sin vidas
                break
            pregunta = q['question'] #Selecciona la pregunta aleatoriamente
            print(f'\npregunta: {pregunta}') 
            resuesta_c = q['correct_answer'] #Selecciona las opciones de respuesta
            option = input('\n1.- Para regresar\n2.- Para responder\n3.- Para mostrar pista\n>>> ') # muestra las opciones al jugador
            if option == '1': # se termina el while loop
                break
            elif option == '2': #inicia el juego
                os.system('clear')
                print(f'\npregunta: {pregunta}\n')
                respuesta = input(f'1.- {q["correct_answer"]}\n2.- {q["answer_2"]}\n3.- {q["answer_3"]}\n4.- {q["answer_4"]}\n>>>> ') # se ingresa la respuesta del usuario
                if respuesta == '1': #se verifica que la respuesta sea correcta
                    print(f"\n\nBien {player.avatar}, has ganado el juego y has conseguido un {self.recompensa}.")
                    inventory.append(self.recompensa) #agrega la recompensa al inventario
                    break
                else:
                    print('\nRespuesta incorrecta, pierdes 0.5 vidas.')
                    vidas -= 0.5 #se restan las vidas respectivas
            elif option == '3': 
                pista = q['clue_1']
                print(f'\nPista: {pista}')
                

class MemoriaEmojis(Juego):
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)
    def play(self, player, vidas, inventory, pistas): #metodo para el juego
        os.system('clear')
        print(f'\n\nJuego: {self.name}\nReglas: {self.reglas}')
        q = self.preguntas[0]
        emojis = q['question']
        emojis =  eval(emojis)
        cartas1 = emojis[0]
        cartas2 = emojis[1]
        cartas3 = emojis[2]
        cartas4 = emojis[3]
        while True:
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print("Ya has ganado este juego.")
                break
            if vidas <= 0: #verifica que no te hayas quedado sin vidas
                break
            option = input('\n1.- Para regresar\n2.- Para responder\n>>> ') # muestra las opciones al jugador
            if option == '1':
                break
            elif option == '2': #inicia el juego
                memoria(cartas1, cartas2, cartas3, cartas4, vidas)
                print(f"\n\nBien {player.avatar}, has ganado el juego y has conseguido un {self.recompensa}.")
                inventory.append(self.recompensa) #agrega la recompensa al inventario
                break
class LogicaBoolena(Juego):
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)
    def play(self, player, vidas, inventory, pistas, abierto): #metodo para el juego
        os.system('clear')
        print(f'\n\nJuego: {self.name}\nReglas: {self.reglas}')
        n = random.randrange(0,2) #Elige un numero random para escoger la pregunta
        q = self.preguntas[n]
        while True:
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print("Ya has ganado este juego.")
                break
            if vidas <= 0: #verifica que no te hayas quedado sin vidas
                break
            pregunta = q['question'] #Selecciona la pregunta aleatoriamente
            print(f'\npregunta: {pregunta}')
            respuesta1 = q['answer'] #Selecciona la respuesta
            option = input('\n1.- Para regresar\n2.- Para responder\n>>> ') # muestra las opciones al jugador
            if option == '1': # se termina el loop
                break
            elif option == '2': #inicia el juego
                respuesta = input('\nRespuesta (True or False): ').title() # se ingresa la respuesta del usuario
                if respuesta == respuesta1: #se verifica que la respuesta sea correcta
                    print(f"\n\nBien {player.avatar}, has ganado el juego y has conseguido un {self.recompensa}.")
                    inventory.append('Puerta Lab')
                    vidas += 1
                    break
                else:
                    print('\nRespuesta invalida.')
                    vidas -= 0.5 #se restan las vidas respectivas

class JuegoLibre(Juego):
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)
    def play(self, player, vidas, inventory, pistas): #metodo para el juego
        os.system('clear')
        print(f'\n\nJuego: La vieja\nReglas: {self.reglas}')
        while True:
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print("Ya has ganado este juego.")
                break
            if vidas <= 0: #verifica que no te hayas quedado sin vidas
                break
            jugador = 'X' #ficha del Jugador
            computadora = 'O' #ficha computadora

            def tablero(matriz):
                print('                La Vieja') # se imprime el tablero
                print("          |          |          ")
                print("1  {}      |2   {}    |3 {}          ".format(matriz[0],matriz[1], matriz[2]))
                print("          |          |          ")
                print("--------------------------------")
                print("          |          |          ")
                print("4  {}      |5   {}    |6 {}          ".format(matriz[3],matriz[4], matriz[5]))
                print("          |          |          ")
                print("--------------------------------")
                print("          |          |          ")
                print("7  {}      |8   {}    |9 {}          ".format(matriz[6],matriz[7], matriz[8]))
                print("          |          |          ")


            def empate(matriz): # se pregunta si hubo empate
                empate = True
                i = 0
                while(empate == True and i < 9):
                    if matriz[i] == " ":
                        empate= False
                    i += 1
                return empate
            def victoria(matriz): # se pregunta si hubo victoria
                if (matriz[0] == matriz[1] == matriz[2] != " " or matriz[3] == matriz[4] == matriz[5] != " " or matriz[6] == matriz[7] == matriz[8] != " " or matriz[0] == matriz[3] == matriz[6] != " " or matriz[1] == matriz[4] == matriz[7] != " " or matriz[2] == matriz[5] == matriz[8] != " " or matriz[0] == matriz[4] == matriz[8] != " " or matriz[2] == matriz[4] == matriz[6] != " " ):
                    return True
                else:
                    return False

            def movimiento(matriz, jugador): # funcion para reaizar un movimiento
                while True:
                    try:
                        posiciones = [1, 2, 3, 4, 5, 6, 7, 8, 9] #movimientos posibles
                        casilla = int(input('\nSeleccione una casilla: ')) #se pide que se seleccione una casilla
                        if casilla not in posiciones:
                            print("casilla no disponible")
                        else:
                            if matriz[casilla - 1] == " ":
                                matriz[casilla - 1] = jugador
                                break
                            else:
                                print('Casilla no disponible')
                    except:
                        print('Respuesta invalida')

            def computadora(matriz, jugador): #funcion para que juegue la computadora
                posiciones = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                casilla = 9
                parar = False
                for i in posiciones:
                    copia= list(matriz)
                    if copia[i] == " ":
                        copia[i] =  computadora
                        if victoria(copia) == True:
                            casilla = i
                if casilla == 9:
                    for j in posiciones:
                        copia = list(matriz)
                        if copia[j] == " ":
                            copia[j] = jugador
                            if victoria(copia) == True:
                                casilla = j
                if casilla == 9:
                    while(not parar):
                        casilla = random.randint(0,8)
                        if matriz[casilla] == " ":
                            parar = True
                matriz[casilla] = 'O'
            matriz = [" "] * 9
            partida = True
            ganador = 0
            o = input('\n1.-Para vovler.\n2.- Para responder\n >>')
            if o == '2':
                while partida:
                    ganador += 1
                    os.system('clear')
                    tablero(matriz)
                    if victoria(matriz):
                        if ganador %2==0:
                            inventory.append('ganaste')
                            partida = False
                        else:
                            print('gana el ordenador')
                            print('Pierdes una vida por esto.')
                            vidas -= 1
                            partida = False
                    elif empate(matriz):
                        print('empate')
                        partida = False
                    
                    elif ganador%2==0:
                        computadora(matriz, jugador)
                    else:
                        movimiento(matriz, jugador)
                break
            elif o == '1':
                break
            else:
                print('Introduzca una opcion valida.')
            os.system("clear")

class PalabraMezclada(Juego):
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)
    def play(self, player, vidas, inventory, pistas): #metodo para el juego
        os.system('clear')
        print(f'\n\nJuego: {self.name}\nReglas: {self.reglas}')
        n = 1
        while True:
            if n == 2:
                break
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print(self.recompensa)
                print("Ya has ganado este juego.")
                break
            if vidas <= 0: #verifica que no te hayas quedado sin vidas
                break
            n = random.randrange(0,2) #Elige un numero random para escoger la pregunta
            q = self.preguntas[n]
            print(f'\nCategoria: {q["category"]}')
            palabras_c = q['words']
            palabras_i = []
            respuestas = []
            for palabra in palabras_c:
                letras = [] #lista donde se agregaran las letras
                palabra_d = '' #palabra desordenada
                for i in palabra:
                    letras.append(i)#las letras de la palabra ordenada se guardan en la lista letras
                random.shuffle(letras) #se mezcla la lista letras
                for i in letras: #se forma la palabra mezclada
                    palabra_d += i
                palabras_i.append(palabra_d)
            print('\nPalabras:\n')
            for i in palabras_i:
                print(i)
            o = input('\n1.-Para vovler.\n2.-Para responder.\n>>> ')
            if o == '1':
                break
            elif o == '2':
                while True:
                    os.system('clear')
                    print('\nPalabras:\n')
                    for i in palabras_i:
                        print(i)
                    if len(respuestas) == 5:
                        print(f"\n\nBien {player.avatar}, has ganado el juego y has conseguido un {self.recompensa}.\n")
                        inventory.append(self.recompensa) #agrega la recompensa al inventario
                        n = 2
                        time.sleep(0.5)
                        break
                    else:
                        respuesta = input('\nIntroduzca una plabra: ')
                        if respuesta in palabras_c:
                            respuestas.append(respuesta)
                            print('\nPalabra Correcta!!')
                            time.sleep(0.5)
                        else:
                            print('palabra incorrecta. Pierdes -0.5 vidas')
                            vidas -= 0.5
          
class EscogeNumero(Juego):
    def __init__(self, name, recompensa, reglas, requerimiento, preguntas, mensaje):
        super().__init__(name, recompensa, reglas, requerimiento, mensaje, preguntas)
    def play(self, player, vidas, inventory, pistas): #metodo para el juego
        q = self.preguntas[0]
        intentos = 0
        pregunta = q['question']
        n = pregunta.find('entre') #busca la palabra entre en el string pregunta
        numeros = pregunta[n+6: len(pregunta)] #separa los numeros del string pregunta
        entre = numeros.find('-') #busca el separador de los numeros
        numero1 = int(numeros[0: entre]) #busca cuales son los numeros para el rango y los convierte en enteros
        numero2 = int(numeros[entre+1: len(numeros)])
        respuesta1 = random.randrange(numero1, numero2 + 1) #se selecciona el numero de la respuesta aleatoriamente
        ultima_respuesta = '' # se guarda la ultima respuesta
        while True:
            os.system('clear')
            print(f'\n\nJuego: {self.name}\nReglas: {self.reglas}')
            if self.recompensa in inventory: #Verifica si el juego ya se jugo previamente
                print(self.recompensa)
                print("Ya has ganado este juego.")
                break
            if vidas <= 0: #verifica que no te hayas quedado sin vidas
                break
            
            
            o = input('\n1.-Para vovler.\n2.-Para responder\n3.-Para mostrar pista\n>>> ') # se le dan opciones al jugador
            if o == '1':
                break
            elif o == '2': # se da paso a la respuesta
                respuesta2 = (input('Respuesta: ')) # se le pide la respuesta al usuario
                if not respuesta2.isnumeric(): # se verifica si la respuesta es numerica
                    print('introduce un numero.')
                else:
                    if respuesta1 == int(respuesta2): # se verifica que la repuestas sean iguales
                        print(f"\n\nBien {player.avatar}, has ganado el juego y has conseguido un {self.recompensa}.")
                        inventory.append(self.recompensa) #agrega la recompensa al inventario
                        break
                    
                    else: 
                        intentos +=1 #se suma un intento
                        print('\nRepuesta incorrecta.')
                        time.sleep(0.5)
                        if intentos == 3: # si se llega a tres intentos se le resta la vida correspondiente
                            print('\npierdes un cuato de  vida.')
                            vidas -= 0.25 
                            intentos = 0 # se resetean los intentos a 0
                    ultima_respuesta = respuesta2 #se iguala la ultima respuesta
            elif o == '3': #se da la pista
                if ultima_respuesta == '': # si no se ha ingresao pista se le engaña al jugador
                    print(q['clue_1'])
                elif int(ultima_respuesta) > respuesta1: #se verifica si la ultima respuesta ingresada por el ususario es mayor o menor que la respuesta correcta
                    if int(ultima_respuesta) - respuesta1 <= 5: # si  la diferencia es menor o igual a 5
                        print('Estás cerca un poco arriba')
                    else:
                        print('Estas muy arriba.')
                elif int(ultima_respuesta) < respuesta1: #se verifica si la ultima respuesta ingresada por el ususario es mayor o menor que la respuesta correcta
                    if respuesta1 - int(ultima_respuesta) <= 5: # si  la diferencia es menor o igual a 5
                        print('Estás cerca un poco abajo')
                    else:
                        print('Estas muy abajo.')
                time.sleep(0.5)
