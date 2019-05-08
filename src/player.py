# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, storage=[]):
        self.name = name
        self.current_room = current_room
        self.storage = storage

    def __str__(self):
        return str(f'{self.name}, {self.current_room}')

    