import sys
import os

# Add parent directory to Python path (Fix for VS Code Run Button)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import logging
from library_manager.inventory import LibraryInventory

logging.basicConfig(level=logging.INFO)

def menu():
    print("\n===== Library Inventory Manager =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def main():
    inventory = LibraryInventory()

    while True:
        menu()
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                t = input("Title: ")
                a = input("Author: ")
                i = input("ISBN: ")
                inventory.add_book(t, a, i)
                print("Book added.")

            elif choice == "2":
                i = input("Enter ISBN: ")
                inventory.issue_book(i)
                print("Book issued.")

            elif choice == "3":
                i = input("Enter ISBN: ")
                inventory.return_book(i)
                print("Book returned.")

            elif choice == "4":
                for b in inventory.display_all():
                    print(b)

            elif choice == "5":
                s = input("Search by title or ISBN: ").lower()
                if s == "title":
                    t = input("Enter title: ")
                    for b in inventory.search_by_title(t):
                        print(b)
                else:
                    i = input("Enter ISBN: ")
                    print(inventory.search_by_isbn(i) or "Not found")

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid option")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
