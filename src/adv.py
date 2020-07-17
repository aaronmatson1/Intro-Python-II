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
is_playing = True
player = Player(room['outside'])

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while is_playing:
    print(f'\n Current location: {player.room.name}')
    print(player.room.description, "\n")
    direction = input('Which way would you like to go? \n`n` for North, `s` for South, `e` for East, and `w` for West. or `q` to quit \n Enter Selection here: ')

    try:
        if direction == 'n':
            player.room = player.room.n_to
        except:
            print(wrongWay)

    try:
        if direction == 'e':
            player.room = player.room.e_to
    except:
        print("Can't go that way!")

    try:
        if direction == 's':
            player.room = player.room.s_to
    except:
        print("Can't go that way!")

    try:
        if direction == 'w':
            player.room = player.room.w_to
    except:
        print("Can't go that way!")

    if direction == 'q':
        print("\n\Game Over!")
        is_playing = False