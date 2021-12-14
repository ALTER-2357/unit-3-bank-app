import time
import random


b = 1000                                                             

def login():
    print("Please enter your user id")
    user_id = input()
    print("Please enter your password")
    password = input()
    if user_id == "admin" and password == "admin":
        print("Please try again")
        login()
    else:
        main(user_id)

def main(user_id):
       
    print("Welcome to the bank of Python user " + str(user_id))
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

def asker():                                                        
    print("Would you like to make another transaction?")
    answer = input() 
    if answer == "yes":
        main()
    if answer == "no":
            exiter()

def withdraw(balance=b):
    print("How much would you like to withdraw?")
    withdraw_amount = int(input())                                     
    if int(withdraw_amount) > balance:                               
        print("You do not have enough funds")
        asker()

    balance = balance - withdraw_amount                               
    time.sleep(1)
    print("Your new balance is " + str(balance))                      
    time.sleep(1)                                                      
    asker()                                                            

def deposit(balance=b):
    print("How much would you like to deposit?")
    deposit_amount = int(input())                                      
    if int(deposit_amount) < 0:                                      
        print("Please try again")
        deposit()                                                     
    balance = balance + deposit_amount                                
    time.sleep(1)
    print("Your new balance is " + str(balance))                       
    time.sleep(1)
    asker()

def check_balance(balance=b):
    time.sleep(1)
    print("Your current balance is " + str(balance))                    
    asker()

 #  4. transfer

def transfer(balance=b):
                 
    print("How much would you like to transfer?")                                                   
    transferamount = int(input())                                                
    answer = str(input("is the person you are transferring to a payee?"))
    if answer == "yes":
        transfer_payee(transferamount)
    if answer == "no":
        transfer_normal(transferamount)
    
def transfer_payee(transferamount, balance=b):
    account_number = random.randint(100000000 , 999999999)  
    print("What is the name of the payee?")
    transfer_name = input()
    print("is the account number " + str(account_number)+ " correct")
    answer = str(input())
    if answer == "yes":
        balance = balance - transferamount
        time.sleep(1)
        print("transfer to " + str(transfer_name) + " is complete")
        time.sleep(.5)
        print("Your new balance is " + str(balance))
        time.sleep(.5)
        asker()
    if answer == "no":
        print("Please try again")
        
        transfer_payee()
             
def transfer_normal(transferamount, balance=b):

    
    print("What is the account number?")
    account_number = input()
    print("What is the sort code?")
    sortcode = input()                                             
    print("is the account number " + str(account_number)+ " correct")
    print("is the sort code " + str(sortcode)+ " correct")    
    answer = str(input())
    if answer == "yes":
        balance = balance - transferamount                             
    time.sleep(1)
    print("transfer to " + str(account_number) + " is complete")         
    time.sleep(.5)
    print("Your new balance is " + str(balance))                       
    time.sleep(.5)
    asker()
    if answer == "no":                                                   
         print("Please try again")
         transfer() 

def exiter():                                                     
    print("Thank you for using the bank of Python")
    time.sleep(1)
    exit()

login()

