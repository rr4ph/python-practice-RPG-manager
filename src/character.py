import json
from item import Item

class Character:
    def __init__(self, max_health, health, name, attack):
        self.max_health = max_health
        self.health = health
        self.name = name
        self.attack = attack
        self.inventory = []
    
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
        with open("data/saves/character.json", "w") as file:
            json.dump(self.to_dict(), file, indent=4)

    def open_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
            return
        
        print("Current items in backpack: \n")
        for index, item in enumerate(self.inventory, start=1):
            print(f"{index}: {item.name}")
        print()

    def add_inventory_item(self, item):
        if not isinstance(item, Item):
            print("Item you're trying to add is not valid.")
            return
        elif len(self.inventory) < 10:
            self.inventory.append(item)
            print(f"{item.name} has been successfully added to the inventory.\n")
        else:
            print("Your inventory is full.")

    def remove_inventory_item(self, item):
            if not isinstance(item, Item):
                print("Item you're trying to remove is not valid.")
                return
            for existingItem in self.inventory:
                if existingItem.name.lower() == item.name.lower():
                    self.inventory.remove(existingItem)
                    print(f"{item.name} has been removed from the inventory.\n")
                    break
            else:
                print("This item is not in your inventory.")

def load_data():
    with open("data/saves/character.json") as file:
        char_data = json.load(file)
        return Character(char_data["max_health"], char_data["health"], char_data["name"], char_data["attack"])