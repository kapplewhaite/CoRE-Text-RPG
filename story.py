class_choice = "None"
player_class = "None"

def intro_scene():
  print("""The current time is 3:00 AM. You are starving. Hungry enough to eat a horse, or even a lawnmower. Specifically a lawnmower from Home Depot.
You jump out of bed, eager for a feast. You quickly approach Home Depot, as running at hyper-sonic speeds is a natural phenomenon for a Home Depot veteran. 
"Hey Kid" 
Says someone behind the door, but it isn't Dream. 
Who could it be? You walk forward, ever so slightly, and ELMO comes dashing towards you. It seems as though he has taken more than his daily dosage of crack, and is about to hit you. 
Which Weapon will you pick up? 
Sword 
Bow 
Wand.""")
  
  while class_choice != "sword" or class_choice != "s" or class_choice != "bow" or class_choice != "b" or class_choice != "wand" or class_choice != "w":
    class_choice = input("Your choice: ").lower()
    
    if class_choice == "sword" or class_choice == "s":
      player_class = "Swordsman"
      break

    elif class_choice == "bow" or class_choice == "b":
      player_class = "Archer"
      break

    elif class_choice == "wand" or class_choice == "w":
      player_class = "Mage"
      break
      
    else:
      print("That is not a valid choice. Please try again.")
      continue
    
  if player_class == "Swordsman":
    print("ELMO: A Swordsman?? I need to get rid of you right now!")
    
  if player_class == "Archer":
    print("ELMO: An Archer?? I need to get rid of you right now!")
    
  if player_class == "Mage":
    print("ELMO: A Mage?? BURN AT THE STAKE, WITCH!")
    
  print("You have no choice but to fight ELMO. You have no choice but to fight ELMO. You have no choice but to fight ELMO. You have no choice but to fight ELMO. You have no choice but to fight ELMO. You have no choice but to fight ELMO. You have no choice but to fight ELMO. You have no choice but to fight ELMO.")