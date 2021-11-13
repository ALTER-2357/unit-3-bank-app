p = 0
s = 0
uid = 0
n = 0
an = 0
user_id = str(uid)
password = str(p)
account_holder = str(n)
sortcode = int(s)
account_number = int(an)

b = 1000

print ("Welcome " + user_id)
print ("What would you like to do?")
print ("1. Withdraw")
print ("2. Deposit")
print ("3. Check balance")
print ("4. Exit")
choice = int(input())
x = choice


def exiter():
    print("Thank you for using our services")
    exit()






def deposit(balance=b):
    print("How much would you like to deposit?")
    deposit_amount = int(input())
    balance = balance + deposit_amount
    print("Your new balance is " + str(balance))
    print("Would you like to make another transaction?")
    answer = input()
    if answer == "yes":
        print("What would you like to do?")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check balance")
        print("4. Exit")
        choice1 = int(input())
        main()
        if answer == "no":
            exiter()






def withdraw(balance=b):
    print("How much would you like to withdraw?")
    withdraw_amount = int(input())
    balance = balance - withdraw_amount
    print("Your new balance is " + str(balance))
    print("Would you like to make another transaction?")
    answer = input()
    if answer == "yes":
        print("What would you like to do?")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check balance")
        print("4. Exit")
        choice2 = int(input())
        x = choice2
        if answer == "no":
            exiter()


def check_balance(balance=b):
    print("Your current balance is " + str(balance))
    print("Would you like to make another transaction?")
    answer = input()
    if answer == "yes":
        print("What would you like to do?")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check balance")
        print("4. Exit")
        choice3 = int(input())
        x = choice3
        if answer == "no":
            exiter()




def transfer(balance=b):
    print("How much would you like to transfer?")
    transfer_amount = int(input())
    balance = balance - transfer_amount
    print("Your new balance is " + str(balance))
    print("Would you like to make another transaction?")
    answer = input()
    if answer == "yes":
        print("What would you like to do?")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check balance")
        print("4. Exit")
        choice4 = int(input())
        x = choice4
        main()
        if answer == "no":
            exiter()




def main(choice = x) :
    if choice == 1:
        withdraw()
    if choice == 2:
        deposit()
    if choice == 3:
        check_balance()
    if choice == 4:
        exiter()

main()
