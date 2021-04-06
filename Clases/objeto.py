class Objeto:
    def __init__(self, name, position, game):
        self.name = name
        self.position = position
        self.game = game
    def show(self):
        print(f'\nnombre: {self.name}\nposicion: {self.position}\njuego:{self.game}')