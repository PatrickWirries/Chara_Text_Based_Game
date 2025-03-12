'''
This file controls the adventure. It creates the many object instances required for the adventure, and runs the program
By Patrick Wirries
'''

from Entities import *
from Game import *

#Player Instance
chara_player = Player("Chara", "A college student, abducted on her way home from class one day.")

#Item instances -> Name, Description, Remove on use, able_to_pickup 
rock_item = Items("rock", "A small, dusty, moldy, weathered rock", True, True)
key_item = Items("key", "An old and rusty key", True, True)
note_item = Items("note", "A small piece of paper with 3 numbers scratched into it. The numbers look faded, but you think you can make out the value. What could the numbers mean?", False, True)
radio_item = Items("radio", "A small black radio with a single button for speaking and a turn dial for a radio channel", True, True)
window_item = Items("window", "A small window partially covered in broken glass. The window's panes are too sharp to crawl through, even if the metal bars weren't blocking it")
bones_item = Items("bones", "A collection of animal bones, mostly old ones, strewn across the room, with a small pile along the wall.")
crate_item = Items("crate", "An old and slightly rusty lock. It requires a 3-digit combination to undo it")
bear_spray_item = Items("spray", "A can of bear spray. Useful and strong. Don't spray it at yourself.", True, True)

#Creature instances -> Name, Description, Item Drops, Item to defeat, text upon defeat, change on wait
kidnapper_creature = Creature("kidnapper", "The mean, old, kidnapping man wearing full black. Time has worn him down over the years" 
                     ,key_item, rock_item, "The man falls over, unconcious, dropping you the key for the door. You can now sneak out if you're careful.")

kidnapperTwo_creature = Creature("kidnapper", "A woman sat at a table eating lunch, dressed in camo. She's almost done eating, and looks like she's ready to leave."
" She doesn't know you're there", None, None, None, True)

hunter_creature = Creature("hunter", "A mid-sized man dressed in camo with a couple orange stripes. His hair has grayed and his skin wrinkled in age", None, None, None)

#Room instances -> Name, Description, Exit List, Item List, Creature List
#Room 1
    #Starting Room
basement_room_one = Room("basement", "An old and musty basement. There's an old mattress for a bed in the corner. On the other side is a small window partially covered in broken glass."
"Metal Bars covered in rust block you from leaving that way. There's an old and dented wooden door ", [], [rock_item, window_item], [kidnapper_creature])

#Room 2
closet_room_two = Room("closet", "An antique closet with worn wooden panels, creaky doors, and a timeless charm that whispers stories of the past. "
"A lot of clothes are hung up on the rail. You quickly jump into the closet, hiding behind the clothes. Before you have a chance to shut the door, a woman walks"
" into the room, and sits down to eat at the table. She can't see you, but she's blocking your path.", [] , [], [kidnapperTwo_creature])

#Room 3
frontdoor_room_three = Room("frontdoor", "You are lost. It's bright out, with a cool breeze flowing. You see a car by the garage, "
"a long gravel driveway leading away from the house. You follow the driveway's road, hoping to make it to an intersection.", [], [], [])

#Room 4
driveway_room_four = Room("driveway", "You're on a long and winding gravel road. The trees around you cover the bright sun, turning light into darkness. You can't see"
"the end of the road. You hear large and angry roar of a car starting up behind you, and you can hear the wheels rolling down the driveway heading in your direction. It’s gaining on you.",
[], None, None)

#Room 5
trail1_room_five = Room("trail", "A winding, narrow trail through dense trees, leading deeper into the quiet, shadowed heart of the forest,"
" where sunlight barely touches the ground, and the air smells of earth and moss.", [], [], [])

#Room 6
trail2_room_six = Room("trail", "A narrow, winding trail through thick woods, where the trees grow dense and tall, "
"leading to a dark cave with jagged rocks and an eerie silence that echoes within. The sky has turned dark, shadowed by a layer of ominous clouds. Rain begins to fall ", [], [], None)

#Room 6 - 2
trail2_1_room_six = Room ("trail", "After leaving the cave, you decided you never want to go back in there again. You push toward the trail, hoping to find humanity.", [], [], [])

#Room 7
cave_room_seven = Room("cave", "A small, dark cave with damp, cold walls, where water drips steadily. The air feels heavy with stillness."
"The faint smell of earth lingers, adding to its eerie atmosphere. While barely visible, you can make out the picture of what looks like bones along one of the walls", [], [bones_item], None)

#Room 8
car_room_eight = Room("car", "You find a rusty, beige car parked in a small clearing in the woods, along a wider path.", [], [], [])

