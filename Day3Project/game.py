print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")
print('''
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |    ______    | || |      __      | || | ____    ____ | || |  _________   | |
| |  .' ___  |   | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | |
| | / .'   \_|   | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | |
| | | |    ____  | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | |
| | \ `.___]  _| | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | |
| |  `._____.'   | || ||____|  |____|| || ||_____||_____|| || | |_________|  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 
''')
direction = input("which way do you want to go? left or right").lower()
action = input("do you want to swim or wait? ").lower()
door = input("choose a door? red, blue or yellow").lower()

if direction == "left":
    if action == "wait":
        if door == "yellow":
            print("You Won!")
        else:
            print("you lost")
    else:
        print("you lost")
else:
   print("you lost")



