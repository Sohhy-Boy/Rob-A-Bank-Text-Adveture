import random
from random import choice
from room import Room
from random import randint 
from character import Enemy
import sys
from item import Item
import time
from rpginfo import RPGInfo

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"



north_gardens = Room("North Gardens")
west_gardens = Room("West Gardens")
shed = Room("Shed")
east_gardens = Room("East Gardens")
roof = Room("Roof")
secondfloor = Room("Second Floor") 
bathroom = Room("Bathroom")
firstfloor = Room("First Floor") 
firstfloormeetingroom = Room("First Floor Meeting Room")
firstfloorbreakroom = Room("First Floor Break Room")
groundfloor = Room("First Floor")
managerroom = Room("Manager Room")
customerservice = Room("Customer Service")
basement = Room("Basement")
vault = Room("Vault")
escapetunnel = Room("Escape tunnel")

number1 = random.randint(1,10)
number2 = random.randint(5,20)
code = number1 * number2


backpack = []

firstfloormeetingroom.set_description("There is a vending machine here")

print("Oh no! You are being chased by cops. \nYou have 2 minutes to get to the secret underground tunnel before the cops come or else the game will be over and you will fail. \nSome useful commands are 'talk' to talk, 'give' to give items to characters, 'craft' to craft items, 'money' to view how poor you are and 'time' to see when the cops will catch you. \nYour time starts now. To view how much time you have left, send 'time' ")
print("There are " + str(Room.number_of_rooms) + " rooms to explore.")


print("\n welcome to game")

money = 0
cash_value = 15

roof.link_room(secondfloor, "down")

firstfloorbreakroom.set_description("There is a vending machine here, selling 'chips', 'chocolate', 'soda' and 'icecream'")

Noah_The_Teller = Enemy("Noah", "A miserable man just trying to make ends meet.")
Noah_The_Teller.set_conversation("Please... don't hurt me... I'll give you my ID card for soda and $10")
Noah_The_Teller.set_weakness("money")

bob_the_manager = Enemy("Bob the Boss", "The manager of the bank")
bob_the_manager.set_conversation(f"You want the escape tunnel code huh? The code is {number1} times {number2}")
bob_the_manager.set_weakness("o")

sally_the_supervisor = Enemy("Sally the Supervisor", "A poor part time shift manager trying to get an Art's degree")
sally_the_supervisor.set_conversation("How did you get here?? I will give you the escape room keys for some flowers and chocolate and $50")
sally_the_supervisor.set_weakness("flowers")

Garry_the_groundsman = Enemy("Garry the Groundsman", "once rich, now poor.")
Garry_the_groundsman.set_conversation("Dont talk to me")
north_gardens.set_character(Garry_the_groundsman)

firstfloormeetingroom.set_character(Noah_The_Teller)
managerroom.set_character(bob_the_manager)
vault.set_character(sally_the_supervisor)


current_room = north_gardens

cash = Item("Cash")
cash.set_description("MONEY!!!")
bathroom.set_item(cash)

fuel = Item("Fuel")
fuel.set_description("Maybe for a bomb or something?")
west_gardens.set_item(fuel)

flowers = Item("Flowers")
flowers.set_description("Pretty flowers")
east_gardens.set_item(flowers)



oxidiser = Item("Oxidiser")
oxidiser.set_description("Maybe for a bomb or something?")
basement.set_item(oxidiser)

idcard = Item("ID Card")

bomb = Item("Bomb")
bomb.set_description("Maybe to blow up doors and get access to places with money")

rope = Item("Rope")
rope.set_description("Rope To Climb")
north_gardens.set_item(rope)

manager_keys = Item("Manager Room Keys")

chips = Item("Chips")
chips.set_description("Salty potato chips in a crinkly bag.")

soda = Item("Soda")
soda.set_description("Refreshing fizzy drink.")

chocolate = Item("Chocolate")
chocolate.set_description("Sweet chocolate bar.")

icecream = Item("Icecream")
icecream.set_description("Cold and creamy treat.")


start_time = time.time()
time_limit = 180

vault.lock()
managerroom.lock()
basement.lock()

crate = Item("Crate")
crate.set_description("A wooden crate with cash inside. Take it to grab the cash.")
crate_value = 20
vault.set_item(crate)

north_gardens.link_room(west_gardens, "west")
north_gardens.link_room(east_gardens, "east")
west_gardens.link_room(north_gardens, "east")
east_gardens.link_room(north_gardens, "west")
east_gardens.link_room(shed, "north")
shed.link_room(east_gardens, "south")

roof.link_room(secondfloor, "down")
secondfloor.link_room(bathroom, "east")
bathroom.link_room(secondfloor, "west")
secondfloor.link_room(firstfloor, "down")

firstfloor.link_room(secondfloor, "up")
firstfloor.link_room(firstfloorbreakroom, "east")
firstfloor.link_room(firstfloormeetingroom, "west")
firstfloormeetingroom.link_room(firstfloor, "east")
firstfloorbreakroom.link_room(firstfloor, "west")
firstfloor.link_room(groundfloor, "down")

groundfloor.link_room(firstfloor, "up")
groundfloor.link_room(customerservice, "east")
groundfloor.link_room(managerroom, "west")
managerroom.link_room(groundfloor, "east")
customerservice.link_room(groundfloor, "west")
groundfloor.link_room(basement, "down")

