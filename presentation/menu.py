"""
CST8002 - Programming Language Research Project
Practical Project Part 2 - Project Review I
Professor: Stanley Pieda
Due Date: See Brightspace
Student: Rakiba Chowdhury
Section: 020

This module contains the Menu class which handles all user interaction
for the program. It displays options, collects input, and calls the
appropriate business layer methods.

Dataset Source:
Parks Canada. (2017). Black Oystercatcher Population - Pacific Rim.
Available at: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02
License: Open Government Licence - Canada

References:
[1] Python Software Foundation, "Built-in Functions," Python 3.12 Documentation.
    [Online]. Available: https://docs.python.org/3/library/functions.html
    [Accessed Feb. 15, 2026]
"""

from business.record_manager import RecordManager

# Student name constant displayed throughout the program
STUDENT_NAME = "Rakiba Chowdhury"


class Menu:
    """
    Handles the user interface for the Black Oystercatcher data program.

    Displays a menu of options and processes user choices by calling
    the appropriate methods on the RecordManager (business layer).

    Attributes:
        manager (RecordManager): The business layer object managing records.
    """

    def __init__(self):
        """
        Initialize the Menu with a RecordManager instance.
        """
        self.manager = RecordManager()

    def display_header(self):
        """
        Display the program header with student name.
        """
        print("=" * 60)
        print(f"  Program by: {STUDENT_NAME}")
        print("  CST8002 Practical Project - Part 2")
        print("=" * 60)

    def display_menu(self):
        """
        Display the main menu options to the user.
        """
        print(f"\n--- Menu (Program by {STUDENT_NAME}) ---")
        print("  1. Reload data from dataset")
        print("  2. Save data to a new CSV file")
        print("  3. Display one record")
        print("  4. Display all records")
        print("  5. Create a new record")
        print("  6. Edit a record")
        print("  7. Delete a record")
        print("  8. Exit")

    def run(self):
        """
        Run the main program loop.

        Displays the header, loads data on startup, then enters a loop
        that shows the menu and processes user choices until exit.
        """
        self.display_header()

        # Load data on startup
        print("\nLoading data from CSV file...")
        count = self.manager.load_data()
        print(f"  Loaded {count} record(s) into memory.")

        # Main menu loop
        while True:
            self.display_menu()

            choice = input("\nEnter your choice (1-8): ").strip()

            if choice == "1":
                self.reload_data()
            elif choice == "2":
                self.save_data()
            elif choice == "3":
                self.display_one_record()
            elif choice == "4":
                self.display_all_records()
            elif choice == "5":
                self.create_record()
            elif choice == "6":
                self.edit_record()
            elif choice == "7":
                self.delete_record()
            elif choice == "8":
                print(f"\nGoodbye! (Program by {STUDENT_NAME})")
                break
            else:
                print("  Invalid choice. Please enter a number from 1 to 8.")

    def reload_data(self):
        """
        Reload all data from the CSV file, replacing in-memory data.
        """
        print(f"\n--- Reload Data (Program by {STUDENT_NAME}) ---")
        count = self.manager.load_data()
        print(f"  Reloaded {count} record(s) from the dataset.")

    def save_data(self):
        """
        Save all in-memory records to a new CSV file using UUID filename.
        """
        print(f"\n--- Save Data (Program by {STUDENT_NAME}) ---")
        filename = self.manager.save_data()
        if filename:
            print(f"  Data saved successfully to: {filename}")
            print(f"  Total records saved: {self.manager.get_record_count()}")
        else:
            print("  Failed to save data.")

    def display_one_record(self):
        """
        Display a single record selected by index number.
        """
        print(f"\n--- Display One Record (Program by {STUDENT_NAME}) ---")
        total = self.manager.get_record_count()

        if total == 0:
            print("  No records in memory.")
            return

        print(f"  Enter a record number (1 to {total}):")
        try:
            index = int(input("  > ")) - 1
            record = self.manager.get_record(index)
            if record:
                print(f"\n  Record #{index + 1}: {record}")
            else:
                print(f"  Invalid record number. Must be between 1 and {total}.")
        except ValueError:
            print("  Please enter a valid number.")

    def display_all_records(self):
        """
        Display all records currently stored in memory.

        Shows the student name every 10 records for visibility.
        """
        print(f"\n--- Display All Records (Program by {STUDENT_NAME}) ---")
        records = self.manager.get_all_records()

        if len(records) == 0:
            print("  No records in memory.")
            return

        for i, record in enumerate(records):
            print(f"  [{i + 1}] {record}")

            # Show student name every 10 records
            if (i + 1) % 10 == 0:
                print(f"      --- Program by {STUDENT_NAME} ---")

        print(f"\n  Total records displayed: {len(records)}")

    def create_record(self):
        """
        Create a new record by collecting user input for each field.
        """
        print(f"\n--- Create New Record (Program by {STUDENT_NAME}) ---")
        try:
            visit_date = input("  Enter Visit date (DD/MM/YYYY): ").strip()
            site_identification = int(input("  Enter Site identification (number): ").strip())
            species = input("  Enter Species: ").strip()
            total_black_oystercatcher_adults = int(
                input("  Enter Total Black oystercatcher adults (number): ").strip()
            )

            new_record = self.manager.create_record(
                visit_date, site_identification, species,
                total_black_oystercatcher_adults
            )
            print(f"\n  Record created successfully: {new_record}")
            print(f"  Total records now: {self.manager.get_record_count()}")

        except ValueError:
            print("  Error: Site identification and adult count must be numbers.")

    def edit_record(self):
        """
        Edit an existing record by selecting it by index and entering new values.
        """
        print(f"\n--- Edit Record (Program by {STUDENT_NAME}) ---")
        total = self.manager.get_record_count()

        if total == 0:
            print("  No records in memory.")
            return

        try:
            print(f"  Enter the record number to edit (1 to {total}):")
            index = int(input("  > ")) - 1

            record = self.manager.get_record(index)
            if record is None:
                print(f"  Invalid record number. Must be between 1 and {total}.")
                return

            print(f"\n  Current record: {record}")
            print("  Enter new values (press Enter to keep current value):\n")

            visit_date = input(f"  Visit date [{record.visit_date}]: ").strip()
            if not visit_date:
                visit_date = record.visit_date

            site_input = input(f"  Site identification [{record.site_identification}]: ").strip()
            if site_input:
                site_identification = int(site_input)
            else:
                site_identification = record.site_identification

            species = input(f"  Species [{record.species}]: ").strip()
            if not species:
                species = record.species

            adults_input = input(
                f"  Total Black oystercatcher adults [{record.total_black_oystercatcher_adults}]: "
            ).strip()
            if adults_input:
                total_black_oystercatcher_adults = int(adults_input)
            else:
                total_black_oystercatcher_adults = record.total_black_oystercatcher_adults

            success = self.manager.update_record(
                index, visit_date, site_identification, species,
                total_black_oystercatcher_adults
            )
            if success:
                print(f"\n  Record #{index + 1} updated: {self.manager.get_record(index)}")
            else:
                print("  Failed to update record.")

        except ValueError:
            print("  Error: Site identification and adult count must be numbers.")

    def delete_record(self):
        """
        Delete a record by selecting it by index number.
        """
        print(f"\n--- Delete Record (Program by {STUDENT_NAME}) ---")
        total = self.manager.get_record_count()

        if total == 0:
            print("  No records in memory.")
            return

        try:
            print(f"  Enter the record number to delete (1 to {total}):")
            index = int(input("  > ")) - 1

            record = self.manager.get_record(index)
            if record is None:
                print(f"  Invalid record number. Must be between 1 and {total}.")
                return

            print(f"  Record to delete: {record}")
            confirm = input("  Are you sure? (y/n): ").strip().lower()

            if confirm == "y":
                deleted = self.manager.delete_record(index)
                print(f"\n  Deleted: {deleted}")
                print(f"  Total records now: {self.manager.get_record_count()}")
            else:
                print("  Delete cancelled.")

        except ValueError:
            print("  Please enter a valid number.")