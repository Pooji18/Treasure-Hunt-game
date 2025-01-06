def snake_room():
 print("\nThere is a snake here.")
 print("Behind the sanke is another door.")
 print("The snake is having eggs!")
 print("What would you do?(1 or2)")
 print("1).Take the eggs.")
 print("2).taunt the snake.")
 a=int(input())
 if(a==1):
	 print("You want eggs not treasure!! Thats why the sanke killed you.\n Game over");
	 lets_play_again()
 elif(a==2):
 	treasure_room() 
def monster_room():
 print("\nNow you entered the room of monster!")
 print("The monster is sleeping.")
 print("Behind the monster,there is another door.What would you do?(1 
or 2)")
 print("1).Go through the door silently")
 print("2).Kill the monster and show your courage!")
 a=int(input())
 if(a==1):
 treasure_room()
 elif(a==2):
 print("The monster was hungry,he/it ate you.\nGame Over");
 lets_play_again() 
def treasure_room():
 print("\nYou are now in a room filled with diamonds!")
 print("And there is a door ti!")
 print("What would you do\?(1 or 2)")
 print("1).Take some diamonds and go through the door.")
 print("2).Just go through the door")
 a=int(input())
 if(a==1):
 print("Game over")
 lets_play_again()
 elif(a==2):
 print("Congrulations ,You have won the treasure")
 lets_play_again() 
def lets_play_again():
#This function lets the user quit the application or progress to playing.
 print("")
 print ("Do you want to play again? (y or n)")
 choice1 = input() # Sets variable to user input
 if choice1.lower().startswith('y'):
 print("Okay lets continue then!")
 start()
 elif choice1.lower().startswith('n'):
 game_over()
 print("Thank you, I hope you will play next time!")
 print("Thank you for playing!")#Terminates the programme
 else:
 print("Sorry, that is an invalid answer. Please restart the 
programme")
 print("")
 quit()
def game_over():
 print("Reason:")
 input()
def start():
#Introduces the user
 print("You are standing in a dark room. \nThere is a door to your left 
and right, which onedo you take? (l or r)")
 a=input()
 if a =='l':#If function checks for the first letter
 snake_room()
 elif a == 'r':
 monster_room()
 else:
 print("Please check your input and try again.")
start()
