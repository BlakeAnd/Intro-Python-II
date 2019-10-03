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
name = "larry"
new_player = Player(name, room["outside"])
# print(new_player.room)

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
import textwrap
print(f"welcome! {new_player.name}")
go = ""
while go != "q":
  current_room = new_player.room
  directions = current_room.directions()
  print("press i for instructions")
  print(f"you are at: {new_player.room}")
  print(f"possible travel directions: {directions} ")
  print(textwrap.fill(current_room.description, width=40))
  go = input("what will you do?  ")
  if(go == "n"):
    if current_room.n_to:
      new_player.room = current_room.n_to
      print("")
    else:
      print("\n can't go that direction")
  elif(go == "s"):
    if current_room.s_to:
      new_player.room = current_room.s_to
      print("")
    else:
      print("\n can't go that direction")
  elif(go == "e"):
    if current_room.e_to:
      new_player.room = current_room.e_to
      print("")
    else:
      print("\n can't go that direction")
  elif(go == "w"):
    if current_room.w_to:
      new_player.room = current_room.w_to
      print("")
    else:
      print("\n can't go that direction!")
  elif(go =="q"):
    print("Goodbye!")
  elif(go == "i"):
    print("\n instructions: press... \n n to go north \n s to go south \n e to go east \n w to go west \n q to quite the game")
  else:
    print("\n invalid input try again")


  