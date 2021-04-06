class Player:
    def __init__(self, username, password, age, avatar, matches):
        self.username = username
        self.password = password
        self.age = age
        self.avatar = avatar
        self.matches = matches
    def show(self):
        print(f'\nusername: {self.username}\nEdad: {self.age}\nAvatar: {self.avatar}')