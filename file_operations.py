
import os
import csv

SAVE_CONTACT = "contact.csv"

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

 