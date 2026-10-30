
contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added successfully")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Phone number:", contacts[name])
    else:
        print("Contact not found")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        contacts[name] = phone
        print("Contact updated")
    else:
        print("Contact not found")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted")
    else:
        print("Contact not found")

def view_contacts():
    if contacts:
        for name, phone in contacts.items():
            print(name, ":", phone)
    else:
        print("No contacts available")

def show_menu():
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View Contacts")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            view_contacts()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice")

main()