#Room 8 - Good
car_room_good = Room("car", "As you sat and waited against the side of the car, you hear footsteps approaching from behind. Terrified, you look in the direction of the noise, and see"
"a man dressed in camo, holding a rifle and heading in your direction. He looks old and friendly, but cautious. You give him quite a fright when he spots you, but after careful conversing,"
"you tell him about what happened to you, and he quickly believes you, trusts you, and offers to give you a ride out of there. He tries to hand you a small, tattered piece of paper with"
" three numbers scribbled into it. The handwriting is barely legible.", [], [note_item], [hunter_creature])

#Room 9
#Tree blocks the road, kidnapper approaches. Can stay and fight or run away
treeBlock_room_nine = Room("tree", "The road curves and winds through the woods. Eventually, you come across a large pine tree that has fallen across the road, blocking the exit. "
"Looks too heavy to move. The hunter decides it's best to backtrack until you can reach a different route to leave the forest. Nervous, you try to warn him that it must have"
"been the kidnapper who caused this, but he shakes you off. Just then, you hear the rumbling of wheels along the dirt and see a different car pulling up behind you, blocking your exit. "
"You see your kidnapper exit the car that blocked you in, and the hunter exits your car to encounter him. Nervously, you exit your vehicle as well, despretely yelling to warn him of who that man really is,"
"but to no avail. The kidnapper tries to reason with the hunter, stating that you are their lost sister, who has been experiencing one of their episodes and doesn't remember who he really is."
"The hunter believes him, and drops his rifle's aim away. This was a mistake, as the kidnapper pulls out a knife and charges the hunter, catching him off, knocking the rifle away.", [], [], [hunter_creature, kidnapper_creature])

#Room 10
largeClearing_room_ten = Room("clearing", "A vast, open clearing surrounded by towering trees, with soft grass swaying in the breeze. In the center, a supply drop sits untouched, it's contents"
"sealed within the wooden crate.", [], [crate_item], [])

#Room 10 - 2
#Supplemental room to grab the radio
open_crate_room = Room("crate", "You've opened the crate. You see a few cans of bear spray, a lot of canned food, dehydrated fruit, bags of coffee beans, and a small container holding a couple radios inside.",
                       [], [radio_item, bear_spray_item], None)

#Room 11
    #Ending Room
riverExit_room_eleven = Room("river", "A large, calm river with a few rapids, littered with several large rocks. A rocky, sandy shoreline surrounds the winding river.", None, None, None)


#Exit Instances ->Name, Description, Destination(Room), transition message, 'hidden', creature blocking exit, item required to open, bad exit
    #Exit leads to room two
woodenDoor_exit = Exit("door", "an old, creaky door with faded paint, it's panels worn and warped. The door appears to be locked", closet_room_two, "You ran"
"out the door. The narrow hallway is dark and cold. You feel around with your hands until you come accross a stairway leading up. You climb."
"As you're nearing the top, you hear the sounds of someone walking upstairs. Nervously, you sprint into the nearest doorway you saw. It appears to be a closet.", False, kidnapper_creature, key_item)

    #Exit leads to room three
frontdoor_exit = Exit("door", "An aged, wooden front door, its surface weathered and rough, with chipped paint and rusty hinges.", frontdoor_room_three, "You exit the large cabin. You can hear "
"scrambling inside the cabin. Terrified, you need to act quickly.", False, kidnapperTwo_creature, None)

#Jumping out of the closet to attack the kidnapper -> Loss
frontdoor_bad_exit = Exit("fight", "Charge out of the closet, attacing the person before they can react to you", closet_room_two, "You jump out of the closet, slamming the door into the wall from"
"the speed. The woman, startled, jumps out of the chair. You get the jump on her, knocking her to the ground. She screams. She kicks you off, sending you flying across the floor, landing on your back. "
"Winded, you struggle to get up. Before you have a chance to, the man from downstairs has reached your floor, and pins you down to the ground. You've been caught.\nYou failed to escape. "
"Restarting from checkpoint.", False, None, None, True)

    #Exit leads to room four
driveway_exit = Exit("driveway", "A long and winding gravel driveway. Large trees shadow the driveway, making it difficult to see the end.", driveway_room_four, "You continue down the driveway, "
"each step sending waves of pain across your bare feet.", False, None, None)

#Exit to continue down the driveway -> Loss
driveway_exit_bad = Exit("driveway", "Continue running down the driveway, which might lead to a main road", driveway_room_four, "You sprint as fast as you can down the gravel road, the rocks digging into "
"your feet. The small rocks begin to make your feet bleed, and you trip and fall from the waves of pain. The man in the car has caught up to you. He jumps out of his car, grabs you by the shoulders,"
" and throws you into the backseat. You've been caught.\nYou failed to escape.\nRestarting from checkpoint.", False) 

    #Exit leads to room five
