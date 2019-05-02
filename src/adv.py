from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item('sword', 'pointy')),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item('pokéflute', 'why not')),
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
newPlayer = Player('Lols', room['outside'])


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
    newPlayer.current_room = newRoom
    # print(newPlayer.current_room)
    return newPlayer

def start_game():
    in_treasure_room = False
    while in_treasure_room is False:
        try:
            starting_room = room_setup()
            new_move = input('Enter direction to go, [n] [s] [e] or [w] or [q] to quit the game')
            if new_move == "q":
                break
            moved_player = move_me(starting_room, new_move)
            if moved_player.current_room == 'Treasure Chamber':
                in_treasure_room = True
        except AttributeError:
            print('This is not a valid entry, please try again')

def get_items(p):
    print()
    print(p.items.name)
    print()
    take_item = input("Do you want to pick up the item? [c] to confirm or [d] to deny")
    if take_item == 'c':
        p.lost_item(p.items)
        print('Please continue going')
    else:
        print('Please continue in the direction you wish')
        
        

print()
print(newPlayer.current_room)    
print("Enter a key to continue... \n [n]orth\n [s]outh\n [e]ast\n [w]est or \n [q]uit")
while True:
    print()
    print()
    cmd = input(' -> ')
    if cmd == 'q':
        break
    elif cmd == 'n' or cmd == 's' or cmd == 'e' or cmd == 'w':
        try:
            updatedPlayer = move_me(newPlayer.current_room, cmd)
            if updatedPlayer is not None:
                print(f"{updatedPlayer.name} is in the {updatedPlayer.current_room.name}")
                print(newPlayer.current_room.description)
                print()
                print(newPlayer.current_room.items)
                if newPlayer.current_room.items is not None:
                    get_items(newPlayer.current_room)
        except AttributeError:
            print('You broke the rules of the game, you are now dead')
            break
    else:
        print('invalid entry')
    # print(newPlayer.current_room.description)

    
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.