basement.link_room(groundfloor, "up")
basement.link_room(escapetunnel, "east")
basement.link_room(vault, "west")
vault.link_room(basement, "east")

customerservice.link_room(east_gardens, "north")
east_gardens.link_room(customerservice, "south")

taunts = [
    "Dispatch: Suspect last seen near the gardens!",
    "Cops: Surround the escapes to make sure he can't leave",
    "Police: We have eyes on the building"
    "Cops: A few minutes out."
]

events = [
    "A rat scurries across the floor. Gross.",
    "You hear footsteps above you...",
    "The lights flicker. Creepy.",
    "You find gum stuck to the wall. Ew."
]

while True:
    print("\n")         
    current_room.get_details()
    
    if manager_keys in backpack:
        managerroom.unlock()
    
    if idcard in backpack:
        basement.unlock()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    
    item = current_room.get_item()
    if item is not None:
        item.describe()
        
    if bomb in backpack and current_room == basement:
        print("You blew up the vault doors")
        vault.unlock()

    command = input("> ")    

    if command in ["north", "south", "east", "west", "up", "down"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Hooray, you won the fight!")
                current_room.set_character(None)
            else:
                print("Oh dear, you lost the fight.")
                sys.exit
        else:
            print("There is no one here to fight with")

    elif command == "take":
        if item is not None:
            if item == cash:
                print(f"You put the cash in your pocket. It is worth {cash_value}")
                backpack.append(item.get_name())
                current_room.set_item(None)
                money += cash_value
            
            elif item == rope:
                print("You cant take that")
            
            elif item == crate:
                print(f"You open the crate and take ${crate_value}. You can't carry the crate itself.")
                money += crate_value

            else:
                print("You put the " + item.get_name() + " in your backpack")
                backpack.append(item.get_name())
                current_room.set_item(None)

    elif command == "buy":
        if current_room == firstfloorbreakroom:
            print("What do you want to buy? (chips, soda, chocolate, icecream)")
            choice = input("> ").lower()

            if choice == "soda":
                if money >= 5:
                    money -= 5
                    backpack.append(soda)
                    print("you got soda, try water next time")
                else:
                    print("Not enough money lol")
            elif choice == "chocolate":
                if money >= 5:
                    money -= 5
                    backpack.append(chocolate)
                    print("you got chocolate, yummy")
                else:
                    print("Not enough money lol")
            elif choice == "chips":
                if money >= 5:
                    money -= 5
                    backpack.append(chips)
                    print("you got chips, crunchy. You should dip them in chocolate syrup, makes it better.")
                else:
                    print("Not enough money lol")
            elif choice == "icecream":
                if money >= 5:
                    money -= 5
                    backpack.append(icecream)
                    print("You got icecream, and a complimentary brain freeze to go along with it. ")
                else:
                    print("Not enough money lol")
            else:
                print("Not a valid option.")
            


    elif command == "money":
        print(money)
    elif command == "money11":
        money_add = int(input("How much money to add? "))
        money += money_add
        print(f"You now have {money}")

    elif command == "give":
        if current_room == firstfloormeetingroom:
            if soda in backpack and money >= 10:
                    money -= 10
                    print(f"Noah gives his ID card. You can use it to access certain areas. You have {remaining_time} left")
                    backpack.append(idcard)
            else:
                print("You do not have the required items. You require $10 and soda")
        elif current_room == vault:
            if chocolate in backpack and money >= 50:
                print("You give Sally an the items and she gives the manager keys in return instead of the escape tunnel keys, plus she doesn't even take the flowers.")
                backpack.append(manager_keys)
                money -= 50
            else:
                print("You do not have the required items. You need $50, flowers and chocolate.")

    elapsed_time = time.time() - start_time
    remaining_time = time_limit - elapsed_time
    if remaining_time <= 0:
        print(f"\n TIMES UP!!! You failed. The police caught you. You ended with {money}, though the police take it all")
        sys.exit()

    elif command == "time":
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        print(f"Time left: {minutes}m {seconds}s")
    
    elif command == "end":
        print("Game ended.")
        sys.exit()
    
    if random.randint(1,5) == 1:
        print(random.choice(events))

    elif command == "climb":
        if current_room == north_gardens:
            current_room = roof
            print("You climbed rope")
        else:
            print("What you gonna climb, the walls? Theres nothing to climb")

    elif command == "craft":
        if "Oxidiser" in backpack and "Fuel" in backpack and current_room == shed:
            backpack.append(bomb)
            print("You have bomb")
        else:
            print("What you trying to craft, happiness?")

    elif command == "timeset":
       time_limit = int(input("time to add")  )
       print(f"{time_limit}")

    if random.randint(1, 20) == 1:
        bonus = random.randint(5, 25)
        money += bonus
        print(GREEN + f"You stumble across a hidden $ {bonus} in loose change!" + RESET)

    if random.randint(1, 8) == 1:  
        print(RED + random.choice(taunts) + RESET)

    if current_room == escapetunnel:
        code_input = int(input("Enter the escape tunnel code: "))
        if code_input == code and money >= 100:
            print(f"\nCongratulations! You escaped with ${money}. You win!")
            RPGInfo.credits()
            sys.exit()
 
        elif code_input == code:
            print(f"\nYou entered the right code, but you only have ${money}. You need at least $100!")
            current_room = basement
        else:
            print("Wrong code! The tunnel remains locked.")
            current_room = basement

        