woods_exit = Exit("woods", "The thick and dense forest. The trees loom above you like giants.", trail1_room_five, "You decided to dart off the driveway, hoping the shake the kidnapper"
" who is approaching by car. You run off into the forest. The brush and branches on the ground cutting into your skin with every step. Your whole body hurts.", False, None, None)

    #Exit leads to room six -> Farther down the trail
woodsTwo_exit = Exit("trail", "A narrow, winding trail through the dark woods shadowed by the overcasting canopies, twisting left and right. The air is thick with whispers and a chill "
"that never fades.", trail2_room_six, "You've continued left down the trail, hoping to escape unnoticed.", False, None, None)

    #Exit leads to room seven -> Cave
cave_exit = Exit("cave", "A small rocky cave where sounds boom and echo, dancing in the wind. A chill runs down your spine as you stare into its darkness", cave_room_seven, "You enter the cave, each"
"footstep pounding like drums. Shivers run down your spine.", False, None, None)

#Bear Encounter -> Loss
cave_bad_exit = Exit("cave", "", cave_room_seven, "As you waited for the rain to end, you fell asleep its gentle lullaby. When you woke up, you were shivering, but at least the rain had stopped. "
"It was freezing in that cave. You chose to leave the cave to hopefully warm out where the sun might be out. However, as you leave the cave, you hear the roar of a black bear on your left. You screamed,"
" but it was too late.\nThis bear encounter didn't go very well. You've died.\nRestarting from checkpoint", True, None, None)

    #Exit leads to room 6.5, supplemental room that prevents you from going back to the cave, only continues down the path
trail2_exit = Exit("trail", "You peer out from the darkness of the cave back into the woods, eyeing the trail you came from", trail2_1_room_six, "You left the cave, probably for the best."
"The shelter was nice, but whatever left the bones there might've came back if you waited any longer", False, None, None)

    #Exit leads to room eight -> Finding the car
car_exit = Exit("clearing", "You look a long way down the trail. Up ahead, you think you make out the appearance of a car, but whose car is it?", car_room_eight, "You continue down the trail, coming across a larger opening"
"in the trail where the paths have divereged.", False, None, None)

#Good encounter with hunter exit
car_exit_good = Exit("hunter", "Good hunter encounter", car_room_good, "You sat and waited by the car, whose contents looked fresh enough for someone to be nearby. You hope it's not the kidnappers"
                     ,True, None, None)

#Exit leads to tree blockade
car_drive_exit = Exit("drive", "Let the driver bring you home", treeBlock_room_nine, "The two of you get into the car. The engine spurs and kicks like it's ready to give out. After a few clicks, "
"the engine wurrs and starts. You and the hunter start driving away. It's a mostly silent ride, as you're still too shaken up to converse too freely. The hunter notices, and offers you food and water, to which you"
"quickly accept. How long has it been since you last ate or drank fresh water? After eating and drinking, you start to feel a little better, but you're still too shaken to talk much.", False, None, note_item)

    #Exit leads to bad hunter encounter -> Player broke into the car
car_exit_bad = Exit("enter", "You peer into the car. Inside the car you see a blanket, some fresh sandwiches, a flashlight, a water bottle, and an open, empty box of rifle ammunition.", car_room_eight, "You "
"smash the window of the car, grabbing everything you can, eating the sandwich and drinking the water. As soon as you finish, you hear footsteps behind you. It's the hunter, and he "
"looks extremely angry that you broke into his car. He aims his rifle at you. You scream.\nYou've been caught.\nYou failed to escape.\nRestarting from checkpoint.", False, None, None)

    #Exit where the player stays and fights the kidnapper -> Loss
fight_kidnapper_exit = Exit("fight", "Stay and help the hunter fight off your kidnapper", treeBlock_room_nine, "You stay to help aid the hunter, who was fighting the hunter. Before you can make it to him"
", the hunter is stabbed and killed. You scream, but the kidnapper has already turned his target to you. He catches you. You've been caught.\nYou failed to escape.\nRestarting from checkpoint.", False, None, None)

    #Exit where you run away from the fight -> Goes to large clearing with crate
run_kidnapper_exit = Exit("run", "Run away from the fight, hoping to escape", largeClearing_room_ten, "You run away, leaving the hunter helpless in the fight. The two men fight each for a little"
" while, giving you plenty of time to escape out of sight. You make it a sizable distance away when you hear the scream of the hunter who helped you. You begin to cry, realizing the fate you left him to.",
False, None, None)

    #Open the crate
