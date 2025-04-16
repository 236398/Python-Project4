def phonebook():
    contacts = {}  
    
    print("Phonebook Application")
    print("---------------------")
    
    while True:
        print("\nOptions:")
        print("1. Add a contact")
        print("2. Look up a contact")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Display all contacts")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print(f"Added {name} to the phonebook.")
            
        elif choice == "2":
            name = input("Enter name to look up: ")
            if name in contacts:
                print(f"{name}'s phone number is {contacts[name]}")
            else:
                print(f"{name} not found in the phonebook.")
                
        elif choice == "3":
            name = input("Enter name to update: ")
            if name in contacts:
                phone = input("Enter new phone number: ")
                contacts[name] = phone
                print(f"Updated {name}'s phone number.")
            else:
                print(f"{name} not found in the phonebook.")
                
        elif choice == "4":
            name = input("Enter name to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Deleted {name} from the phonebook.")
            else:
                print(f"{name} not found in the phonebook.")
                
        elif choice == "5":
            if contacts:
                print("\nPhonebook Contacts:")
                print("------------------")
                for name, phone in sorted(contacts.items()):
                    print(f"{name}: {phone}")
            else:
                print("Phonebook is empty.")
                
        elif choice == "6":
            print("Thank you for using the phonebook application!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    phonebook()
