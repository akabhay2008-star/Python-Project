from library_manager.book import Book
from library_manager.inventory import LibraryInventory

def show_menu():
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
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            if inventory.issue_book(isbn):
                print("Book issued!")
            else:
                print("Book not available or not found.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            if inventory.return_book(isbn):
                print("Book returned!")
            else:
                print("Book not found or already available.")

        elif choice == "4":
            books = inventory.display_all()
            if not books:
                print("Catalog is empty.")
            else:
                for b in books:
                    print(b)

        elif choice == "5":
            title = input("Enter title keyword: ")
            results = inventory.search_by_title(title)
            if results:
                for b in results:
                    print(b)
            else:
                print("No books found.")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
