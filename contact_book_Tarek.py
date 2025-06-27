import csv
import os

CONTACTS_FILE = 'contacts.csv'

def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, mode='w', newline='') as file:
        fieldnames = ['Name', 'Phone', 'Email', 'Address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

def add_contact(contacts):
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        if not phone.isdigit():
            raise ValueError("Phone number must be numeric.")
        for c in contacts:
            if c['Phone'] == phone:
                print("Error: Phone number already exists for another contact.")
                return
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        save_contacts(contacts)
        print("Contact added successfully!")
    except ValueError as ve:
        print("Error:", ve)

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("===== All Contacts =====")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. Name : {contact['Name']}\n   Phone : {contact['Phone']}\n   Email : {contact['Email']}\n   Address: {contact['Address']}")
    print("========================")

def search_contact(contacts):
    term = input("Enter search term (name/email/phone): ").lower()
    results = [c for c in contacts if term in c['Name'].lower() or term in c['Email'].lower() or term in c['Phone']]
    if results:
        print("Search Result:")
        for contact in results:
            print(f"Name : {contact['Name']}\nPhone : {contact['Phone']}\nEmail : {contact['Email']}\nAddress: {contact['Address']}\n")
    else:
        print("No contact found with that term.")

def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to delete: ")
    for contact in contacts:
        if contact['Phone'] == phone:
            confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.remove(contact)
                save_contacts(contacts)
                print("Contact deleted successfully!")
                return
            else:
                print("Delete operation cancelled.")
                return
    print("Contact not found.")

def menu():
    contacts = load_contacts()
    print("Welcome to the Contact Book CLI System!")
    print("Loading contacts from contacts.csv... Done!")
    while True:
        print("\n=========== MENU ===========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        print("============================")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            remove_contact(contacts)
        elif choice == '5':
            print("Thank you for using the Contact Book CLI System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    menu()
