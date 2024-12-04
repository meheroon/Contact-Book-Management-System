#import json
import os
import csv

SAVE_CONTACT = "contact.csv"





def main():
    while True:
        print("\n ----Contact Book Manage System----")
        print("1. Add a Contact")
        print("2.View All Contact")
        print("3. Remove a Contact")
        print("0. Exit")
        choice = input ("Enter your choice: ").strip()


        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            remove_contact()    
        elif choice == "0":
            print("\n Exiting the program. Goodbye!")
            break
        else:
            print("\n Invalid choice. Please try again.")

            

# Load contacts from file
def load_contacts():
    contacts= []
    if os.path.exists( SAVE_CONTACT ):
        with open(SAVE_CONTACT, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)
    return contacts
        
    

#save contact to file
def save_contacts(contacts):
    with open(SAVE_CONTACT, "w", encoding="utf-8", newline='') as file:
        filednames = ["name", "email", "phone", "address"]
        writer = csv.DictWriter(file, fieldnames=filednames)
        writer.writeheader()
        writer.writerows(contacts)


#add a contact
def add_contact():
    print("\n ----Add a New Contact---")
    name = input("Enter the name: ").strip()
    email = input("Enter the email: ").strip()
    phone = input("Enter the phone number: ").strip()
    address = input("Enter the address: ").strip()

    contacts = load_contacts()
    # Check for duplicate phone numbers
    if any(contact["phone"] == phone for contact in contacts):
        print("\nError: This phone number already exists.")
        return

    contact = {
        "name" : name,
        "email" : email,
        "phone" : phone,
        "address" : address,
    }

    #contact = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)


    print(f"\nContact '{name} ' added successfully!\n")

 #view contacts
def view_contact():
    print("\n -----Contact Details------")
    contacts = load_contacts()
    if not contacts:
        print("No Contacts Found.")   
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"\nContact {idx}:")
            print(f" Name: {contact['name']}")
            print(f" Email: {contact['email']}")
            print(f" Phone: {contact['phone']}")
            print(f" Address: {contact['address']}")
 
 #remove a contact
def remove_contact():
    print("\n--------Remove a Contact-------")
    phone = input("Enter the phone number of the contact to remove:").strip()
    contacts = load_contacts()
    updated_contacts = [contact for contact in contacts if contact["phone"] != phone ]
    if len(contacts) == len(updated_contacts):
        print("\nError : No contact found with the provided phone number.")
    else:
        save_contacts(updated_contacts)
        print("\nContact removed successfully!")    

if __name__ == "__main__":
    main()

        