import time
import random

p = 0
s = 0
uid = 0
n = 0
an = 0
user_id = str(uid)
password = str(p)
account_holder = str(n)
sortcode = int(s)
account_number = (an)

b = 1000

print("Welcome to the bank of Python")
print("What is your account number?")
account_number = input()
print("What is your password?")
print ("Welcome " + account_number)





def exiter():
    print("Thank you for using our services")
    exit()


def deposit(balance=b):
    print("How much would you like to deposit?")
    deposit_amount = int(input())
    balance = balance + deposit_amount
    time.sleep(1)
    print("Your new balance is " + str(balance))
    time.sleep(1)
    asker()




def withdraw(balance=b):
    print("How much would you like to withdraw?")
    withdraw_amount = int(input())
    balance = balance - withdraw_amount
    time.sleep(1)
    print("Your new balance is " + str(balance))
    time.sleep(1)
    asker()


def check_balance(balance=b):
    time.sleep(1)
    print("Your current balance is " + str(balance))
    asker()




def transfer(balance=b):
    account_number = random.randint(100000000 , 999999999) 
    print("How much would you like to transfer?")
    if int(input()) > balance:
        print("You do not have enough funds")
        asker()
    transfer_amount = int(input())
    print("How would you like to transfer to?")
    transfer_name = input()
    print("is the account number " + str(account_number)+ " correct")
    answer = str(input())
    if answer == "yes":
        balance = balance - transfer_amount
    time.sleep(1)
    print("transfer to " + str(transfer_name) + " is complete")
    time.sleep(.5)
    print("Your new balance is " + str(balance))
    time.sleep(.5)
    asker()
    if answer == "no":
         print("Please try again")
         transfer()

   




def asker():
    print("Would you like to make another transaction?")
    answer = input()
    if answer == "yes":
        main()
    if answer == "no":
            exiter()




def main():

    print("What would you like to do?")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check balance")
    print("4. transfer")
    print("5. Exit")
    choice = int(input())
    if choice == 1:
        withdraw()
    if choice == 2:
        deposit()
    if choice == 3:
        check_balance()
    if choice == 4:
        transfer()
    if choice == 5:
        exiter()
        
        
main()