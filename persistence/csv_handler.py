"""
CST8002 - Programming Language Research Project
Practical Project Part 4 - Project Release
Professor: Stanley Pieda
Due Date: April 12, 2026
Student: Rakiba Chowdhury
Section: 020

This module handles all file input/output operations for reading
and writing CSV data. It uses the uuid library to generate unique
file names when saving data.

Dataset Source:
Parks Canada. (2017). Black Oystercatcher Population - Pacific Rim.
Available at: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02
License: Open Government Licence - Canada

References:
[1] Python Software Foundation. (2024). csv - CSV File Reading and Writing. docs.python.org [Online]. 
Available: https://docs.python.org/3/library/csv.html [Accessed: Feb. 15, 2026].
[2] Python Software Foundation. (2024). uuid - UUID objects according to RFC 4122. docs.python.org [Online]. 
Available: https://docs.python.org/3/library/uuid.html [Accessed: Feb. 15, 2026].
"""

import csv
import uuid
from model.oystercatcher_record import OysterCatcherRecord

# Column headers matching the dataset
COLUMN_HEADERS = [
    "Visit date",
    "Site identification",
    "Species",
    "Total Black oystercatcher adults"
]

def load_records_from_csv(filename, limit=100):
    """
    Read records from a CSV file and return a list of OysterCatcherRecord objects.

    Opens the CSV file, skips the French translation row (row 2),
    and parses up to the specified number of records.

    Args:
        filename (str): Path to the CSV file to read.
        limit (int): Maximum number of records to load (default 100).

    Returns:
        list: A list of OysterCatcherRecord objects parsed from the file.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        PermissionError: If the file cannot be accessed.
    """

    records = []

    try:
        with open(filename, mode="r", encoding="latin-1", newline="") as file:
            reader = csv.DictReader(file)

            for i, row in enumerate(reader):
                # Skip the French translation row
                if i == 0 and "Date de la visite" in row.get("Visit date", ""):
                    continue

                if len(records) >= limit:
                    break

                try:
                   record = OysterCatcherRecord.from_row(row)
                   records.append(record)
                except (ValueError, KeyError) as row_error:
                    print(f"Skipping row {i + 1}: {row_error}")

    except FileNotFoundError:
        print(f" ERROR: Could not find the file: {filename}")
    except PermissionError:
        print(f" ERROR: Permission denied: {filename}")
    except Exception as e:
        print(f" ERROR: Unexpected problem reading file: {e}")
    return records

def save_records_to_csv(records):
    """
    Save a list of OysterCatcherRecord objects to a new CSV file.

    Generates a unique file name using UUID (uuid4) and writes
    all records in the list to the file in CSV format.

    Args:
        records (list): List of OysterCatcherRecord objects to save.

    Returns:
        str: The generated file name, or None if saving failed.
    """
    # Generate unique file name using UUID
    unique_id = uuid.uuid4()
    filename = f"{unique_id}.csv"

    try:
        with open(filename, mode="w", encoding="latin-1", newline="") as file:
            writer = csv.writer(file)

            # Write header row
            writer.writerow(COLUMN_HEADERS)

            # Write each record
            for record in records:
                writer.writerow(record.to_list())

        return filename

    except PermissionError:
        print(f"  ERROR: Permission denied when writing: {filename}")
        return None
    except Exception as e:
        print(f"  ERROR: Could not save file: {e}")
        return None