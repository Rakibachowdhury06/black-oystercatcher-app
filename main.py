"""
CST8002 - Programming Language Research Project
Practical Project Part 1 - Proof of Concept
Professor: Stanley Pieda
Due Date: February 1, 2026
Student: Rakiba Chowdhury
Section: 020

Dataset Source:
Parks Canada. (2017). Black Oystercatcher Population – Pacific Rim.
Available at: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02
License: Open Government Licence – Canada

This program loads data from a CSV file and displays 
it using custom Record objects stored in a list.

References:
[1] Python Software Foundation. (n.d.). csv — CSV File Reading and Writing. 
    docs.python.org. [Online]. Available at: 
    https://docs.python.org/3/library/csv.html 
    [Accessed on: January 30, 2026]
[2] Python Software Foundation. (n.d.). Errors and Exceptions. 
    docs.python.org. [Online]. Available at: 
    https://docs.python.org/3/tutorial/errors.html 
    [Accessed on: January 30, 2026]
[3] Python Software Foundation. (n.d.). Built-in Types. 
    docs.python.org. [Online]. Available at: 
    https://docs.python.org/3/library/stdtypes.html 
    [Accessed on: January 30, 2026]

"""

import csv
from record import OysterCatcherRecord

STUDENT_NAME = "Rakiba Chowdhury"

CSV_FILE = "pacific_rim_npr_coastalmarine_black_oystercatcher_population_nesting_counts_2008-2017_data.csv"
NUM_RECORDS_TO_LOAD = 5



def load_records(filename: str, limit:int) -> list[OysterCatcherRecord]:
    """
    Load records from CSV and parse into OysterCatcherRecord objects.

    Args:
        filename: Path to CSV file
        limit: Maximum records to load

    Returns:
        List of OysterCatcherRecord objects
    """
    records: list[OysterCatcherRecord] = []

    try:
        with open(filename, mode="r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            for i, row in enumerate(reader):
                if i >= limit:
                    break
                try:
                    record = OysterCatcherRecord.from_row(row)
                    records.append(record)
                except (ValueError, KeyError) as row_error:
                    # Skip bad rows but keep program running
                    print(f"{STUDENT_NAME} | Skipping row {i + 1} due to parse error: {row_error}")

    except FileNotFoundError:
        print(f"{STUDENT_NAME} | ERROR: Could not find the file: {filename}")   
    except PermissionError:
        print(f"{STUDENT_NAME} | ERROR: Permission denied when trying to open: {filename}")
    except Exception as e:
        print(f"{STUDENT_NAME} | ERROR: Unexpected problem reading file: {e}")

    return records

def main() -> None:
    """
    Main program entry point. Loads and displays Black Oystercatcher records.
    """
    print("=" * 60)
    print(f"Student: {STUDENT_NAME}")
    print("CST8002 Practical Project - Part 1")
    print("=" * 60)

    records = load_records(CSV_FILE, NUM_RECORDS_TO_LOAD)

    print(f"\nLoaded {len(records)} record(s) from the first {NUM_RECORDS_TO_LOAD} line(s).\n")

    for r in records:
        print(
            f"{STUDENT_NAME} | "
            f"date={r.visit_date}, site={r.site_id}, species={r.species}, total_adults={r.total_adults}"
    
        )

if __name__ == "__main__":
    main()

