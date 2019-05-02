# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return str(f"{self.name}, {self.description}")

    def lost_item(self, item):
        self.items.remove(item)
        print(f'{item.name} was removed')

    def list_items(self, item):
        if len(self.items) > 0:
            print("items in room")
            for i in self.items:
                print(i.name)