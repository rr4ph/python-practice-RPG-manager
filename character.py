import json

class Character:
    def __init__(self, max_health, health, name, attack):
        self.max_health = max_health
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
    
    def save_data(self):
        with open("character.json", "w") as file:
            json.dump(self.to_dict(), file, indent=4)

def load_data():
    with open("character.json", "w") as file:
        char_data = json.load(file)
        return Character(char_data["max_health"], char_data["health"], char_data["name"], char_data["attack"])
    