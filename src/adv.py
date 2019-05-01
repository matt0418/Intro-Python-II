from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player('Lols', room['outside'].name)


# Write a loop that:


# user = input("[North] North [East] East [South] South [West] West [Q] Press q to quit\n")

def room_setup():
    for i in room:
        if newPlayer.current_room == room[i].name:
            print()
            print(f"{newPlayer.name} is in the")
            print(room[i].name)
            print()
            print(room[i].description)
            print()
            print("What direction would you like to go?")
            for d in ['n_to', 's_to', 'e_to', 'w_to']:
                r = getattr(room[i], d, False)
                if r is not False:
                    print(f'To move to {r.name}, enter {d} ')
            return room[i]


def move_me(currentRoom, move):
    moving = move + '_to'
    newRoom = getattr(currentRoom, moving, False)
    newPlayer.current_room = newRoom.name
    print(newPlayer.current_room)
    return newPlayer

def start_game():
    in_treasure_room = False
    while in_treasure_room is False:
        starting_room = room_setup()
        new_move = input('Enter direction to go, [n] [s] [e] or [w] or [q] to quit the game')
        if new_move == "q":
            break
        moved_player = move_me(starting_room, new_move)
        if moved_player.current_room == 'Treasure Chamber':
            in_treasure_room = True

start_game()
print('You won the game')
    
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.