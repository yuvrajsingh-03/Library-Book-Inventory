import json
import os
from datetime import datetime

# --- FILE PATH CONSTANTS ---
DATA_DIR = "data"
BOOKS_FILE = os.path.join(DATA_DIR, "catalog.json")
MEMBERS_FILE = os.path.join(DATA_DIR, "members.json")

# --- UTILITY & STORAGE FUNCTIONS ---
def ensure_data_folder():
    """Creates the data directory if it doesn't exist."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_json(filepath):
    """Loads JSON data from a file safely."""
    ensure_data_folder()
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_json(filepath, data):
    """Saves data to a JSON file."""
    ensure_data_folder()
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

# --- CORE SYSTEM CLASS ---
class LibrarySystem:
    def __init__(self):
        self.books = load_json(BOOKS_FILE)
        self.members = load_json(MEMBERS_FILE)

    def add_book(self):
        print("\n--- Add New Book ---")
        isbn = input("Enter ISBN: ").strip()
        
        # Check if ISBN exists
        for book in self.books:
            if book['isbn'] == isbn:
                print("Error: A book with this ISBN already exists!")
                return

        title = input("Enter Title: ").strip()
        author = input("Enter Author: ").strip()
        try:
            total_copies = int(input("Enter Total Copies: "))
            if total_copies <= 0:
                print("Copies must be greater than 0.")
                return
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return

        new_book = {
            "isbn": isbn,
            "title": title,
            "author": author,
            "total_copies": total_copies,
            "available_copies": total_copies
        }
        self.books.append(new_book)
        save_json(BOOKS_FILE, self.books)
        print(f"Book '{title}' added successfully!")

    def search_books(self):
        print("\n--- Search Catalog ---")
        query = input("Enter Title, Author, or ISBN to search: ").strip().lower()
        results = [
            b for b in self.books 
            if query in b['title'].lower() or query in b['author'].lower() or query in b['isbn'].lower()
        ]

        if not results:
            print("No matching books found.")
            return

        print("\nMatching Books:")
        for b in results:
            print(f"- [{b['isbn']}] {b['title']} by {b['author']} | Available: {b['available_copies']}/{b['total_copies']}")

    def issue_book(self):
        print("\n--- Issue Book ---")
        member_id = input("Enter Member ID: ").strip()
        isbn = input("Enter Book ISBN: ").strip()

        # Find book
        book = next((b for b in self.books if b['isbn'] == isbn), None)
        if not book:
            print("Book not found!")
            return

        if book['available_copies'] <= 0:
            print("Sorry, no copies currently available for issue!")
            return

        # Find or create member
        member = next((m for m in self.members if m['member_id'] == member_id), None)
        if not member:
            member_name = input("New Member detected! Enter Member Name: ").strip()
            member = {"member_id": member_id, "name": member_name, "borrowed_books": []}
            self.members.append(member)

        # Update records
        today_str = datetime.now().strftime("%Y-%m-%d")
        member['borrowed_books'].append({"isbn": isbn, "issue_date": today_str})
        book['available_copies'] -= 1

        save_json(BOOKS_FILE, self.books)
        save_json(MEMBERS_FILE, self.members)
        print(f"Book '{book['title']}' successfully issued to {member['name']}!")

    def return_book(self):
        print("\n--- Return Book ---")
        member_id = input("Enter Member ID: ").strip()
        isbn = input("Enter Book ISBN: ").strip()

        member = next((m for m in self.members if m['member_id'] == member_id), None)
        if not member:
            print("Member record not found!")
            return

        # Check if borrowed
        borrowed_entry = next((b for b in member['borrowed_books'] if b['isbn'] == isbn), None)
        if not borrowed_entry:
            print("This member does not have this book checked out!")
            return

        # Calculate fine ($1/day if held over 14 days)
        issue_date = datetime.strptime(borrowed_entry['issue_date'], "%Y-%m-%d")
        days_held = (datetime.now() - issue_date).days
        overdue_days = max(0, days_held - 14)
        fine = overdue_days * 1.0

        # Update records
        member['borrowed_books'].remove(borrowed_entry)
        book = next((b for b in self.books if b['isbn'] == isbn), None)
        if book:
            book['available_copies'] += 1

        save_json(BOOKS_FILE, self.books)
        save_json(MEMBERS_FILE, self.members)

        print(f"Book successfully returned! Days held: {days_held}.")
        if fine > 0:
            print(f"OVERDUE FINE: ${fine:.2f} ({overdue_days} days overdue)")
        else:
            print("No late fees accrued.")

    def view_member_history(self):
        print("\n--- Member History ---")
        member_id = input("Enter Member ID: ").strip()
        member = next((m for m in self.members if m['member_id'] == member_id), None)

        if not member:
            print("Member not found!")
            return

        print(f"\nMember: {member['name']} (ID: {member['member_id']})")
        if not member['borrowed_books']:
            print("No books currently checked out.")
        else:
            print("Currently Borrowed Books:")
            for b in member['borrowed_books']:
                print(f"- ISBN: {b['isbn']} | Date Issued: {b['issue_date']}")

# --- CLI MENU LOOP ---
def main():
    system = LibrarySystem()

    while True:
        print("\n=================================")
        print(" Library Management System (CLI) ")
        print("=================================")
        print("1. Add New Book")
        print("2. Search Catalog")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Member History")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            system.add_book()
        elif choice == "2":
            system.search_books()
        elif choice == "3":
            system.issue_book()
        elif choice == "4":
            system.return_book()
        elif choice == "5":
            system.view_member_history()
        elif choice == "6":
            print("\nExiting System. All data saved automatically. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
