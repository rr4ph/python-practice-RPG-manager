class Character:
    def __init__(self, health, name, attack):
        self.health = health
        self.name = name
        self.attack = attack
    
    def show_status(self):
        print(f"{self.name} has {self.health} HP and {self.attack} ATK.\n")

    def health_check(self):
        self.show_status()
        if (self.health <= 0):
            print(f"{self.name} has been defeated.\n")
            quit()

    def take_damage(self, attacker):
        self.health = self.health - attacker.attack
        print(f"{self.name} took {attacker.attack} damage from {attacker.name}.\n")
        self.health_check()

    def attack_sequence(self, target):
        print(f"{self.name} attacks {target.name}.\n")
        target.take_damage(self)
