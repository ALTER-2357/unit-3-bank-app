import time
import random


#n = 0
#an = 0
#s = 0
#account_holder = str(n)
#sortcode = int(s)
#account_number = (an)


p = 0
uid = 0
user_id = str(uid)
password = str(p)
b = 1000                                                                #sets the balance to 1000

print("Welcome to the bank of Python")
print("What is your account number?")
account_number = input()
print("What is your password?")
password = input() 
print ("Welcome " + account_number) 

#   1. Withdraw

def withdraw(balance=b):
    print("How much would you like to withdraw?")                      #asks how much the user would like to withdraw
    withdraw_amount = int(input())                                     #takes the amount the user would like to withdraw
    if int(withdraw_amount) > balance:                                 #checks if the amount is greater than the balance to see if it is possible to withdraw money
        print("You do not have enough funds")
        asker()

    balance = balance - withdraw_amount                                #subtracts the amount the user would like to withdraw from the balance
    time.sleep(1)
    print("Your new balance is " + str(balance))                       #prints the new balance
    time.sleep(1)                                                      
    asker()                                                            #asks if the user would like to make another transaction

#   2. Deposit

def deposit(balance=b):
    print("How much would you like to deposit?")
    deposit_amount = int(input())                                       #takes the amount the user would like to deposit
    if int(deposit_amount) < 0:                                         #checks if the amount is less than 0
        print("Please try again")
        deposit()                                                       #asks if the user would like to make another transaction
    balance = balance + deposit_amount                                  #adds the amount the user would like to deposit to the balance
    time.sleep(1)
    print("Your new balance is " + str(balance))                        #prints the new balance
    time.sleep(1)
    asker()

#   3. Check balance
 
def check_balance(balance=b):
    time.sleep(1)
    print("Your current balance is " + str(balance))                    #prints the current balance
    asker()

 #  4. transfer
def transfer(balance=b):
    account_number = random.randint(100000000 , 999999999)               #generates random for account number
    print("How much would you like to transfer?")
    if int(input()) > balance:                                           #checks if the amount is greater than the balance to see if it is possible to transfer money
        print("You do not have enough funds")
        asker()                                                          #asks if the user would like to make another transaction
    transfer_amount = int(input())                                       #takes the amount the user would like to transfer
    print("How would you like to transfer to?")
    transfer_name = input()                                              #takes the name of the account the user would like to transfer to
    print("is the account number " + str(account_number)+ " correct")    # asks if the account number is correct
    answer = str(input()) #takes the answer from the user
    if answer == "yes":
        balance = balance - transfer_amount                              # subtracts the amount the user would like to transfer from the balance
    time.sleep(1)
    print("transfer to " + str(transfer_name) + " is complete")          #prints that the transfer is complete
    time.sleep(.5)
    print("Your new balance is " + str(balance))                         #prints the new balance
    time.sleep(.5)
    asker()
    if answer == "no":                                                   #asks if the user would like to make another transaction
         print("Please try again")
         transfer() 

   


def asker():                                                             #asks if the user would like to make another transaction
    print("Would you like to make another transaction?")
    answer = input() 
    if answer == "yes":
        main()
    if answer == "no":
            exiter()


def exiter():                                                            #exits the program
    print("Thank you for using the bank of Python")
    time.sleep(1)
    exit()


def main():                                                              #asks the user what they would like to do

    print("What would you like to do?")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check balance")
    print("4. transfer")
    print("5. Exit")
    choice = int(input())                                               #takes the user's choice
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