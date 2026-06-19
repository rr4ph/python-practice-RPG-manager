from item import Item

class Inventory:
    def __init__(self):
        self.items = []

    def open_inventory(self):
        if not self.items:
            print("Your inventory is empty.")
            return
        
        print("Current items in backpack: \n")
        current_items = {}
        for index, item in enumerate(self.items, start=1):
            current_items[index] = item.name.lower()
            print(f"{index}: {item.name}")
        print()
        return current_items

    def add_inventory_item(self, item):
        if not isinstance(item, Item):
            print("Item you're trying to add is not valid.")
            return False
        elif len(self.items) < 10:
            self.items.append(item)
            print(f"{item.name} has been successfully added to the inventory.\n")
            return True
        else:
            print("Your inventory is full.")
            return False

    def remove_inventory_item(self, item):
            if isinstance(item, int):
                print(item)
                removableItem = self.items[item - 1]
                print(f"{removableItem.name} has been removed from the inventory.\n")
                self.items.pop(item - 1)
                return
            elif not isinstance(item, Item):
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
        if isinstance(item, int):
            usedItem = self.items[item - 1]
            if usedItem.use_item(character):  
                self.remove_inventory_item(item)
            return
        elif not isinstance(item, Item):
                print("Item you're trying to use is not valid.")
                return
        for existingItem in self.items:
            if existingItem.name.lower() == item.name.lower():
                    if item.use_item(character):  
                        self.remove_inventory_item(existingItem)
                    break
        else:
            print(f"{item.name} is not in your inventory.")