class Warrior:
    def __init__(self, w_type):
        self.health = 500
        self.type = w_type
    # an attack method
    def attack(self, target):
        # when target is hit, health points will drop
        if self.type == "ninja":
            target.warrior.health -= 50
            print(f"{self.type} threw a throwing star at {target.name}, it did 50 damage. Targets health: {target.warrior.health}")
        elif self.type == "wizard":
            target.warrior.health -= 75
            print(f"{self.type} shot a fireball at {target.name}, current target health: {target.warrior.health}")
        else:
            target.warrior.health -= 100
            print(f"{self.type} sliced {target.name} in half! Target health: {target.warrior.health}")
        return self