from warrior import Warrior

class Player:
    def __init__(self, name, w_type):
        self.name = name
        self.warrior = Warrior(w_type)
    def greet(self, message, other_player):
        print(f"{self.name} says {message} to {other_player.name}")
        return self
    def edit_name(self, new_name):
        self.name = new_name
        return self