import os
import Player
import winsound


introMsg = """
*****************************************************************************************
* Welcome,stranger.                                                                     *
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons.  *
* In a country where magic rules, anything is possible if you wish so.                  *
* It all depends on you, brave hero.                                                    *
*****************************************************************************************
"""
sound = "Main_Menu.wav"
winsound.PlaySound(sound, winsound.SND_ASYNC)


print(introMsg)
print("Would you like to start the adventure?")
user_answer = input("Yes ot No -> ")
if user_answer.upper() == "YES":
    print("Let's start!")
    os.system("cls")
    answer = input("""Chose a type of player: 
1 for Warrior 
2 for Wizard
-> """)
    if answer == "1":
        player_name = input("""You have chosen to be a mighty warrior.     
What is your name?
-> """)
        player = Player.Warrior(player_name)
        print("Intro to the world intro msg.")
        input("Press a key to continue...")

        os.system('cls')  # clear screen
        sound = "Exploring.wav"  # play sound Exploring
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        print("""You are in the middle of a crossroads.
You have 3 paths in front of you:
1. Going to a village.
2. Going to a forest.
3. Going to a desert.""")
        path_option = input("What is your destination?")
    elif answer == "2":
        player_name = input("""You have chosen to be a mighty wizard.     
What is your name?
-> """)
        player = Player.Wizard(player_name)
        # Need to implement an intro msg
        print("Intro to the world.")
        os.system('cls')

    else:
        print("Chose a valid option.")

else:
    print("Thank you, Goodbye!")
