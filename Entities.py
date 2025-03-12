#POTENTIAL MODIFY:
#Creature __str__


'''
The entities file contains all entity related objects for the game.
'''

from abc import abstractmethod, ABC

#Entity Class. The parent class for all the entity related objects
class Entities(ABC):

    #Abstract constructor for entities
    @abstractmethod
    def __init__(self, name:str, desc:str) -> None:
        self._name = name
        self._desc = desc

    '''Getters and setters'''
    
    #Get name
    def get_name(self) ->str:
        return self._name
    
    #Set name
    def set_name(self, name) ->None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name

    #Get description
    def get_description(self) ->str:
        return self._desc
    
    #Set description
    def set_description(self, desc) ->None:
        if not isinstance(desc, str):
            raise TypeError("Description must be a string")
        self._desc = desc

    #String method
    def __str__(self) ->str:
        return (f"{self._name}\n {self._desc}")
    

'''Item class. Defines methods for gameplay-related items'''
class Items(Entities):
    
    #Constructor
    def __init__(self, name:str, desc:str, remove_on_use:bool = False, pickup:bool = False) -> None:
        super().__init__(name, desc)
        self._remove_on_use = remove_on_use
        self._pickup = pickup #If Item can be picked up

    '''Setters/Getters'''
    #Set pickup value
    def set_pickup(self, value):
        if not isinstance(value, bool):
            raise TypeError("Pickup value must be a boolean")
        self._pickup = value
        
    #Get pickup value
    def get_pickup(self):
        return self._pickup

    #Get remove_on_use
    def get_item_removal(self) ->bool:
        return self._remove_on_use
    
    #Set removal
    def set_item_removal(self, value) ->None:
        if not isinstance(value, bool):
            raise TypeError("Item removal on use should be a boolean")
        self._remove_on_use = value

    #String method to return characteristics of the item
    def __str__(self):
        #return super().__str__ + f"\nRemoval on use? {self._remove_on_use}"
        return super().__str__()
    

'''Player class. Defines player related methods'''
class Player(Entities):
    #Constructor
    def __init__(self, name, desc):
        super().__init__(name, desc)
        self._items = [] #List of items in inventory

    #Get inventory
    def get_items(self) ->list[Items]:
        return self._items
    
    #Add an item to inventory
    def add_item(self, item):
        if not isinstance(item, Items):
            raise TypeError("Item added to inventory must be an Item Object")
        self._items.append(item)
    
    #Remove an item from inventory
    def remove_item(self, item):
        if item not in self._items:
            raise ValueError("Item is not in inventory")
        self._items.remove(item)

    def __str__(self):
        return super().__str__()


'''Creature class. Defines all NPC related methods'''
class Creature(Entities):

    #Constructor
    def __init__(self, name:str, desc:str, item:Items = None, defeated_by:Items=None, defeated_text:str=None, change_on_wait:bool = False) -> None:
        super().__init__(name, desc)
        self._item = item #The item dropped by the creature
        self._defeated_by = defeated_by #What items are required to defeat the creature
        self._defeated_text = defeated_text #Text displayed after defeating a creature
        self._change_on_wait = change_on_wait #Boolean to decide if an event happens if the player waits

    '''Setters/Getters'''
    #Get wait
    def get_change_on_wait(self) -> bool:
        return self._change_on_wait
    
    #Set wait
    def set_change_on_wait(self, value):
        if not isinstance(value, bool):
            raise TypeError("Change on wait must be a bool")
        self._change_on_wait = value

    #Get item dropped
    def get_item_dropped(self) ->Items:
        return self._item
    
    #Set item dropped by creature
    def set_item_dropped(self, item) ->None:
        if not isinstance(item, Items):
            raise TypeError("Item dropped must be of type Items")
        
    #Get defeated_by (Item)
    def get_defeated_by(self) ->Items:
        return self._defeated_by
    
    #Set defeated_by (Item)
    def set_defeated_by(self, item) ->None:
        if not isinstance(item, Items):
            raise ValueError("Item to defeat the creature must be of type Items")
        self._defeated_by = item

    #Get text of defeated_text
    def get_defeated_text(self) ->str:
        return self._defeated_text
    
    #Set text of defeated_text
    def set_defeated_text(self, text) ->None:
        if not isinstance(text, str):
            raise TypeError("Text shown after creature's defeat must be a string")
        self._defeated_text = text


    '''Room Class. Defines all room related methods'''
