"""
CST8002 - Programming Language Research Project
Practical Project Part 4 - Project Release
Professor: Stanley Pieda
Due Date: April 12, 2026
Student: Rakiba Chowdhury
Section: 020

This module contains the OysterCatcherRecord class which represents
a single row from the Black Oystercatcher population dataset.

Dataset Source:
Parks Canada. (2017). Black Oystercatcher Population - Pacific Rim.
Available at: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02
License: Open Government Licence - Canada

References:
[1] Python Software Foundation. (2024). Classes. docs.python.org [Online].
 Available: https://docs.python.org/3/tutorial/classes.html [Accessed: Jan. 27, 2026].
"""


class OysterCatcherRecord:
    """
    Represents a single observation record from the Black OysterCatcher
    population nesting counts dataset (2008-2017).
    Each instance stores data from one row of the CSV file with attributes
    matching the dataset column names.

    Attributes:
        visit_date (str): Date of the observation visit.
        site_identification (int): Numeric identifier for the observation site.
        species (str): Scientific name of the species observed.
        total_black_oystercatcher_adults (int): Count of adult birds observed.
    """

    def __init__(self, visit_date, site_identification, species,
                 total_black_oystercatcher_adults):
        """
        Initialize an OysterCatcherRecord with observation data.

        Args:
            visit_date (str): Date of observation in DD/MM/YYYY format.
            site_identification (int): Numeric site identifier.
            species (str): Scientific or common species name.
            total_black_oystercatcher_adults (int): Number of adult birds counted.
        """
        self.visit_date = visit_date
        self.site_identification = site_identification
        self.species = species
        self.total_black_oystercatcher_adults = total_black_oystercatcher_adults

    @classmethod
    def from_row(cls, row):
        """
        Create an OysterCatcherRecord from a CSV row dictionary.

        Factory method that constructs a record object from a dictionary
        returned by csv.DictReader.

        Args:
            row (dict): Dictionary with keys matching CSV column headers.

        Returns:
            OysterCatcherRecord: New instance with data from the row.

        Raises:
            KeyError: If required column names are missing from row.
            ValueError: If numeric fields cannot be converted to int.
        """
        return cls(
            visit_date=row["Visit date"],
            site_identification=int(row["Site identification"]),
            species=row["Species"],
            total_black_oystercatcher_adults=int(row["Total Black oystercatcher adults"])
        )

    def to_list(self):
        """
        Convert the record to a list of values for CSV writing.

        Returns:
            list: Record fields in column order.
        """
        return [
            self.visit_date,
            self.site_identification,
            self.species,
            self.total_black_oystercatcher_adults
        ]

    def __str__(self):
        """
        Return a human-readable string representation of the record.

        Returns:
            str: Formatted string with all record fields.
        """
        return (f"Date: {self.visit_date}, "
                f"Site: {self.site_identification}, "
                f"Species: {self.species}, "
                f"Adults: {self.total_black_oystercatcher_adults}")