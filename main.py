
from contact_operations import add_contact,view_contact,remove_contact,search_contact
def main():
    while True:
        print("\n ----Contact Book Manage System----")
        print("1. Add a Contact")
        print("2.View All Contact")
        print("3. Remove a Contact")
        print("4. Search a Contact")
        print("0. Exit")
        choice = input ("Enter your choice: ").strip()


        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            remove_contact()   
        elif choice == "4":
            search_contact() 
        elif choice == "0":
            print("\n Exiting the program. Goodbye!")
            break
        else:
            print("\n Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