class Room(Entities):

    #Constructor
    def __init__(self, name:str, desc:str, exits:list, items:list[Items] = [], creatures:list[Creature]=[]):
        super().__init__(name, desc)
        self._exits = exits                                 #List of exits
        self._items = items                                 #List of items in the room
        self._creatures = creatures                         #List of creatures in the room
        
    #Get exits
    def get_exits(self):
        return self._exits

    #Add an exit to the list of exits
    def add_exit(self, exit):
        if not isinstance(exit, Exit):
            raise TypeError("Exit must be of type Exit")
        self._exits.append(exit)

    #Remove an exit from the list of exits
    def remove_exit(self, exit):
        if not isinstance(exit, Exit):
            raise TypeError("Exit must be of type Exit")
        if exit in self._exits:
            self._exits.remove(exit)

    #Add an item to the items list
    def get_items(self):
        return self._items

    #Add an item to the list of items
    def add_item(self, item):
        if not isinstance(item, Items):
            raise TypeError("Item must be of type Items")
        self._items.append(item)

    #Remove an exit from the list of exits
    def remove_item(self, item):
        if not isinstance(item, Items):
            raise TypeError("Item must be of type Items")
        if item in self._items:
            self._items.remove(item)

    #Get all creature
    def get_creature(self):
        return self._creatures

    #Add creature to creature list
    def add_creature(self, creature):
        if not isinstance(creature, Creature):
            raise TypeError("Creature must be of type Creature")
        self._creatures.append(creature)
    
    #Remove creature from creature list
    def remove_creature(self, creature):
        if not isinstance(creature, Creature):
            raise TypeError("Creature must be of type Creature")
        if creature in self._creatures:
            self._creatures.remove(creature)
    
    #String method
    def __str__(self):
        return super().__str__()


'''Exit Class. Defines all exit related methods'''
class Exit(Entities):

    #Constructor
    def __init__(self, name:str, desc:str, destination:Room, transition:str, hidden:bool, blocked_by:Creature=None, opened_with:Items=None, bad_exit:bool = False):
        super().__init__(name, desc)
        self._destination = destination #Room to transition forward
        self._transition = transition #Transition text
        self._hidden = hidden #Boolean representing if the exit is listed in a room's exit list
        self._blocked_by = blocked_by #A creature blocking the exit
        self._opened_with = opened_with #Item needed to go through the exit
        self._bad_exit = bad_exit       #If the exit should be removed after an event

    #Get bad_exit
    def get_bad_exit(self):
        return self._bad_exit
    
    #Set bad exit
    def set_bad_Exit(self, value):
        if not isinstance(value, bool):
            raise TypeError("Bad Exit value must be a bool")
        self._bad_exit = value

    #Get destination
    def get_destination(self):
        return self._destination
    
    #Set destination
    def set_destination(self, destination):
        if not isinstance(destination, Room):
            raise TypeError("Destination must be of type Room")
        self._destination = destination

    #Get transition
    def get_transition(self):
        return self._transition
    
    #Set transition
    def set_transition(self, transition):
        if not isinstance(transition, str):
            raise TypeError("Transition text must be of type string")
        self._transition = transition

    #Get hidden
    def get_hidden(self):
        return self._hidden

    #Set hidden
    def set_hidden(self, hidden):
        if not isinstance(hidden, bool):
            raise TypeError("Hidden value is a bool")
        self._hidden = hidden

    #Get blocked_by
    def get_blocked_by(self):
        return self._blocked_by

    #Set blocked by
    def set_blocked_by(self, value):
        if not isinstance(value, Creature):
            if value is not None:
                raise TypeError("Blocked by must be of type Creature")
        self._blocked_by = value
    
    #Get opened_with
    def get_opened_with(self):
        return self._opened_with

    #Set opened with
    def set_opened_with(self, value):
        if not isinstance(value, Items):
            raise TypeError("Opened with must be of type Items")
        self._opened_with = value