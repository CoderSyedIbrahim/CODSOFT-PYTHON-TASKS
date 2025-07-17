contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print(f"\nName: {name}")
            for key, value in details.items():
                print(f"{key}: {value}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Details for {name}:")
        for key, value in contacts[name].items():
            print(f"{key}: {value}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        print("Leave blank to keep current value.")
        phone = input(f"New Phone ({contacts[name]['Phone']}): ") or contacts[name]['Phone']
        email = input(f"New Email ({contacts[name]['Email']}): ") or contacts[name]['Email']
        address = input(f"New Address ({contacts[name]['Address']}): ") or contacts[name]['Address']
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid option.")
