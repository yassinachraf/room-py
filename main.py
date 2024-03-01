from room import Room
from character import Enemy, Friend

print()
print("******************************************************************************")
print("** Welcome to the bootcamp Text Based Adventure Game (TBAG) **")
print("******************************************************************************")
print()

"""These are attributes"""
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

kitchen.set_description ("A dark and dirty room buzzing with files")
ballroom.set_description("A decaying ballroom, etc.")
dining_hall.set_description("A dining room frozen etc.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

jenny = Friend("Jenny", "A friendly spirit who loves sunshine and laughter.")
kitchen.set_character(jenny)

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There's no one here to talk to.")
    elif command == "fight":
        if inhabitant is not None:
            print("What will you fight with?")
            fight_with = input("> ")
            if inhabitant.fight(fight_with) == False:
                print("You lost the fight.")
                print("Game Over.")
                break
        else:
            print("There's no one here to fight.")
    elif command == "hug":
        if isinstance(inhabitant, Friend):
            inhabitant.hug()
        else:
            print("There's no one here to hug.")
    elif command == "offer":
        if isinstance(inhabitant, Friend):
            print("What will you offer?")
            offer_item = input("> ")
            inhabitant.offer_gift(offer_item)
        else:
            print("They don't seem interested in any offers.")
            