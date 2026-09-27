# Library-Book-Inventory
A modular Python CLI app to manage book inventory, track borrowings, and calculate overdue fines using JSON storage

## Features

### 1. Book Inventory Management (CRUD)
* **Add New Books**: Register books with details including ISBN, title, author, and available copy count.
* **Catalog Search & Retrieval**: Search the library catalog instantly by ISBN, title, or author name.
* **Update & Delete Entries**: Modify book details or remove outdated records from the system.

### 2. Check-Out & Return Engine
* **Issue Books**: Process book check-outs while automatically verifying copy availability.
* **Process Returns**: Handle returned items and automatically restore the available stock count.
* **Stock Tracking**: Prevent over-borrowing by enforcing real-time copy limits.

### 3. Borrower & Fine Management
* **Member History**: Maintain records of member details and their actively borrowed books.
* **Overdue Fine Calculation**: Automatically calculate late return penalties based on overdue days.
* **Local Data Persistence**: Save all inventory and transaction records to JSON files without requiring external databases.

## 4. Technologies & Tools Used
* **Language**: Python 3.x
* **Storage**: Local JSON files (no external database server needed)
* **Testing**: Python `unittest` library
* **Version Control**: Git & GitHub

## 5. Installation & Setup
1. **Clone the repository**:
   ```bash
   (https://github.com/Swetank-020508/-library-book-inventory.git)
   cd library-book-inventory
