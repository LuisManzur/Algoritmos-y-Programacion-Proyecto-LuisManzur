from dibujos_cuartos import mueble_de_libros, mueble_de_sentarse, mueble_con_gavetas, pizarra, computadora_1, computadora_2, saman,banquito_1, banquito_2, puerta_pasillo, puerta_servidores, rack, papelera
import random
import os
import time

def show_image(o):
    if o == 'mueble de libros':
        print(mueble_de_libros)
    elif o == 'computadora 1':
        print(computadora_1)
    elif o == 'computadora 2':
        print(computadora_2)
    elif o == 'mueble de sentarse':
        print(mueble_de_sentarse)
    elif o == 'mueble con gabetas':
        print(mueble_con_gavetas)
    elif o == 'Saman':
        print(saman)
    elif o == 'Banco 1':
        print(banquito_1)
    elif o == 'Banco 2':
        print(banquito_2)
    elif o == 'Puerta Lab':
        print(puerta_pasillo)
    elif o == 'Puerta Servidores':
        print(puerta_servidores)
    elif o == 'Rack':
        print(rack)
    elif o == 'papelera':
        print(papelera)
    elif o == 'pizarra':
        print(pizarra)

def play(rooms, lct, player, partidas): #funcion donde se realizaran todo el main del juego
    vidas = lct[0] # busca la cantidad de vidas seleccionadas por el jugador
    pistas = lct[1] # busca la cantidad pistas que puede utilizar el jugador
    tiempo1 = lct[2] #la cantidad de tiempo seleccionada por el jugador
    inventory = []
    
    
    
    print(f'\nHoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {lct[2]} minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?')

    o = input('\n"S" para si, "N" para no: ').upper() #Opcion para inicalizar el juego
    if o == 'S':
        primera = 'si' #primera imagen
        r = 'Biblioteca'
        o = 'mueble de libros'
        p = 'center'
        abierto = 'no'
        tiempo2 = time.time()
        while True:
            tiempo3 = time.time()
            tiempo = round(tiempo3 - tiempo2)
            if 'ganaste' in inventory: #verifica si ganaste
                os.system('clear')
                print('¡Felicidades! Has logrado evitar una catástrofe en la Unimet, por esto el siguiente trimestre te sale gratis.')
                partida = {'jugador': player.username, 'tiempo': tiempo/60}
                partidas.append(partida)
                time.sleep(8)
            
                break
            if tiempo1 <= tiempo: # verifica si se te acabo el tiempo
                print('\nSe te ha acabado el tiempo')
                time.sleep(5)
                break
            if vidas <= 0:
                print('\nse te han acabado las vidas')
                time.sleep(5)
                break
            if primera == 'si':
                print(f'\n\nBienvenido {player.avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente, te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto.')
                time.sleep(8)
                os.system('clear')
                primera = 'no'
            print('\nCargando...')
            time.sleep(2)
            os.system("clear")
            print(f'te quedan {(tiempo1 - tiempo)/60} minutos      vidas:{vidas}')
            show_image(o) 
            if r == 'Biblioteca': #se verifica el cuarto
                if p == 'center': # se verificala posicion dentro del cuarto
                    option = input('Para ir a la izquierda "I".\nPara ir a la derecha "D".\nPara ir a la plaza rectorado "P"\nPara ir a los laboratorios "L"\nPara inetractuar con el objeto "G"\n>>> ').upper() #se le dan al jugador las opciones de movimiento.
                    if option == 'I': #verifica la entrada
                        p = 'left'#cambia la posicion dentro del cuarto
                        for room in rooms: #busca el cuarto
                            if r == room.name: 
                                objectts = room.objetos #busca el objeto dentro del cuarto
                                for objetct in objectts: 
                                    if p == objetct.position: 
                                        o = objetct.name #cambia el nombre del objeto
                    elif option == 'D': # verifica la entrada
                        p = 'right' 
                        for room in rooms: #busca el cuarto
                            if r == room.name: #busca el objeto dentro del cuarto
                                objects = room.objetos
                                for objetct in objects:
                                    if p == objetct.position: #cambia la posicion dentro del cuarto
                                        o = objetct.name
                    elif option == 'P': #verifica la entrada
                        p = 'center' #cambia la posicion dentro del cuarto
                        r = 'Plaza Rectorado'# cambia la variable de cuarto
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects: #busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        o = objetct.name
                                        
                    elif option == 'L': # verifica la entrada
                        p = 'center' #cambia la posicion dentro del cuarto
                        r = 'Pasillo Laboratorios '# cambia la variable de cuarto
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects: #busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        o = "Puerta Lab"

                    elif option == "G": #verifica la entrada
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        g = objetct.game #juego del objeto
                                        if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                            if g.requerimiento in inventory: 
                                                g.play(player, vidas, inventory, pistas) #inicia el metodo play dentro de la clase
                                            else:
                                                print(f'\n{g.mensaje}')
                                        else:
                                            g.play(player, vidas, inventory, pistas)
                                                    
                    else:
                        print('\n Escoja una opcion valida\n')
                elif p == 'left':
                    option = input('Para ir al centro "C".\nPara ir a la derecha "D".\nPara inetractuar con el objeto "G"\n>>> ').upper()
                    if option == 'C': #verifica la entrada
                        p = 'center'#cambia la posicion dentro del cuarto
                        for room in rooms: #busca el cuarto
                            if r == room.name: 
                                objects = room.objetos #busca el objeto dentro del cuarto
                                for objetct in objects: 
                                    if p == objetct.position: 
                                        o = objetct.name #cambia el nombre del objeto
                    elif option == 'D': # verifica la entrada
                        p = 'right' 
                        for room in rooms: #busca el cuarto
                            if r == room.name: #busca el objeto dentro del cuarto
                                objects = room.objetos
                                for objetct in objects:
                                    if p == objetct.position: #cambia la posicion dentro del cuarto
                                        o = objetct.name
                    elif option == "G": #verifica la entrada
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        g = objetct.game #juego del objeto
                                        if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                            if g.requerimiento in inventory: 
                                                g.play(player, vidas, inventory, pistas)#inicia el metodo play dentro de la clase
                                            else:
                                                print(f'\n{g.mensaje}')
                                        else:
                                            g.play(player, vidas, inventory, pistas)
                    else:   
                        print('\n Escoja una opcion valida\n')             
                elif p == 'right':
                    option = input('Para ir al centro "C".\nPara ir a la Izquierda "I".\nPara inetractuar con el objeto "G".\n>>> ').upper()
                    print('\n\nCargando...')
                    if option == 'I': #verifica la entrada
                        p = 'left'#cambia la posicion dentro del cuarto
                        for room in rooms: #busca el cuarto
                            if r == room.name: 
                                objects = room.objetos #busca el objeto dentro del cuarto
                                for objetct in objects: 
                                    if p == objetct.position: 
                                        o = objetct.name #cambia el nombre del objeto
                    elif option == 'C': # verifica la entrada
                        p = 'center' 
                        for room in rooms: #busca el cuarto
                            if r == room.name: #busca el objeto dentro del cuarto
                                objects = room.objetos
                                for objetct in objects:
                                    if p == objetct.position: #cambia la posicion dentro del cuarto
                                        o = objetct.name
                    elif option == "G": #verifica la entrada
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        g = objetct.game #juego del objeto
                                        if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                            if g.requerimiento in inventory: 
                                                g.play(player, vidas, inventory, pistas)#inicia el metodo play dentro de la clase
                                            else:
                                                print(f'\n{g.mensaje}')
                                        else:
                                            g.play(player, vidas, inventory, pistas)
                    else:
                        print('\nEscoja una opcion valida\n')      
            elif r == 'Plaza Rectorado':
                if p == 'center':
                    option = input('Para ir a la izquierda "I".\nPara ir a la derecha "D".\nPara ir a la biblioteca "B".\nPara inetractuar con el objeto "G".\n>>> ').upper()
                    if option == 'I': #verifica la entrada
                        p = 'left'#cambia la posicion dentro del cuarto
                        for room in rooms: #busca el cuarto
                            if r == room.name: 
                                objects = room.objetos #busca el objeto dentro del cuarto
                                for objetct in objects: 
                                    if p == objetct.position: 
                                        o = objetct.name #cambia el nombre del objeto
                    elif option == 'D': # verifica la entrada
                        p = 'right' 
                        for room in rooms: #busca el cuarto
                            if r == room.name: #busca el objeto dentro del cuarto
                                objects = room.objetos
                                for objetct in objects:
                                    if p == objetct.position: #cambia la posicion dentro del cuarto
                                        o = objetct.name
                    elif option == "G": #verifica la entrada
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        g = objetct.game #juego del objeto
                                        if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                            if 'título Universitario' in inventory: 
                                                if 'Mensaje: Si estas gradudado puedes pisar el Samán' in inventory: 
                                                    g.play(player, vidas, inventory, pistas)#inicia el metodo play dentro de la clase
                                                else:
                                                    print(f'\n{g.mensaje}')
                                                    vidas -= 1
                                            else:
                                                print(f'\n{g.mensaje}')
                                                vidas -= 1
                                        else:
                                            g.play(player, vidas, inventory, pistas)
                    elif option == 'B':
                        p = 'center' #cambia la posicion dentro del cuarto
                        r = 'Biblioteca' #cambia la variable de cuarto
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects: #busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        o = objetct.name
                    else:
                        print('\n Escoja una opcion valida\n')
                elif p == 'left':
                    option = input('Para ir al centro "C".\nPara ir a la derecha "D".\nPara inetractuar con el objeto "G".\n>>> ').upper()
                    if option == 'C': #verifica la entrada
                        p = 'center'#cambia la posicion dentro del cuarto
                        for room in rooms: #busca el cuarto
                            if r == room.name: 
                                objects = room.objetos #busca el objeto dentro del cuarto
                                for objetct in objects: 
                                    if p == objetct.position: 
                                        o = objetct.name #cambia el nombre del objeto
                    elif option == 'D': # verifica la entrada
                        p = 'right' 
                        for room in rooms: #busca el cuarto
                            if r == room.name: #busca el objeto dentro del cuarto
                                objects = room.objetos
                                for objetct in objects:
                                    if p == objetct.position: #cambia la posicion dentro del cuarto
                                        o = objetct.name
                    elif option == "G": #verifica la entrada
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        g = objetct.game #juego del objeto
                                        if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                            if g.requerimiento in inventory: 
                                                g.play(player, vidas, inventory, pistas)#inicia el metodo play dentro de la clase
                                            else:
                                                print(f'\n{g.mensaje}')
                                        else:
                                            g.play(player, vidas, inventory, pistas)
                    else:
                        print('\n Escoja una opcion valida\n')             
                elif p == 'right':
                    option = input('Para ir al centro "C".\nPara ir a la Izquierda "I".\nPara inetractuar con el objeto "G".\n>>> ').upper()
                    if option == 'I': #verifica la entrada
                        p = 'left'#cambia la posicion dentro del cuarto
                        for room in rooms: #busca el cuarto
                            if r == room.name: 
                                objects = room.objetos #busca el objeto dentro del cuarto
                                for objetct in objects: 
                                    if p == objetct.position: 
                                        o = objetct.name #cambia el nombre del objeto
                    elif option == 'C': # verifica la entrada
                        p = 'center' 
                        for room in rooms: #busca el cuarto
                            if r == room.name: #busca el objeto dentro del cuarto
                                objects = room.objetos
                                for objetct in objects:
                                    if p == objetct.position: #cambia la posicion dentro del cuarto
                                        o = objetct.name
                    elif option == "G": #verifica la entrada
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        g = objetct.game #juego del objeto
                                        if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                            if g.requerimiento in inventory: 
                                                g.play(player, vidas, inventory, pistas)#inicia el metodo play dentro de la clase
                                            else:
                                                print(f'\n{g.mensaje}')
                                        else:
                                            g.play(player, vidas, inventory, pistas)
                    else:
                        print('\nEscoja una opcion valida\n')
            elif r == 'Pasillo Laboratorios ':
                if p == 'center':
                    option = input('Para acceder a el laboratorio "L"..\nPara ir a la biblioteca "B"\nPara inetractuar con el objeto "G".\n>>> ').upper()
                    if option == 'G':
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        if objetct.name == 'Puerta Lab':
                                            g = objetct.game #juego del objeto
                                            if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                                if g.requerimiento in inventory: 
                                                    g.play(player, vidas, inventory, pistas, abierto)#inicia el metodo play dentro de la clase
                                                else:
                                                    print(f'\n{g.mensaje}')
                                            else:
                                                g.play(player, vidas, inventory, pistas, abierto)
                    elif option == 'B':
                        p = 'center' #cambia la posicion dentro del cuarto
                        r = 'Biblioteca' #cambia la variable de cuarto
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects: #busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        o = objetct.name
                    elif option == 'L':
                        if "Puerta Lab" in inventory:
                            p = 'center' #cambia la posicion dentro del cuarto
                            r = 'Laboratorio SL001' #cambia la variable de cuarto
                            for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                                if r == room.name:
                                    objects = room.objetos
                                    for objetct in objects: #busca el objeto dentro del cuarto
                                        if p == objetct.position:
                                                o = objetct.name
                        else:
                            print('\nPrimero debes jugar con la puerta')
                            
                    else:
                        print('\nEscoja una opcion valida\n')
            elif r == 'Laboratorio SL001':
                if p == 'center': # 
                    option = input('Para ir a la izquierda "I".\nPara ir a la derecha "D".\nPara ir a la biblioteca "B".\nPara ir al cuarto de servidores "S".\nPara inetractuar con el objeto "G".\n>>> ').upper()
                    if option == 'I': #verifica la entrada
                        p = 'left'#cambia la posicion dentro del cuarto
                        for room in rooms: #busca el cuarto
                            if r == room.name: 
                                objects = room.objetos #busca el objeto dentro del cuarto
                                for objetct in objects: 
                                    if p == objetct.position: 
                                        o = objetct.name #cambia el nombre del objeto
                    elif option == 'D': # verifica la entrada
                        p = 'right' 
                        for room in rooms: #busca el cuarto
                            if r == room.name: #busca el objeto dentro del cuarto
                                objects = room.objetos
                                for objetct in objects:
                                    if p == objetct.position: #cambia la posicion dentro del cuarto
                                        o = objetct.name
                    elif option == "G": #verifica la entrada
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        g = objetct.game #juego del objeto
                                        if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                            if g.requerimiento in inventory: 
                                                g.play(player, vidas, inventory, pistas)#inicia el metodo play dentro de la clase
                                            else:
                                                print(f'\n{g.mensaje}')
                                        else:
                                            g.play(player, vidas, inventory, pistas)
                    elif option == 'B':
                        p = 'center' #cambia la posicion dentro del cuarto
                        r = 'Biblioteca' #cambia la variable de cuarto
                        for room in rooms: #verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name: 
                                objects = room.objetos
                                for objetct in objects: #busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        o = objetct.name
                    elif option == 'S':
                        p = 'center' #cambia la posicion dentro del cuarto
                        r = "Cuarto de Servidores " #cambia la variable de cuarto
                        for room in rooms: #verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name: 
                                objects = room.objetos
                                for objetct in objects: #busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        o = objetct.name
                    else:
                        print('\n Escoja una opcion valida\n')
                elif p == 'left':
                    option = input('Para ir al centro "C".\nPara ir a la derecha "D".\nPara inetractuar con el objeto "G"\n>>> ').upper()
                    if option == 'C': #verifica la entrada
                        p = 'center'#cambia la posicion dentro del cuarto
                        for room in rooms: #busca el cuarto
                            if r == room.name: 
                                objects = room.objetos #busca el objeto dentro del cuarto
                                for objetct in objects: 
                                    if p == objetct.position: 
                                        o = objetct.name #cambia el nombre del objeto
                    elif option == 'D': # verifica la entrada
                        p = 'right' 
                        for room in rooms: #busca el cuarto
                            if r == room.name: #busca el objeto dentro del cuarto
                                objects = room.objetos
                                for objetct in objects:
                                    if p == objetct.position: #cambia la posicion dentro del cuarto
                                        o = objetct.name
                    elif option == "G": #verifica la entrada
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        g = objetct.game #juego del objeto
                                        if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                            if g.requerimiento in inventory: 
                                                g.play(player, vidas, inventory, pistas)#inicia el metodo play dentro de la clase
                                            else:
                                                print(f'\n{g.mensaje}')
                                        else:
                                            g.play(player, vidas, inventory, pistas)
                    else:
                        print('\n Escoja una opcion valida\n')  
                elif p == 'right':
                    option = input('Para ir al centro "C".\nPara ir a la Izquierda "I".\nPara inetractuar con el objeto "G".\n>>> ').upper()
                    if option == 'I': #verifica la entrada
                        p = 'left'#cambia la posicion dentro del cuarto
                        for room in rooms: #busca el cuarto
                            if r == room.name: 
                                objects = room.objetos #busca el objeto dentro del cuarto
                                for objetct in objects: 
                                    if p == objetct.position: 
                                        o = objetct.name #cambia el nombre del objeto
                    elif option == 'C': # verifica la entrada
                        p = 'center' 
                        for room in rooms: #busca el cuarto
                            if r == room.name: #busca el objeto dentro del cuarto
                                objects = room.objetos
                                for objetct in objects:
                                    if p == objetct.position: #cambia la posicion dentro del cuarto
                                        o = objetct.name
                    elif option == "G": #verifica la entrada
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        g = objetct.game #juego del objeto
                                        if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                            if 'contraseña' in inventory: 
                                                g.play(player, vidas, inventory, pistas)#inicia el metodo play dentro de la clase
                                            else:
                                                print(f'\n{g.mensaje}')
                                        else:
                                            g.play(player, vidas, inventory, pistas)
                    else:
                        print('\nEscoja una opcion valida\n') 
            elif r == "Cuarto de Servidores ":
                if p == 'center':
                    option = input('Para ir a la izquierda "I".\nPara ir a la derecha "D".\nPara ir a los laboratorios "L".\nPara inetractuar con el objeto "G".\n>>> ').upper()
                    if option == 'I': #verifica la entrada
                        p = 'left'#cambia la posicion dentro del cuarto
                        for room in rooms: #busca el cuarto
                            if r == room.name: 
                                objects = room.objetos #busca el objeto dentro del cuarto
                                for objetct in objects: 
                                    if p == objetct.position: 
                                        o = objetct.name #cambia el nombre del objeto
                    elif option == 'D': # verifica la entrada
                        p = 'right' 
                        for room in rooms: #busca el cuarto
                            if r == room.name: #busca el objeto dentro del cuarto
                                objects = room.objetos
                                for objetct in objects:
                                    if p == objetct.position: #cambia la posicion dentro del cuarto
                                        o = objetct.name
                    elif option == "G": #verifica la entrada
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        if objetct.name == 'Puerta Servidores':
                                            g = objetct.game #juego del objeto

                                            if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                                if 'carnet' in inventory: 
                                                    if 'Disco Duro' in inventory: 
                                                        g.play(player, vidas, inventory, pistas)#inicia el metodo play dentro de la clase
                                                    else:
                                                        print(f'\n{g.mensaje}')
                                                else:
                                                    print(f'\n{g.mensaje}')
                                            else:
                                                g.play(player, vidas, inventory, pistas)
                    elif option == 'L':
                        p = 'center' #cambia la posicion dentro del cuarto
                        r = 'Laboratorio SL001' #cambia la variable de cuarto
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects: #busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        o = objetct.name
                    else:
                        print('\n Escoja una opcion valida\n')
                elif p == 'left':
                    option = input('Para ir al centro "C".\nPara ir a la derecha "D".\nPara inetractuar con el objeto "G".\n>>> ').upper()
                    if option == 'C': #verifica la entrada
                        p = 'center'#cambia la posicion dentro del cuarto
                        for room in rooms: #busca el cuarto
                            if r == room.name: 
                                objects = room.objetos #busca el objeto dentro del cuarto
                                for objetct in objects: 
                                    if p == objetct.position: 
                                        o = objetct.name #cambia el nombre del objeto
                    elif option == 'D': # verifica la entrada
                        p = 'right' 
                        for room in rooms: #busca el cuarto
                            if r == room.name: #busca el objeto dentro del cuarto
                                objects = room.objetos
                                for objetct in objects:
                                    if p == objetct.position: #cambia la posicion dentro del cuarto
                                        o = objetct.name
                    elif option == "G": #verifica la entrada
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        g = objetct.game #juego del objeto
                                        if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                            if g.requerimiento in inventory: 
                                                g.play(player, vidas, inventory, pistas)#inicia el metodo play dentro de la clase
                                            else:
                                                print(f'\n{g.mensaje}')
                                        else:
                                            g.play(player, vidas, inventory, pistas)
                    else:
                        print('\n Escoja una opcion valida\n')             
                elif p == 'right':
                    option = input('Para ir al centro "C".\nPara ir a la Izquierda "I".\nPara inetractuar con el objeto "G".\n>>> ').upper()
                    if option == 'I': #verifica la entrada
                        p = 'left'#cambia la posicion dentro del cuarto
                        for room in rooms: #busca el cuarto
                            if r == room.name: 
                                objects = room.objetos #busca el objeto dentro del cuarto
                                for objetct in objects: 
                                    if p == objetct.position: 
                                        o = objetct.name #cambia el nombre del objeto
                    elif option == 'C': # verifica la entrada
                        p = 'center' 
                        for room in rooms: #busca el cuarto
                            if r == room.name: #busca el objeto dentro del cuarto
                                objects = room.objetos
                                for objetct in objects:
                                    if p == objetct.position: #cambia la posicion dentro del cuarto
                                        o = objetct.name
                    elif option == "G": #verifica la entrada
                        for room in rooms: # verifica que e cuarto este guardado en la lista cuartos
                            if r == room.name:
                                objects = room.objetos
                                for objetct in objects:#busca el objeto dentro del cuarto
                                    if p == objetct.position:
                                        g = objetct.game #juego del objeto
                                        if g.requerimiento: #verifica si el juego tiene algun requerimiento
                                            if g.requerimiento in inventory: 
                                                g.play(player, vidas, inventory, pistas)#inicia el metodo play dentro de la clase
                                            else:
                                                print(f'\n{g.mensaje}')
                                        else:
                                            g.play(player, vidas, inventory, pistas)
                    else:
                        print('\nEscoja una opcion valida\n')
