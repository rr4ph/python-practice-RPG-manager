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

class Sword(Item):
    def __init__(self):
        super().__init__(
            "Sword",
            "Default iron sword, 5 ATK."
        )
    
    def use_item(self, character):
        super().use_item(character)
        character.attack += 5
        print(f"Equipped {self.name}, +5 ATK.")

ITEM_DATABASE = {
    "potion": Potion,
    "1": Potion,
    "sword": Sword,
    "2": Sword
}