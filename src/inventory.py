from item import Item

class Inventory:
    def __init__(self):
        self.items = []

    def open_inventory(self):
        if not self.items:
            print("Your Everlast socks are empty.")
            return
        
        print("Current items in Everlast socks: \n")
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
            print(f"{item.name} has been successfully added to the Everlast socks.\n")
            return True
        else:
            print("Your Everlast socks are full.")
            return False

    def remove_inventory_item(self, item):
            if isinstance(item, int):
                if not (1 <= item <= len(self.items)):
                    print("There's no item with such ID.")
                    return False
                
                removableItem = self.items[item - 1]
                print(f"{removableItem.name} has been removed from the Everlast socks.\n")
                self.items.pop(item - 1)
                return True
            elif not isinstance(item, Item):
                print("Item you're trying to remove is not valid.")
                return False
            for existingItem in self.items:
                if existingItem.name.lower() == item.name.lower():
                    self.items.remove(existingItem)
                    print(f"{item.name} has been removed from the Everlast socks.\n")
                    return True
            else:
                print("This item is not in your Everlast socks.")
                return False

    def use_inventory_item(self, item, character):
        if isinstance(item, int):
            if not (1 <= item <= len(self.items)):
                print("There's no item with such ID.")
                return False
            
            usedItem = self.items[item - 1]
            usedItem.use_item(character) 
            return True
        elif not isinstance(item, Item):
                print("Item you're trying to use is not valid.")
                return False
        for existingItem in self.items:
            if existingItem.name.lower() == item.name.lower():
                    existingItem.use_item(character)
                    return True

        else:
            print(f"{item.name} is not in your Everlast socks.")
            return False