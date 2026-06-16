class Character:
    def __init__(self, health, name, attack):
        self.max_health = health
        self.health = health
        self.name = name
        self.attack = attack
    
    def show_status(self):
        print(f"{self.name} has {self.health} HP and {self.attack} ATK.\n")

    def health_check(self):
        if (self.health <= 0):
            print(f"{self.name} has been defeated.\n")
            return False
        else: 
            return True

    def take_damage(self, attacker):
        self.health = max(0, self.health - attacker.attack)
        print(f"{self.name} took {attacker.attack} damage from {attacker.name}.\n")
        self.health_check()
        self.show_status()

    def attack_sequence(self, target):
        print(f"{self.name} attacks {target.name}.\n")
        target.take_damage(self)

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
    
    def heal_full(self):
        self.heal(self.max_health)

    def to_dict(self):
        return {
            "max_health": self.max_health,
            "health": self.health,
            "attack": self.attack,
            "name": self.name
        }
    