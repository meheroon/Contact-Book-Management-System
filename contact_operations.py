from file_operations import load_contacts, save_contacts


    
#add a contact
def add_contact():
    print("\n ----Add a New Contact---")
    name = input("Enter the name: ").strip()
    while not name.replace("","").isalpha():
        name = input("Invalid input. Enter a valid name: ").strip()
    email = input("Enter the email: ").strip()
    while not ("@" in email and "." in email):  # Basic validation for email format
        email = input("Invalid input. Enter a valid email: ").strip()
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

def search_contact():
    print("/n-------Search a Contact------------")
    search_query = input("Enter name to search:").strip().lower()
    contacts = load_contacts()
    matching_contacts = [
        contact for contact in contacts
        if search_query in contact["name"].lower()
        or search_query in contact["email"].lower() 
        or search_query in contact["phone"]
    ]
    if not matching_contacts:
        print("\nNo matching contacts found.")
    else:
        print("\nMatching Contacts:")
        for idx, contact in enumerate(matching_contacts, start=1):
            print(f"\nContact {idx}:")
            print(f"\nName: {contact['name']}")
            print(f" Email: {contact['email']}")
            print(f" Phone: {contact['phone']}")
            print(f" Address: {contact['address']}")
            


        