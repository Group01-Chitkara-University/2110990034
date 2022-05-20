from time import sleep          # importing sleep function that halts the execution of a program for a specified time period

userArray = []                  # initialized empty user and password arrays
passArray = []
balance = [0] * 99              # initialized an 0 array

'''
    Start function:
        1. asks the user for a specified input and can execute itself again 4 times if the user enters wrong inputs and then exits.
        2. on the basis of choice entered the program calls the specified function
'''

def start():
    choice = ''
    i = 0
    while choice != 'l' and choice != 'c' and choice != 'q':
        choice = input("\nChoose from the options below\n\tl -> login\n\tc -> create an account \n\tq -> quit\n\n> ")
        if ( i== 3):
            exit(0)
        i += 1
        
    if choice == "l":
        login()
    elif choice == "c":
        createAccount()
    elif choice == "q":
        exit(0)

'''
    Request balance function:
        1. displays the balacne of the user specified and then after 1 second the program exits to the main menu
'''

def reqBal(username):
    print("\nDear, ",username, " you have $", balance[userArray.index(username)], " in your account")
    sleep(1)
    printMainMenu(username)

# MAIN PROGRAM STARTS HERE

print("\nWelcome to the ATM Project\n")
start()     # Calling the start function