def GetPin():
    print()
    
    while True:
        count = 0
        pin = input("Please enter your pin: ")
        try:
            pin_int = int(pin)
            if len(pin) < 4:
                print("\nPin must contain at least four digits.")
            elif len(pin > 4):
                print("\nPin can only contain four digits.")
            else:
                print("\nPin must contain four digits.\n")
                count += 1
        except ValueError:
            print("\nYou must enter a number containing four digits to access your account.\n")
    
    return pin_int

def menu():
    print("[1] Register New User")
    print("[2] Login")
    print("[0] Exit the program.")

def main():
    menu()
    try:
        option = int(input("Enter your option: "))
    
        while option != 0:
            if option == 1:
                #do option 1 stuff
                print("Option 1 has been called.")
            elif option == 2:
                #do option 2 stuff
                print("Option 2 has been called.")
            else:
                print("Invalid option.") 
            print()
            menu()
            option = int(input("Enter your option: "))
    except ValueError:
        print("\nInput must be a number.\n")
        menu()
        option = int(input("Enter your option: "))
        
    print("Thanks for using this program!  Goodbye!")
    
    pin = GetPin()

if __name__ == "__main__": main()