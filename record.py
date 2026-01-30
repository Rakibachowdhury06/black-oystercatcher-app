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

The record class will represent one row from the Black Oystercatcher population dataset.
"""

class OysterCatcherRecord:
    def __init__(self, visit_date: str, site_id: int, species: str, total_adults: int):
        self.visit_date = visit_date
        self.site_id = site_id
        self.species = species
        self.total_adults = total_adults

    @classmethod
    def from_row(cls, row: dict):
            """
            Create an OystercatcherRecord object from a CSV row dictionary.
            """
            return cls(
                visit_date=row["Visit date"],
                site_id=int(row["Site identification"]),
                species=row["Species"],
                total_adults=int(row["Total Black oystercatcher adults"])
            )
        
    def __str__(self):
            """
            String representation used when printing the record.
            """
            return (
                f"Date: {self.visit_date},"
                f"Site: {self.site_id},"
                f"Species: {self.species},"
                f"Adults: {self.total_adults}"
            )