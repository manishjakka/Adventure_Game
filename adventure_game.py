import time
import random
import sys


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0)


def intro():
    print_pause("You find yourself standing in an open field, filled"
                "with grass and yellow wildflowers.")
    print_pause("Rumor has it that a dragon is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")


list = ["wicked fairy", "pirate", "lion"]
enemy = random.choice(list)


def house(items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door"
                "opens and out steps a %s " % enemy)
    print_pause("Eep! This is the %s house!" % enemy)
    print_pause("The %s attacks you!" % enemy)
    print_pause("You feel a bit under-prepared for this,"
                "what with only having a tiny dagger.")
    while True:
        choice = input("Would you like to (1) fight or (2) run away")
        if choice == '1':
            if "sword" in items:
                print_pause("As the %s moves to attack, you unsheath "
                            "your new sword." % enemy)
                print_pause("The Sword of Ogoroth shines brightly in your"
                            "hand as you brace yourself for the attack.")
                print_pause("But %s takes one look at your shiny new"
                            "toy and runs away!" % enemy)
                print_pause("You have rid the town of the"
                            "%s.You are victorious!" % enemy)
                play_again()
                break
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for %s" % enemy)
                print_pause("You have been defeated!")
                play_again()
                break
        elif choice == '2':
            print_pause("You run back into the field. Luckily, "
                        "you don't seem to have been followed.")
            field(items)
        else:
            print_pause("sorry i dont undestand")


def play_again():
    while True:
        play = input("Would you like to play again? (y/n)")
        if play == 'y':
            print_pause("Excellent! Restarting the game ...")
            play_game()
        elif play == 'n':
            print_pause("Thanks for playing! See you next time.")
            sys.exit()
        else:
            print_pause("sorry i dont undestand")


def cave(items):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger "
                "and take the sword with you.")
    print_pause("You walk back out to the field.")
    items.append("sword")
    field(items)


def field(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        floor = input("Please enter 1 or 2.")
        if floor == '1':
            house(items)
        elif floor == '2':
            cave(items)


def play_game():
    items = []
    intro()
    field(items)


play_game()
