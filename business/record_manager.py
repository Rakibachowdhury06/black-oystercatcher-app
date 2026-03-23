"""
CST8002 - Programming Language Research Project
Practical Project Part 3 - Project Review 2
Professor: Stanley Pieda
Due Date: See Brightspace
Student: Rakiba Chowdhury
Section: 020

This module contains the RecordManager class which handles all
business logic for managing OysterCatcherRecord objects in memory.
It provides methods to create, read, update, delete, and sort records
stored in a list.

Dataset Source:
Parks Canada. (2017). Black Oystercatcher Population - Pacific Rim.
Available at: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02
License: Open Government Licence - Canada

References:
[1] Python Software Foundation. (2024). Data Structures. docs.python.org [Online]. 
Available: https://docs.python.org/3/tutorial/datastructures.html [Accessed: Feb. 15, 2026].
[2] Python Software Foundation. (2024). Sorting HOW TO. docs.python.org [Online]. 
Available: https://docs.python.org/3/howto/sorting.html [Accessed: Mar. 20, 2026].
"""

from model.oystercatcher_record import OysterCatcherRecord
from persistence.csv_handler import load_records_from_csv, save_records_to_csv

# Path to the dataset CSV file
CSV_FILE = "pacific_rim_npr_coastalmarine_black_oystercatcher_population_nesting_counts_2008-2017_data.csv"

# Maximum number of records to load from file
RECORDS_TO_LOAD = 100

# Valid column names the user can sort by (must match OysterCatcherRecord attributes)
SORTABLE_COLUMNS = {
    "1": "visit_date",
    "2": "site_identification",
    "3": "species",
    "4": "total_black_oystercatcher_adults"
}


class RecordManager:
    """
    Manages a list of OystercatcherRecord objects in memory.

    Provides business logic methods for CRUD operations (Create, Read,
    Update, Delete) as well as loading from and saving to CSV files,
    and sorting records by a chosen column.

    Attributes:
        records (list): The in-memory list of OysterCatcherRecord objects.
    """

    def __init__(self):
        """
        Initialize RecordManager with an empty list of records.
        """
        self.records = []

    def load_data(self):
        """
        Load records from the CSV dataset file into memory.

        Replace any existing in-memory data with freshly loaded records
        from the CSV file. Loads up to RECORDS_TO_LOAD records.

        Returns:
            int: The number of records loaded.
        """
        self.records = load_records_from_csv(CSV_FILE, RECORDS_TO_LOAD)
        return len(self.records)

    def save_data(self):
        """
        Save all in-memory records to a new CSV file with a UUID filename.

        Returns:
            str: The generated filename, or None if saving failed.
        """
        return save_records_to_csv(self.records)

    def get_record(self, index):
        """
        Retrieve a single record by its index position.

        Args:
            index (int): Zero-based index of the record to retrieve.

        Returns:
            OysterCatcherRecord: The record at the given index, or None
            if the index is out of range.
        """
        if 0 <= index < len(self.records):
            return self.records[index]
        return None

    def get_all_records(self):
        """
        Retrieve all records currently stored in memory.

        Returns:
            list: The complete list of OysterCatcherRecord objects.
        """
        return self.records

    def get_record_count(self):
        """
        Get the total number of records in memory.

        Returns:
            int: Number of records stored.
        """
        return len(self.records)

    def create_record(self, visit_date, site_identification, species,
                      total_black_oystercatcher_adults):
        """
        Create a new OysterCatcherRecord and add it to the in-memory list.

        Args:
            visit_date (str): Date of observation.
            site_identification (int): Site identifier number.
            species (str): Species name.
            total_black_oystercatcher_adults (int): Count of adult birds.

        Returns:
            OysterCatcherRecord: The newly created record.
        """
        new_record = OysterCatcherRecord(
            visit_date=visit_date,
            site_identification=site_identification,
            species=species,
            total_black_oystercatcher_adults=total_black_oystercatcher_adults
        )
        self.records.append(new_record)
        return new_record

    def update_record(self, index, visit_date, site_identification, species,
                      total_black_oystercatcher_adults):
        """
        Update an existing record at the given index with new values.

        Args:
            index (int): Zero-based index of the record to update.
            visit_date (str): New date of observation.
            site_identification (int): New site identifier.
            species (str): New species name.
            total_black_oystercatcher_adults (int): New adult count.

        Returns:
            bool: True if the record was updated, False if index was invalid.
        """
        if 0 <= index < len(self.records):
            self.records[index].visit_date = visit_date
            self.records[index].site_identification = site_identification
            self.records[index].species = species
            self.records[index].total_black_oystercatcher_adults = total_black_oystercatcher_adults
            return True
        return False

    def delete_record(self, index):
        """
        Delete a record from the in-memory list at the given index.

        Args:
            index (int): Zero-based index of the record to delete.

        Returns:
            OysterCatcherRecord: The deleted record,
            or None if the index was invalid.
        """
        if 0 <= index < len(self.records):
            return self.records.pop(index)
        return None

    def sort_records(self, column_name):
        """
        Sort the in-memory records in ascending order by the specified column.

        Uses Python's built-in list.sort() with a key function to sort
        all OysterCatcherRecord objects by the given attribute name.
        Sorting is performed in-place on the records list.

        Args:
            column_name (str): The OysterCatcherRecord attribute to sort by.
                Must be one of: 'visit_date', 'site_identification',
                'species', or 'total_black_oystercatcher_adults'.

        Returns:
            bool: True if sorting was successful, False if column_name
            is not a valid attribute on OysterCatcherRecord.
        """
        if not self.records:
            return False

        # Verify the column name is a valid attribute before sorting
        if not hasattr(self.records[0], column_name):
            return False

        self.records.sort(key=lambda record: getattr(record, column_name))
        return True

    