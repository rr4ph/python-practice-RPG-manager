import json
from inventory import Inventory
from item import ITEM_DATABASE

class Character:
    def __init__(self, max_health, health, name, attack, inventory=None, equipped_weapon=None):
        self.max_health = max_health
        self.health = health
        self.name = name
        self.attack = attack
        self.inventory = inventory or Inventory()
        self.equipped_weapon = equipped_weapon
    
    def show_character_info(self):
        print(f"""
-- CHARACTER INFO --
Name: {self.name}
Health: {self.health}/{self.max_health} HP
Attack: {self.attack} ATK""")
        if not self.equipped_weapon:
            print("Weapon: No weapon equipped.")
        else:
            print(f"Weapon: {self.equipped_weapon.name}")

    def show_HP(self):
        print(f"{self.name}: {self.health}/{self.max_health} HP.\n")

    def health_check(self):
        if (self.health <= 0):
            print(f"{self.name} has been defeated.\n")
            return False
        else: 
            return True

    def take_damage(self, attacker):
        self.health = max(0, self.health - attacker.attack)
        print(f"{self.name} took {attacker.attack} damage from {attacker.name}.\n")
        self.show_HP()

    def attack_sequence(self, target):
        print(f"{self.name} attacks {target.name}.\n")
        target.take_damage(self)

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
    
    def heal_full(self):
        self.heal(self.max_health)

    def has_weapon(self):
        return self.equipped_weapon is not None

    def to_dict(self):
        inventory_list = []
        for item in self.inventory.items:
            inventory_list.append(item.name.lower())

        return {
            "max_health": self.max_health,
            "health": self.health,
            "name": self.name,
            "attack": self.attack,
            "equipped_weapon":  (self.equipped_weapon.name.lower() if self.equipped_weapon
                                else None),
            "inventory": inventory_list
        }
    
    def save_data(self):
        with open("data/saves/character.json", "w") as file:
            json.dump(self.to_dict(), file, indent=4)

def load_data():
    with open("data/saves/character.json") as file:
        char_data = json.load(file)

        weapon_data = char_data["equipped_weapon"]
        if weapon_data:
            equipped_weapon = ITEM_DATABASE[weapon_data]()
        else:
            equipped_weapon = None

        char_items = Inventory()
        for item in char_data["inventory"]:
            char_items.items.append(ITEM_DATABASE[item]())

            
        return Character(char_data["max_health"], 
                         char_data["health"], 
                         char_data["name"], 
                         char_data["attack"], 
                         char_items, 
                         equipped_weapon
                        )