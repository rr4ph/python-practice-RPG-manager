class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use_item(self, character):
        print(f"{character.name} used {self.name}.")


class Potion(Item):
    def __init__(self):
        super().__init__(
            "Potion",
            "Restores 50 HP."
        )
    
    def use_item(self, character):
        super().use_item(character)
        character.heal(50)
        print("Recovered 50 HP.")
        return True

class Sword(Item):
    def __init__(self):
        super().__init__(
            "Sword",
            "Default iron sword, 5 ATK."
        )
        self.damage = 5
    
    def use_item(self, character):
        if character.has_weapon():
            print(f"{character.name} already has {character.equipped_weapon.name} equipped.")
            print(f"Would you like to switch {character.equipped_weapon.name} to {self.name}?")
            choice = input("Y/N: ").lower().strip()
            if choice in ["y", "yes"]:
                character.inventory.add_inventory_item(character.equipped_weapon)
                character.attack -= character.equipped_weapon.damage
                character.equipped_weapon = None
            elif choice in ["n", "no"]:
                print("Operation has been halted.")
                return False
        super().use_item(character)
        character.equipped_weapon = self
        character.attack += self.damage
        print(f"Equipped {self.name}, +{self.damage} ATK.")
        return True

ITEM_DATABASE = {
    "potion": Potion,
    "sword": Sword,
}