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
    Login function:
        1. first checks if their are any previous accounts created on the device [true everytime the program is rerun][database not connected]
        2. if above condition is false then moves on and asks the user for input of username ans validates it in the above stored array
        3. if it evaluates to true then asks the user for password else alerts the user to register as no such account exists
        3. then matches the password of the current user and if all is well then displays the message of login successful
        4. at last it calls the main menu function which has extended functionality about the user actions
'''

def login():
    global user, paswd
    if (len(userArray) == 0 and len(passArray) == 0):
        print("\nCurrently we have no accounts! Please register first!!")
        start()
    else:
        user = input("\n\nEnter your username: ")
        if(not(user in userArray)):
            print("\nNo such user exists! Please register first!!")
            start()
        else:
            paswd = input("\nEnter your password: ")
            if(paswd == passArray[userArray.index(user)]):
                print("\n***LOGIN SUCCESSFUL*")
                printMainMenu(user)
            else:
                print("\nWRONG PASSWORD! Please start again")
                start()

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
    Deposit function: 
        1. asks the user for amount to be entered and then increments the balance at the same index that the username has to avoid redundancy
        2. after that displays the message of transaaction successful
        3. sleep function here halts the processing of the program for 1 second here
'''
    
def deposit(username):
    bal = int(input("\nEnter the amount to be deopited: $"))
    balance[userArray.index(username)] += bal
    sleep(1)
    print("\nTRANSACTION SUCCESSFUL")
    sleep(1)
    printMainMenu(username)

'''
    Withdraw function:
        1. first check if the user has 0 balance. if it is true then alerts the user of the 0 balance and tells them to deposit some money first
        2. if it is false then asks the user to enter the amount to be withdrawn and checks wether it is greater than the balance of user or not
        3. if it is greater than the balance then shows an error and goes to main menu and user has to again use the functionality
        4. if it is smaller then the transaction is successful and user is directed to main menu after 1 second
'''

def withdraw(username):
    if(balance[userArray.index(username)] == 0):
        print("\nYou have 0 balance! Please deposit some money first.")
        sleep(1)
        printMainMenu(username)
    else:
        withMoney = int(input("\nEnter the amount to be withdrawn: $"))
        if(withMoney > balance[userArray.index(username)]):
                print("\nInsufficient balance in your account! Please try again!!")
                sleep(1)
                printMainMenu(username)
        else:
            balance[userArray.index(username)] -= withMoney
            sleep(1)
            print("\nTRANSACTION SUCCESSFUL")
            sleep(1)
            printMainMenu(username)

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