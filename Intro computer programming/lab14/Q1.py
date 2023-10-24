import pickle
from tkinter import filedialog
import os

phonebook = {}

def add_contact():
    try:
        name = input("Enter name: ")
        number = input("Enter phone number: ")

        if not name.isalpha() or not name.strip():
            raise ValueError("Invalid name. Please enter a valid name.")
        elif name == "nigga" :
            raise ValueError("Explicit name detected bruh. Contact not saved.")
        if not number.isdigit() or not number.strip():
            raise ValueError("Invalid phone number. Please enter a valid phone number.")

        phonebook[name] = number
        print("Contact added successfully.")

    except ValueError as e:
        print(e)

def delete_contact():
    name = input("Enter name: ")
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def find_contact():
    name = input("Enter name: ")
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print("Contact not found.")


def save_contacts():
    try:
        filename = filedialog.asksaveasfilename(
            title="Select a file to save contacts",
            filetypes=(("Pickle files", "*.pkl"),)
        )

        if not filename:
            print("No file selected. Contacts not saved.")
            return

        if os.path.exists(filename):
            overwrite = input("The file already exists. Do you want to overwrite it? (y/n): ")
            if overwrite.lower() != 'y':
                print("Contacts not saved.")
                return

        with open(filename, "wb") as f:
            pickle.dump(phonebook, f)
        print("Contacts saved successfully.")
    
    except Exception as e:
        print("Error saving contacts:", str(e))

def load_contacts():
    global phonebook
    filename = filedialog.askopenfilename(title="Select a file to load contacts", filetypes=(("Pickle files", "*.pkl"),))
    
    if not filename:
        print("No file selected. Contacts not loaded.")
        return

    if os.path.exists(filename):
        overwrite = input("Loading new contacts will overwrite your existing contacts. Do you want to continue? (y/n): ")
        if overwrite.lower() != 'y':
            print("Contacts not loaded.")
            return

    try:
        with open(filename, "rb") as f:
            phonebook = pickle.load(f)
        print("Contacts loaded successfully.")
    except Exception as e:
        print("Error loading contacts:", str(e))
    

def print_contacts():
    for name, number in phonebook.items():
        print(f"{name}: {number}")

def main():
    while True:
        print("Phonebook Manager")
        print("Press \"+\" to add a new contact.")
        print("Press \"-\" to delete a contact.")
        print("Press \"f\" to find a contact.")
        print("Press \"s\" to save all contacts to a file.")
        print("Press \"l\" to load previous saved contacts from a file.")
        print("Press \"p\" to print out all contacts in the phonebook.")
        print("Press \"q\" to quit the program.")
        choice = input("Enter your choice: ")
        if choice == "+":
            add_contact()
        elif choice == "-":
            delete_contact()
        elif choice == "f":
            find_contact()
        elif choice == "s":
            save_contacts()
        elif choice == "l":
            load_contacts()
        elif choice == "p":
            print_contacts()
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
