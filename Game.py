'''This file contains all logic for playing the game/game mechanics'''

from Entities import *
import time
class Game:

    #Constructor
    def __init__(self, player:Player, starting_room:Room, ending_room:Room, starting_text:str, ending_text:str) -> None:
        self._player = player                   #Player Object
        self._starting_room = starting_room     #Starting Room
        self._ending_room = ending_room         #Ending Room
        self._starting_text = starting_text     #Text to display at beginning of the game
        self._ending_text = ending_text         #Text to display at the end of the game
        self._current_room = starting_room      #Current room object for reference -> Starts as starting room

    #Display status of room (Description and contents)
    def display_status(self) -> None:
        Game.slow_print(f"{self._current_room.get_name()}\n" +  
              f"{self._current_room.get_description()}\n")
        Game.slow_print("Items:\n")
        if self._current_room.get_items() is not None:
            for item in self._current_room.get_items():
                Game.slow_print(f"* {item.get_name()}\n")
        Game.slow_print("Exits:\n")
        for exit in self._current_room.get_exits():
            if exit.get_hidden() == False:
                Game.slow_print(f"* {exit.get_name()}\n")
        Game.slow_print("NPCs in Room:\n")
        if self._current_room.get_creature() is not None:
            for npc in self._current_room.get_creature():
                Game.slow_print(f"* {npc.get_name()}\n")
        
    #Display valid commands that the player can call -> helpful guide on how to play
    def display_help(self) -> None:
        Game.slow_print(f"List of possible commands:\n" +
              f"1. Go (destination) -> Command to move around. Specify the exit you'd like to take Example: Go door\n" +
              f"2. Look (entity) -> Command to look at an entity in the room. Example: 'Look door'\n" +
              f"3. Get (item) -> Command to pick up an item within the room if it's possible. Example: 'Get key'\n" +
              f"4. Use (item, entity) -> Command to use an item on an entity. Example: 'use key on door'\n" +
              f"5. Wait -> The player waits around and let's a litle time pass. Example: 'Wait'\n" +
              f"6. Help -> Displays this helpful command guide. Example: 'Help'\n")

    #Display the player's inventory
    def display_inventory(self) -> None:
        if self._player.get_items() is None:
            Game.slow_print("Your inventory is empty")
        for item in self._player.get_items():
            Game.slow_print(f"* {item}")

  #Process user's input to decide which course of action to take
    def process_input(self):
        while (True):
            command = input("What do you do?")
            if command != "":
                break
        command = command.split()
        command = [word.lower() for word in command]
        if command[0] == 'go':
            if len(command) < 2:
                self.process_go(input(Game.slow_print("Where would you like to go?")))
            else:
                self.process_go(command[1])
        elif command[0] == 'get':
            if len(command) < 2:
                self.process_get(input(Game.slow_print("What would you like to pick up?")))
            else: 
                self.process_get(command[1])
        elif command[0] == 'look':
            if len(command) < 2:
                self.process_look(input(Game.slow_print("What would you like to look at?")))
            else:
                self.process_look(command[1])
        elif command[0] == 'use':
            if len(command) < 2:
                self.process_use(input(Game.slow_print("What item would you like to use?")), input(Game.slow_print("What creature would you like to use the item on?")))
            elif len(command) < 4:
                self.process_use(command[1], input(Game.slow_print("What creature would you like to use the item on?")))
            else:
                self.process_use(command[1], command[3])
    
        elif command[0] == 'inventory':
            self.display_inventory()
        elif command[0] == 'help':
            self.display_help()
        elif command[0] == 'wait':
            self.process_wait()
        else:
            Game.slow_print("Command not found. Type 'help' for helpful commands")

    #Process a transition to a different room
    def process_go(self, destination):

            #Loop through to get to the exit matching the exit's name
            for value in self._current_room.get_exits():
                if destination == value.get_name():
                    destination = value

            #If destination is not an exit object
            if not isinstance(destination, Exit):
                Game.slow_print("Destination not found")
                return
                    #Determine if player is able to go through that exit by checking for creature blocking path, ensuring it's not a friendly
            if destination.get_blocked_by() is not None:
                    if destination.get_blocked_by().get_name() != "hunter":
                        Game.slow_print(f"A creature stands before you, blocking the exit")
                        return
                    
                #Determine if the player has an item that is needed
            if destination.get_opened_with() is not None:
                if destination.get_opened_with() not in self._player.get_items():
                    Game.slow_print("Missing item required")
                    return

            #Print exit transition text
            Game.slow_print(destination.get_transition())
                    
            #switch current room to the room instance
            self._current_room = destination.get_destination()

    #Process an item pick-up from the room
    def process_get(self, item):
    
            #Loop through items in room
        for value in self._current_room._items:

            #If value = 'item in room's name'
            if item == value.get_name():
                    
                    #If able to pickup
                    if value.get_pickup() == True:
                        self._player.add_item(value)
                        Game.slow_print(f"Item {item} has been added to your inventory")
                        self._current_room.remove_item(value)
                        return
                    else:
                        Game.slow_print(f"{value.get_name()} is not able to picked up")
                        return
        #No item found to match name
        Game.slow_print(f"Item not found")
       
    #Process a 'look at' function to investigate an exit, item, or creature
    def process_look(self, command:str):
        #Loop to check all creatures
        if self._current_room.get_creature() is not None:
            for creature in self._current_room.get_creature():
                        #If user input matches creature's name
                    if command == creature.get_name():
                        Game.slow_print(f"{creature}")
                        return

                #Loop through to find the item
        if self._current_room.get_items() is not None:
            for item in self._current_room.get_items():
                        #If user input matches item's name
                if command == item.get_name():
                    Game.slow_print(f"{item}")
                    return

                #Loop to get to that exit
        if self._current_room.get_exits() is not None:
            for exit in self._current_room.get_exits():
                if command == exit.get_name():
                    Game.slow_print(f"{exit}")
                    return
            #If not a creature, item, or exit
        Game.slow_print("Unknown reference")
                


    #Process using an item on a creature
    def process_use(self, item, creature):

        #Check if item is in the inventory
        for value in self._player.get_items():
            if item == value.get_name():
                item = value
        if not isinstance(item, Items):
            Game.slow_print("Item not in inventory")
            return 

        #Loop through the room's creature to match the creature's name with user input
        for enemy in self._current_room.get_creature():
            if creature == enemy.get_name():
                creature = enemy

        if not isinstance(creature, Creature):
            Game.slow_print("Creature is not found in room")
            return
        
        #Check if the item matches the creature's item name that defeats it
        if item == enemy.get_defeated_by():

            #Remove item from inventory if needed
            if item.get_item_removal() == True:
                self._player.remove_item(item)

            #Print defeated text
            Game.slow_print(enemy.get_defeated_text())

            #Check if the enemy drops an item and add it to the room
            if enemy.get_item_dropped() is not None:
                self._current_room.add_item(enemy.get_item_dropped())

            #Remove creature from room
            self._current_room.remove_creature(enemy)
            
            for value in self._current_room.get_exits():
                value.set_blocked_by(None)
                return
        Game.slow_print("That item can not be used here")

    #Process a 'wait' command -> Detects and displays if a creature comes into the scene or leaves the scene based on waiting
    def process_wait(self):
        
        #Print flavor
        Game.slow_print("You wait around a little while, hoping for something to change")

        # If waiting finds hidden exit, forces player to take it
        for destination in self._current_room.get_exits():
            if destination.get_hidden() == True:

                #Print exit transition text
                Game.slow_print(destination.get_transition())
                    
                #switch current room to the room 
                self._current_room = destination.get_destination()
                return

        #Loop through all creatures
        if self._current_room.get_creature() is None:
            Game.slow_print("You waited, but nothing happened")
            return
        for enemy in self._current_room.get_creature():

            #If the enemy has a changing action, make them disappear from the room
            if enemy.get_change_on_wait() == True:
                for exit in self._current_room.get_exits():
                    if exit.get_bad_exit() == True:
                        self._current_room.remove_exit(exit)
                    exit.set_blocked_by(None) 
                    self._current_room.remove_creature(enemy)
                Game.slow_print("Waiting seemed to pay off.")
                return
        Game.slow_print("You waited, but nothing happened")
            
    #Slow down printing words to terminal -> Enhances story and makes it easier on eyes
    def slow_print(text):
        for char in text:
            print(char, end="", flush=True)
            time.sleep(0.008)

    #Starts and runs the game
    def start(game):
        #Print intro text
        Game.slow_print(game._starting_text + "\n")

        #Display helpful commands for the player to help them start the game
        game.display_help()
        print()

        #Loop to keep playing until the last room is reached
        while (game._current_room != game._ending_room):
            
            #Print game status (name, description, entities)
            game.display_status()
            print()

            #Expect user input
            game.process_input()
            print('\n') 

        #Display ending text
        Game.slow_print(game._ending_text)