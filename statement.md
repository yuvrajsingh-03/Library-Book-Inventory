# Project Statement: Library Book Inventory & Borrowing System

## Problem Statement
Manual tracking of library books and borrowing records often leads to missing inventory, untracked book allocations, lost records, and human error when calculating late fees. Small libraries or departmental libraries require a lightweight, reliable system to digitize cataloging and borrowing workflows.

## Scope
The Library Book Inventory & Borrowing System is a modular, terminal-based Python application. It provides catalog management (CRUD operations), handles checkout and return logic with real-time stock verification, tracks member history, and automatically calculates late penalties. All data persists locally in structured JSON files without needing external database servers.

## Target Audience
Librarians, academic department staff, and administrators managing small to medium-sized book collections looking for an easy-to-use, offline management solution.

## Core Capabilities
* **Catalog Management**: Add, search, update, and remove book entries.
* **Transaction Engine**: Validate stock availability on checkout and restore available copies on return.
* **Borrower & Fine Management**: Maintain member activity logs and automate late return fee calculations.
