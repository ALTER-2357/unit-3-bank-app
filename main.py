p = 0
b = 0
s = 0
uid = 0
n = 0
an = 0
user_id = int(uid)
password = str(p)
account_holder = str(n)
balance = int(b) 
sortcode = int(s)
account_number = int(an)





def main():
    
    print ("Welcome " + user_id)

    print ("What would you like to do?")
    print ("1. Withdraw")
    print ("2. Deposit")
    print ("3. Check balance")
    print ("4. Exit")
    choice = int(input())
    if choice == 1:
        withdraw()
    elif choice == 2:
        deposit()
    elif choice == 3:
        check_balance()
    elif choice == 4:
        exiter()


def exiter():
    print ("Thank you for using our services")
    exit()




def deposit():
    print ("How much would you like to deposit?")
    deposit_amount = int(input())
    balance = balance + deposit_amount
    print ("Your new balance is " + str(balance))
    print ("Would you like to make another transaction?")
    answer = input()
    if answer == "yes":
        print ("What would you like to do?")
        print ("1. Withdraw")
        print ("2. Deposit")
        print ("3. Check balance")
        print ("4. Exit")
        choice = int(input())
        if choice == 1:
            withdraw()
        elif choice == 2:
            deposit()
        elif choice == 3:
            check_balance()
        elif choice == 4:
            exit()
    elif answer == "no":
        exiter()


def withdraw(): 
    print ("How much would you like to withdraw?")
    withdraw_amount = int(input())
    balance = balance - withdraw_amount
    print ("Your new balance is " + str(balance))
    print ("Would you like to make another transaction?")
    answer = input()
    if answer == "yes":
        print ("What would you like to do?")
        print ("1. Withdraw")
        print ("2. Deposit")
        print ("3. Check balance")
        print ("4. Exit")
        choice = int(input())
        if choice == 1:
            withdraw()
        elif choice == 2:
            deposit()
        elif choice == 3:
            check_balance()
        elif choice == 4:
            exit()
    elif answer == "no":
        exiter()


def check_balance():  
    print ("Your current balance is " + str(balance))
    print ("Would you like to make another transaction?")
    answer = input()
    if answer == "yes":
        print ("What would you like to do?")
        print ("1. Withdraw")
        print ("2. Deposit")
        print ("3. Check balance")
        print ("4. Exit")
        choice = int(input())
        if choice == 1:
            withdraw()
        elif choice == 2:
            deposit()
        elif choice == 3:
            check_balance()
        elif choice == 4:
            exit()
    elif answer == "no":
        exiter()



def transfer():
    print ("How much would you like to transfer?")
    transfer_amount = int(input())
    balance = balance - transfer_amount
    print ("Your new balance is " + str(balance))
    print ("Would you like to make another transaction?")
    answer = input()
    if answer == "yes":
        print ("What would you like to do?")
        print ("1. Withdraw")
        print ("2. Deposit")
        print ("3. Check balance")
        print ("4. Exit")
        choice = int(input())
        if choice == 1:
            withdraw()
        elif choice == 2:
            deposit()
        elif choice == 3:
            check_balance()
            
            
            
          
