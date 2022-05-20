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
    Create account function:
        1. asks the user for their username and password
        2. then stores it in the user array and password array
'''

def createAccount():
    user = input("\nPlease enter your User Name: ")
    paswd = input("\nPlease enter a Password: ")

    userArray.append(user)
    passArray.append(paswd)

    start()

'''
    Main menu function:
        1. greets the user and asks them for their choice on different actions available like deposit, withdraw, request balance.
        2. if the user enters wrong input more than 2 times then the program quits and goes to the starting stage
        3. after the user enters a valid choice it validates it and calls a function accordingly
'''

def printMainMenu(username):
    print("\nWelcome, ",username,"! Please choose from below")
    i = 0
    choice = ''
    while choice != 'd' and choice != 'w' and choice != 'r' and choice !='q':
        choice = input("\n\td -> deposit money\n\tw -> withdraw money\n\tr -> request balance\n\tq -> quit\n\n> ")
        if i == 2:
            print("\nInvalid input received too many times exiting ....")
            sleep(2)
            start()

    if choice == 'd':
        deposit(username)
    elif choice == 'w':
        withdraw(username)
    elif choice == 'r':
        reqBal(username)
    elif choice == 'q':
        print("\nThank you, ",username, "! Program exiting ......")
        sleep(1)
        start()
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