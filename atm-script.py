import re
import sqlite3

# print the user menu
def menu():
    print("[1] Register New User")
    print("[2] Login")
    print("[0] Exit the program.")

def option_1():
    email = input("Enter your email: ")
    while not (valid_email(email)):
        print("Email must be valid.")
        email = input("Enter your email: ")
    
    if user_available(email):
        print("Username is available.")
        pin = get_pin()
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
            pinString = input("Enter your 4-digit pin number: ")
            try:
                pin = int(pinString)
                if len(pinString) < 4 or len(pinString) > 4:
                    print("Pin must contain four digits.")
                elif len(pinString) == 4:
                    break;
            except ValueError:
                print("Pin numbers can only contain digits.")
        return pin
        
def option_2():
    print()
    email = input("Enter your login name: ")
    while not (valid_email(email)):
        print("Email must be valid.")
        email = input("Enter your email: ")
    pin = get_pin()
    while not (correct_pin(email, pin)):
        print("Pin does not match pin on file.")
        print("Please try again.")
        pin = get_pin()
    else:
        print("Welcome to your account.")
    
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
        
def main():
    
    #display menu
    menu()
    #prompt for user choice
    try:
        print()
        option = int(input("Enter your option: "))
    
        while option != 0:
            if option == 1:
                option_1()
            elif option == 2:
                option_2()
            else:
                print("Invalid option.") 
            print()
            menu()
            option = int(input("Enter your option: "))
    except ValueError:
        print()
        print("Input must be a number.")
        menu()
        option = int(input("Enter your option: "))
        
    print("Thanks for using this program!  Goodbye!")
    
    pin = GetPin()

if __name__ == "__main__": main()