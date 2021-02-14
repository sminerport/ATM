import re
import sqlite3
from itertools import chain

def start_menu():
    print()
    print("Welcome to the ATM Application.")
    print("Please choose from the choices below.")
    print()
    print("***********************************")
    print("*                                             ")
    print("*   [1] Register New User        ")
    print("*   [2] Log in                            ")
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
    email = input("Enter your email (0 to exit): ")
    if email == '0':
        return
    while not (valid_email(email)):
        print()
        print("Email must be valid.")
        print()
        email = input("Enter your email (0 to exit): ")
        if email == '0':
            return
    if user_available(email):
        print()
        print("Username is available.")
        pin = get_pin()
        if (pin == 0):
            return
        print()
        insert_user_and_pin(email, pin)
        print("**********************************************")
        print("*           New Customer Added             *")
        print("**********************************************")
    else:
        print()
        print("User already exists.")
        print("Please choose a new username or log in.")
        
def insert_user_and_pin(email, pin):
    db = sqlite3.connect('customer.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO customers (user_name, pin) VALUES (?, ?)", (email.lower(), pin))
    db.commit()
    db.close()
    
def valid_email(email):
    regex = '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex,email):
        return True
    else:
        return False
    
def user_available(email):
        db = sqlite3.connect('customer.db')
        cursor = db.cursor()
        cursor.execute("SELECT count(*) FROM customers WHERE user_name =?", (email.lower(),))
        data=cursor.fetchone()[0]
        if data==0:
            return True
        else:
            return False
        db.close()

def get_pin():
        while (True):
            print()
            pinString = input("Enter your 4-digit pin number (0 to exit): ")
            try:
                pin = int(pinString)
                if (pin == 0):
                    break;
                if len(pinString) < 4 or len(pinString) > 4:
                    print()
                    print("Pin must contain four digits.")
                elif len(pinString) == 4:
                    break;
            except ValueError:
                print()
                print("Pin numbers can only contain digits.")
        return pin
        
def log_in():
    print()
    print("**********************************************")
    print("*                  Log in Screen                   *")
    print("**********************************************")
    print()
    email = None
    email = input("Enter your email (0 to exit): ")
    if (email == '0'):
        return
    while not (valid_email(email)):
        print()
        print("Email must be valid.")
        print()
        email = input("Enter your email (0 to exit): ")
        if (email == '0'):
            return
    pin = get_pin()
    if (pin == 0):
        return
    while not (correct_pin(email, pin)):
        print()
        print("Pin does not match pin on file.")
        print("Please try again.")
        pin = get_pin()
        if (pin == 0):
            return
    print()
    get_acct_user_choice()
    return

def correct_pin(email, input_pin):
    db = sqlite3.connect('customer.db')
    cursor = db.cursor()
    result = cursor.execute("SELECT pin FROM customers WHERE user_name =?", (email.lower(),))
    try:
        db_pin = next(result)
        if db_pin[0] == input_pin:
            db.close()
            return True
        else:
            db.close()
            return False
    except StopIteration as e:
        db.close()
        return False
    
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
                print("Returning to the main menu...")
                return;
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
                log_in()
            else:
                print()
                print("Invalid option.")
        #if user does not input a number, this error is thrown      
        except ValueError:
            print()
            print("Input must be a number.")
            
def create_customers_table():
    db = sqlite3.connect('customer.db')
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE if not exists customers (
        id INTEGER PRIMARY KEY, user_name text, pin int
        )
    """)
    db.commit()
    
def main():
    create_customers_table()
    get_init_user_choice()

if __name__ == "__main__": main()