from item import Item

class Inventory:
    def __init__(self):
        self.items = []

    def open_inventory(self):
        if not self.items:
            print("Your inventory is empty.")
            return
        
        print("Current items in backpack: \n")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}: {item.name}")
        print()

    def add_inventory_item(self, item):
        if not isinstance(item, Item):
            print("Item you're trying to add is not valid.")
            return
        elif len(self.items) < 10:
            self.items.append(item)
            print(f"{item.name} has been successfully added to the inventory.\n")
        else:
            print("Your inventory is full.")

    def remove_inventory_item(self, item):
            if not isinstance(item, Item):
                print("Item you're trying to remove is not valid.")
                return
            for existingItem in self.items:
                if existingItem.name.lower() == item.name.lower():
                    self.items.remove(existingItem)
                    print(f"{item.name} has been removed from the inventory.\n")
                    break
            else:
                print("This item is not in your inventory.")

    def use_inventory_item(self, item, character):
        if not isinstance(item, Item):
                print("Item you're trying to use is not valid.")
                return
        for existingItem in self.items:
            if existingItem.name.lower() == item.name.lower():
                    item.use_item(character)
                    self.remove_inventory_item(existingItem)
                    break
        else:
            print(f"{item.name} is not in your inventory.")