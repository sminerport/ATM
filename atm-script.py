import re
import sqlite3

def start_menu():
    print()
    print("Welcome to the ATM Application.")
    print("Please choose from the choices below.")
    print()
    print("***********************************")
    print("*                                             ")
    print("*   [1] Register New User        ")
    print("*   [2] Login                             ")
    print("*   [0] Exit the program            ")
    print("*                                             ")
    print("***********************************")
    print()

def register_user():
    print()
    print("**********************************************")
    print("*           Registering a new user            *")
    print("**********************************************")
    
    print()
    email = input("Enter your email: ")
    while not (valid_email(email)):
        print()
        print("Email must be valid.")
        print()
        email = input("Enter your email: ")
    
    if user_available(email):
        print()
        print("Username is available.")
        pin = get_pin()
        print()
        print("Thank you for entering a valid pin number.")
        insert_user_and_pin(email, pin)
        print("New customer added.")
    else:
        print()
        print("User already exists.")
        print("Please choose a new username or login.")
        
def insert_user_and_pin(email, pin):
    db = sqlite3.connect('customer.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO customers (user_name, pin) VALUES (?, ?)", (email, pin))
    db.commit()
    db.close()
    
def valid_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex,email):
        return True
    else:
        return False
    
def user_available(email):
        db = sqlite3.connect('customer.db')
        cursor = db.cursor()
        cursor.execute("SELECT count(*) FROM customers WHERE user_name =?", (email,))
        data=cursor.fetchone()[0]
        if data==0:
            return True
        else:
            return False
        db.close()

def get_pin():
        while (True):
            print()
            pinString = input("Enter your 4-digit pin number: ")
            try:
                pin = int(pinString)
                if len(pinString) < 4 or len(pinString) > 4:
                    print()
                    print("Pin must contain four digits.")
                elif len(pinString) == 4:
                    break;
            except ValueError:
                print()
                print("Pin numbers can only contain digits.")
        return pin
        
def login():
    print()
    print("**********************************************")
    print("*                  Login Screen                    *")
    print("**********************************************")
    print()
    email = input("Enter your login name: ")
    while not (valid_email(email)):
        print()
        print("Email must be valid.")
        print()
        email = input("Enter your email: ")
    pin = get_pin()
    while not (correct_pin(email, pin)):
        print()
        print("Pin does not match pin on file.")
        print("Please try again.")
        pin = get_pin()
    print()
    get_acct_user_choice()

def correct_pin(email, input_pin):
    db = sqlite3.connect('customer.db')
    cursor = db.cursor()
    cursor.execute("SELECT pin FROM customers WHERE user_name =?", (email,))
    db_pin=cursor.fetchone()[0]
    if db_pin == input_pin:
        return True
    else:
        return False
    db.close()
    
def user_menu():
    print("**********************************************")
    print("*        Welcome to your account           *")
    print("**********************************************")
    print()
    print("***************************************")
    print("*                                                   ")
    print("*   [1] Check Account Balance      ")
    print("*   [2] Withdrawal Money              ")
    print("*   [3] Transfer Money                  ")
    print("*   [4] Make a Deposit                   ")
    print("*   [0] Sign-out                              ")
    print("*                                                   ")
    print("***************************************")
    print()
    
def get_acct_user_choice():
    option = None
    while option != 0:
        #try to convert user input to a number
        try:
            user_menu()
            option = int(input("Enter your option: "))
            if option == 0:
                print()
                print("Thanks for using this program! Goodbye!")
                break;
            elif option == 1:
                #todo check acct balance
                pass
            elif option == 2:
                #todo withdrawal money
                pass
            elif option == 3:
                #todo transfer funds
                pass
            elif option == 4:
                #todo deposit money
                pass
            else:
                print()
                print("Invalid option.")
        #if user does not input a number, this error is thrown      
        except ValueError:
            print()
            print("Input must be a number.")

def get_init_user_choice():
    option = None
    while option != 0:
        #try to convert user input to a number
        try:
            start_menu()
            option = int(input("Enter your option: "))
            if option == 0:
                print()
                print("Thanks for using this program! Goodbye!")
                break;
            elif option == 1:
                register_user()
            elif option == 2:
                login()
            else:
                print()
                print("Invalid option.")
        #if user does not input a number, this error is thrown      
        except ValueError:
            print()
            print("Input must be a number.")
    
def main():
    get_init_user_choice()

if __name__ == "__main__": main()