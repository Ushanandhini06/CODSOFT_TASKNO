contacts = {}
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for name, details in contacts.items():
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])
                print("Address:", details["address"])
                print("--------------------")
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print("\nContact Found!")
            print("Name:", name)
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
            print("Address:", contacts[name]["address"])
        else:
            print("Contact not found.")
    elif choice == "4":
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            print("Contact updated successfully!")
        else:
            print("Contact not found.")
    elif choice == "5":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice. Please enter 1 to 6.")