open_crate_exit = Exit("open", "Try to open the crate", open_crate_room, "You remember the note in your pocket with a 3-digit combination. You try those numbers, and the crate opens", False, None, note_item)

    #Exit to leave clearing instead of opening the crate
open_crate_exit_bad = Exit("run", "Run away from the clearing, hoping to take cover from the kidnapper's view by traveling along a trail on the opposite side of the clearing", largeClearing_room_ten,
                           "You ran across the clearing, hoping to escape from view and to shelter undear the large trees. You made it to and started running down the trail."
                           "You didn't get far before you came across a large black bear and her two cubs. You screamed, but it was too late.\nYou've been killed by the mama bear.\nYou've failed to escape."
                           "\nRestarting from checkpoint.", False, None, None)


    #River exit
radio_call_exit = Exit("call", "Use the radio to call for help", riverExit_room_eleven, "You use the radio to call for help, waiting a few seconds to listen for a voice between calls. Nobody"
    "answers. You begin to feel helpless. You begin mentaly preparing yourself to head into the woods again to continue trying to escape, when you finally hear a voice on on other side, asking if you're"
    "still there. You explain your situation, and they tell you to follow the stream on the edge of the clearing where you'll be able to receive help. Your heart pounds, but you feel a wave of relief pass"
    "over you.", False, None, radio_item)

#Add exits to exit list for Room Objects
basement_room_one.add_exit(woodenDoor_exit)
closet_room_two.add_exit(frontdoor_exit)
closet_room_two.add_exit(frontdoor_bad_exit)
frontdoor_room_three.add_exit(driveway_exit)
driveway_room_four.add_exit(woods_exit)
driveway_room_four.add_exit(driveway_exit_bad)
trail1_room_five.add_exit(woodsTwo_exit)
trail2_room_six.add_exit(cave_exit)
trail2_1_room_six.add_exit(car_exit)
cave_room_seven.add_exit(trail2_exit)
cave_room_seven.add_exit(cave_bad_exit)
trail2_room_six.add_exit(car_exit)
car_room_eight.add_exit(car_exit_bad)
car_room_eight.add_exit(car_exit_good)
car_room_good.add_exit(car_drive_exit)
treeBlock_room_nine.add_exit(fight_kidnapper_exit)
treeBlock_room_nine.add_exit(run_kidnapper_exit)
largeClearing_room_ten.add_exit(open_crate_exit)
largeClearing_room_ten.add_exit(open_crate_exit_bad)
open_crate_room.add_exit(radio_call_exit)

    #Beginning text to set the scene of the game
intro_text = ("Your name is Chara, a 21 year old college student in a small town, who loves school, studying, and spends a lot of late nights working on assignments. After a long and stressful" 
    " day of class and homework, you finally decide to leave campus to head back home to your apartment and get some rest. You don’t live far from the University, so you chose to "
    "walk today. It’s dark, the glow from the streetlights is barely enough to cut through the fog. Quiet too, the only sound is a low and dull humming from the barely functioning "
    "lights along the road. A car’s engine can be heard from behind you, driving along the same road as you. You don’t think much of it, and continue walking. Suddenly, the car begins"
    " to slow down and stops a few feet ahead of you. Your heart races as you try to run away, but the car gives chase. It stops once more in the way of your path, and the doors swing "
    "open. Two people dressed in black jump out of the car and grab hold of you. You try to struggle but the fight is over quickly when you feel the prick of a needle in your arm. Your "
    "body goes numb and weak as your eyes fall shut. The last thing you remember is being dragged into the car, and a low roar of the engine as you’re driven away. When you wake up, your body hurts."
    "You're fatigued, lost, and in a cold and dark basement. You're scared, but you must persevere if you want to find a way home safely.")

    #Ending text to end the game
ending_text = ("You follow the stream heading Northbound, and you come across a watch tower where forest rangers were waiting for your arrival. They take you in, and after resting the night at the "
    "watch tower, a state trooper arrives in the morning to take you out of the woods. After a check-in with doctors and a long questioning process with the authorities on the accounts of what "
    "occurred, they bring you home. The authorities check out the cabin you warned them about where you were first dragged to, but they find no evidence of anyone having lived there recently. "
    "The kidnappers were never caught, but at least you’re safe. You’re safe, right?")

#Create and run the game
game_start = Game(chara_player, basement_room_one, riverExit_room_eleven, intro_text, ending_text)
Game.start(game_start)